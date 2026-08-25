#!/usr/bin/env python3
"""Parse BCPD-Master-Question-Bank.md -> inlined question data for index.html.

Format contract
---------------
Domain header (sets the domain for every question below it):
    ## Domain 4 - Modules and Libraries

Question block:
    **Q42.** Stem text? *(Choose 2)*

    ```python
    i = 0
    ```

    - A. option
    - B. option

    ```verify
    assert i == 0
    ```

Answer row:
    | Q42 | A & C | 4.2 | authored | explanation |
      qid | letters | objective | src | why

The `verify` fence is what makes this bank different from a scraped one. The snippet is
executed, its stdout and any exception are exposed to the verify block as `_stdout` and
`_exc`, and the assertions run against the real result. A question whose keyed answer
disagrees with CPython **fails the build**. No answer here is asserted; each is shown.

Run: python build-questions.py [--skip-verify]
"""
import re
import sys
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKING = HERE.parent / "BCPD-questions"
SHIPPED = HERE / "questions"
MIRRORED = ("BCPD-Master-Question-Bank.md", "BCPD-Objectives.md", "SOURCES.md")

SKIP_VERIFY = "--skip-verify" in sys.argv

LEAKS = ("C:" + chr(92) + "Users" + chr(92), "C:/Users/", "/home/")


def leak_check(paths):
    """A local path in a published file discloses it. Fail loudly rather than scrub
    silently: an auto-scrub quietly misses any pattern it was not taught."""
    for doc in paths:
        text = doc.read_text(encoding="utf-8")
        for pat in LEAKS:
            if pat in text:
                sys.exit(f"ERROR: {doc.name} contains a local path ({pat!r}) and would "
                         f"publish it. Scrub it before building.")


# Check the source BEFORE mirroring, so a leaked file never reaches questions/ at all.
leak_check(sorted(WORKING.glob("*.md")))

# ---------------------------------------------------------------- mirror forward
# Two copies exist by design: the working folder is authored in, questions/ is what ships.
# Copy forward on every build so they cannot drift (the CAD build shipped a stale copy for
# a whole session because the script read the published folder while the log called the
# working folder canonical).
if (WORKING / MIRRORED[0]).exists():
    SHIPPED.mkdir(exist_ok=True)
    for name in MIRRORED:
        src = WORKING / name
        if not src.exists():
            continue
        dst = SHIPPED / name
        new = src.read_text(encoding="utf-8")
        if not dst.exists() or dst.read_text(encoding="utf-8") != new:
            dst.write_text(new, encoding="utf-8")
            print(f"Synced {name} -> questions/", file=sys.stderr)

leak_check(sorted(SHIPPED.glob('*.md')))

SRC = SHIPPED / "BCPD-Master-Question-Bank.md"
HTML = HERE / "index.html"
if not SRC.exists():
    sys.exit(f"ERROR: no question bank at {SRC}")

lines = SRC.read_text(encoding="utf-8").splitlines()

# ------------------------------------------------------------- pass 1: answer rows
answers = {}
ans_row = re.compile(
    r'^\|\s*Q(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*(.+?)\s*\|\s*$'
)
for ln in lines:
    m = ans_row.match(ln)
    if not m:
        continue
    letters = re.findall(r'\b([A-G])\b', m.group(2).strip())
    if not letters:
        continue
    # The Src column carries provenance, optionally with a "+scenario" suffix marking a
    # question written in the symptom-then-mechanism format the objectives PDF calls
    # "scenario based". Format and provenance are separate facts, so they are split here
    # rather than given a shared vocabulary that conflates them.
    raw_src = m.group(4).strip().lower()
    scen = "scenario" in raw_src
    src = "+".join(p for p in raw_src.split("+") if p and p != "scenario") or "unknown"
    answers[int(m.group(1))] = {
        "letters": letters,
        "obj": m.group(3).strip(),
        "src": src,
        "scen": scen,
        "why": m.group(5).strip().replace("**", ""),
    }

# --------------------------------------------------------- pass 2: question blocks
domain_hdr = re.compile(r'^##\s+Domain\s+(\d+)\b')
q_hdr = re.compile(r'^\*\*Q(\d+)\.\*\*\s*(.*)$')
opt_line = re.compile(r'^\s*-\s*([A-G])\.\s+(.*)$')
fence = re.compile(r'^\s*```(\w*)\s*$')

