# BCPD Practice

A study app for the **BeingCert Certified Python Developer (BCPD)** exam.

190 questions across all 45 sub-objectives of the official exam objectives document, 33 of them
scenario questions. Every question containing code is **executed by the build** and its answer
asserted against what CPython actually does. If an answer disagreed with the interpreter, the
build would fail rather than ship.

That is the whole point. Practice sites key their questions by vote and disagree with each
other; Python answers are decidable by running them.

## Using it

Open `index.html`. That is the entire installation — one self-contained file with the questions
inlined, so it works by double-click with no server and no internet.

Three modes:

- **Study** — answer, see the explanation immediately, hand the question to an AI if you want it
  taught. Filter by domain, by sub-objective, or to scenario questions only.
- **Exam simulation** — 90 questions in 120 minutes, drawn to the blueprint weights
  (18/14/13/14/13/9/9), no feedback until the end. Filters are deliberately ignored here: a
  weighted simulation of a filtered pool is not a simulation of the exam.
- **My wrong answers** — everything you have got wrong, to drill again.

Progress is stored in the browser's localStorage. Nothing is uploaded and there is no account.

## Ask AI

After you answer, one button hands the question — with your choice, the correct answer and a
short tutoring instruction — to the assistant you picked in **Ask AI with** on the setup screen:
Claude, ChatGPT, Perplexity or Gemini. The choice is remembered.

**The prompt always goes to your clipboard as well as into the URL.** Prefill support is uneven
across assistants and changes without notice, so if the tab comes up empty, just paste.

**Private chat** uses the platform's own temporary-chat link where one exists. Only Claude and
ChatGPT expose that by URL, so the other two are unavailable while it is on. A web page cannot
force a browser incognito window — that is a browser restriction, not a missing feature.

Gemini accepts no prompt from a URL at all, so for Gemini the button copies first and *then*
offers to open it. Opening the tab immediately would steal focus before you could read the note
telling you to paste.

No API key, no sign-up, no cost beyond whatever free account you already have.

The button appears **only after you answer** — deliberately. A beginner with an always-available
tutor asks before struggling, and the struggle is where the learning happens.

## Building

The app is generated from the markdown bank. To change a question, edit the bank and rebuild:

```bash
python build-questions.py
```

The build:

1. **Leak-checks** the source for local filesystem paths before anything is copied, so a leaked
   path can never reach the published folder.
2. Mirrors the bank forward into `questions/`, so the authored copy and the shipped copy cannot
   drift.
3. Parses questions, options, answer keys, sub-objective tags, scenario flags and explanations.
4. **Executes every code snippet** and asserts the keyed answer against the result.
5. Reports coverage per sub-objective — domain totals hide empty bullets, so coverage is
   measured one level down.
6. Inlines the data into `index.html`.

Any validation failure or any disagreement between an answer and the interpreter exits non-zero
and writes nothing.

Requires Python 3.12 and NumPy (`pip install numpy`) for the Domain 4 questions. Tkinter
verification degrades gracefully where no display is available.

Pass `--skip-verify` to parse without executing. Do not ship a build made that way.

## Layout

```
questions/
  BCPD-Master-Question-Bank.md   the bank
  BCPD-Objectives.md             the blueprint, transcribed
  SOURCES.md                     method and provenance
build-questions.py
index.html                       the app, questions inlined
```

## Two things the vendor has not settled

The objectives PDF says **90 questions**, multiple-choice and scenario-based. The certification
web page says **80**, multiple choice only. Both are BeingCert's own documents. This app follows
the PDF. And no BeingCert document states which **Python version** is tested; the bank targets
and verifies against 3.12. Both are worth confirming before exam day.

See `questions/SOURCES.md` for the full method.

## The Special set

A fourth mode carries **133 questions from the tutor's own practice exam**
(`bpcd-practice-exam.vercel.app`), used with his permission.

They are kept in a separate array from the verified bank, not merged into it. The main
bank's claim is that every code answer was proved by execution; blending in questions that
carry someone else's key would quietly destroy that claim while appearing to strengthen it.

What the mining found:

- **130 of the 133 are tagged `PCAP`** in his own data — the Python Institute associate
  exam, a tier above BCPD.
- **His set contains no GUI Programming questions at all**, a domain worth 10% of the real
  paper. Drill it for difficulty, not for coverage.
- **Four keys disagreed with the interpreter** and are corrected in place, each explaining
  what changed. Two were real errors; two were malformed (one key read
  `0 (none of the above)`, another read `FALSE` — the option *text*, Excel-coerced).

The two banks were also checked against each other: **zero duplicate questions.** 190 + 133
is 323 distinct items, not a double count.

**Every one of the 133 carries an explanation**, written from the code's actual executed
output rather than from reading the snippet. **21 are flagged defective** and say why —
duplicate options, a stem asking for two answers where the key gives one, or code whose
real result no option offers. A defective question is shipped with the defect named rather
than dropped: meeting one and being told what is wrong with it teaches more than quietly
failing it, and the flagged list is what to hand back to the tutor.

## The printable sheet

- `BCPD-All-Questions.pdf` — all 323 questions across both banks, 82 pages.
- `BCPD-Special-Questions.pdf` — the practice-exam set on its own, 133 questions, 32 pages.

Correct options are marked in green. Rebuild with:

```bash
python ../special-extract/make_pdf.py
python ../special-extract/make_pdf.py --only special
```