questions = []
cur_domain = None
i, n = 0, len(lines)
while i < n:
    ln = lines[i]
    dm = domain_hdr.match(ln)
    if dm:
        cur_domain = int(dm.group(1))
        i += 1
        continue
    qm = q_hdr.match(ln)
    if not qm:
        i += 1
        continue

    qid, stem = int(qm.group(1)), qm.group(2).strip()
    opts, letters, code, verify = [], [], None, None
    j = i + 1
    while j < n:
        l2 = lines[j]
        # a fenced block: python = shown to the learner, verify = executed against it
        fm = fence.match(l2)
        if fm:
            kind = fm.group(1) or "text"
            body, k = [], j + 1
            while k < n and not fence.match(lines[k]):
                body.append(lines[k])
                k += 1
            block = "\n".join(body)
            if kind == "verify":
                verify = block
            else:
                code = block if code is None else code + "\n" + block
            j = k + 1
            continue
        om = opt_line.match(l2)
        if om:
            letters.append(om.group(1))
            opts.append(om.group(2).strip())
            j += 1
            continue
        if not l2.strip():
            j += 1
            continue
        if l2.startswith("**Q") or l2.startswith("#") or l2.startswith("---") or l2.startswith("|"):
            break
        if not opts:
            stem += " " + l2.strip()          # stem wrapped onto the next line
            j += 1
            continue
        break

    stem = re.sub(r'\s*\*?\(Choose[^)]*\)\*?\s*$', '', stem).strip().replace("**", "")
    questions.append({
        "qid": qid, "d": cur_domain, "stem": stem,
        "opts": opts, "letters": letters, "code": code, "verify": verify,
    })
    i = j

# ------------------------------------------------------------------ merge + validate
LET2IDX = {c: k for k, c in enumerate("ABCDEFG")}
out, errors, warnings = [], [], []
seen = set()

for q in sorted(questions, key=lambda x: x["qid"]):
    qid = q["qid"]
    if qid in seen:
        errors.append(f"Q{qid}: duplicate question number")
        continue
    seen.add(qid)
    a = answers.get(qid)
    if a is None:
        errors.append(f"Q{qid}: no answer row found")
        continue
    ans_idx = sorted(LET2IDX[c] for c in a["letters"])
    if len(q["opts"]) < 2:
        errors.append(f"Q{qid}: only {len(q['opts'])} options")
    for x in ans_idx:
        if x >= len(q["opts"]):
            errors.append(f"Q{qid}: answer index {x} >= option count {len(q['opts'])}")
    if q["d"] is None:
        errors.append(f"Q{qid}: no '## Domain N' header above it")
    if not a["obj"]:
        errors.append(f"Q{qid}: no sub-objective tag")
    elif q["d"] is not None and not a["obj"].startswith(f"{q['d']}."):
        errors.append(f"Q{qid}: objective {a['obj']} does not belong to domain {q['d']}")
    if q["code"] and not q["verify"]:
        warnings.append(f"Q{qid}: has a code block but no verify block - answer is asserted, not proven")
    out.append({
        "id": qid, "d": q["d"], "obj": a["obj"], "q": q["stem"],
        "code": q["code"], "opts": q["opts"], "ans": ans_idx,
        "multi": len(ans_idx) > 1, "src": a["src"], "scen": a["scen"], "exp": a["why"],
    })

for qid in sorted(set(answers) - seen):
    errors.append(f"Q{qid}: answer row with no question block")

# ------------------------------------------------------- the interpreter is the authority
RUNNER = r'''
import sys, json, io, contextlib, os, tempfile
job = json.load(sys.stdin)
# Domain 6 snippets create real files. Run every snippet from a throwaway directory so a
# question can never write into the repo - the first build dropped five stray .txt files
# next to index.html because the chdir lived in the verify block, which runs too late.
os.chdir(tempfile.mkdtemp(prefix="bcpd-verify-"))
ns, buf, exc = {}, io.StringIO(), None
# A verify block starting "# noexec" means the displayed snippet must NOT be run - it
# blocks (a GUI mainloop), waits on stdin, or is a pseudo-listing. The verify block then
# proves the claim on its own terms instead of being skipped, which is the point: an
# unrunnable snippet is still an answer that has to be shown rather than asserted.
if job["verify"].lstrip().startswith("# noexec"):
    job = dict(job, code="")
try:
    with contextlib.redirect_stdout(buf):
        exec(compile(job["code"], "<snippet>", "exec"), ns)
except BaseException as e:
    exc = e
ns["_stdout"] = buf.getvalue()
ns["_exc"] = exc
exec(compile(job["verify"], "<verify>", "exec"), ns)
'''

verified = 0
if not SKIP_VERIFY:
    jobs = [q for q in questions if q["code"] and q["verify"]]
    for q in jobs:
        payload = json.dumps({"code": q["code"], "verify": q["verify"]})
        try:
            r = subprocess.run([sys.executable, "-c", RUNNER], input=payload,
                               capture_output=True, text=True, timeout=10)
        except subprocess.TimeoutExpired:
            errors.append(f"Q{q['qid']}: verification timed out (infinite loop in the snippet?)")
            continue
        if r.returncode != 0:
            tail = (r.stderr.strip().splitlines() or ["(no stderr)"])[-1]
            errors.append(f"Q{q['qid']}: VERIFY FAILED - {tail}")
        else:
            verified += 1

# ------------------------------------------------------------------------- report
print(f"Parsed {len(out)} questions", file=sys.stderr)
dc = Counter(o["d"] for o in out)
NAMES = {1: "Introduction and Setup", 2: "Data Structures", 3: "OOP",
         4: "Modules and Libraries", 5: "Debugging and Error Handling",
         6: "File Handling", 7: "GUI Programming"}
for d in range(1, 8):
    print(f"  D{d} {NAMES[d]:<30} {dc.get(d, 0):>4}", file=sys.stderr)

# Coverage by sub-objective. Domain totals hide empty bullets - this is the check that
# found two nearly-empty objectives in the CAD bank after the domain totals looked fine.
OBJS = []
for ln in (WORKING / "BCPD-Objectives.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r'^\|\s*(\d+\.\d+)\s*\|', ln)
    if m:
        OBJS.append(m.group(1))
oc = Counter(o["obj"] for o in out)
empty = [o for o in OBJS if oc.get(o, 0) == 0]
THIN_AT = 3
thin = [o for o in OBJS if 0 < oc.get(o, 0) < THIN_AT]
print(f"  objectives covered: {len(OBJS) - len(empty)}/{len(OBJS)}", file=sys.stderr)
if empty:
    print(f"  EMPTY objectives: {', '.join(empty)}", file=sys.stderr)
if thin:
    print(f"  thin (<3): {', '.join(thin)}", file=sys.stderr)

sc = Counter(o["src"] for o in out)
print("  by src: " + ", ".join(f"{k}={v}" for k, v in sorted(sc.items())), file=sys.stderr)
print(f"  multi-select: {sum(1 for o in out if o['multi'])}", file=sys.stderr)
print(f"  scenario format: {sum(1 for o in out if o['scen'])}", file=sys.stderr)
if SKIP_VERIFY:
    print("  VERIFICATION SKIPPED (--skip-verify)", file=sys.stderr)
else:
    noexec = sum(1 for q in questions
                 if q["verify"] and q["verify"].lstrip().startswith("# noexec"))
    print(f"  executed and verified: {verified}/{sum(1 for q in questions if q['code'])} "
          f"code questions ({noexec} proved without running the snippet)", file=sys.stderr)
for w in warnings:
    print("  warn: " + w, file=sys.stderr)
if errors:
    print("ERRORS:", file=sys.stderr)
    for e in errors:
        print("  " + e, file=sys.stderr)
    sys.exit(1)
print("  no validation errors", file=sys.stderr)

# --------------------------------------------------------------------------- emit
parts = [
    "{id:%d,d:%d,o:%s,q:%s,c:%s,opts:%s,ans:%s,multi:%s,src:%s,scen:%s,exp:%s}" % (
        o["id"], o["d"],
        json.dumps(o["obj"]),
        json.dumps(o["q"], ensure_ascii=False),
        json.dumps(o["code"], ensure_ascii=False) if o["code"] else "null",
        json.dumps(o["opts"], ensure_ascii=False),
        json.dumps(o["ans"]),
        "true" if o["multi"] else "false",
        json.dumps(o["src"]),
        "true" if o["scen"] else "false",
        json.dumps(o["exp"], ensure_ascii=False),
    )
    for o in out
]
js = "const QS = [\n" + ",\n".join(parts) + "\n];\n"

# Inlining the data into index.html keeps the file genuinely self-contained: it opens with a
# double-click over file:// (where fetch() is CORS-blocked) and can never serve a stale copy.
START, END = "<script id=\"qdata\">", "</script><!--/qdata-->"
html = HTML.read_text(encoding="utf-8")
a, b = html.find(START), html.find(END)
if a == -1 or b == -1:
    sys.exit("ERROR: qdata markers not found in index.html")
HTML.write_text(html[:a + len(START)] + "\n" + js + html[b:], encoding="utf-8")
print(f"Inlined {len(out)} questions into index.html", file=sys.stderr)
