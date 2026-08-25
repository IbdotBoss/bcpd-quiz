# Sources and method

## The standing rule

**No question in this bank is taken from a BeingCert exam.** Every question is written from
the published exam objectives and the CPython documentation, and every question containing
code is proved by executing it. If a claim cannot be settled by running it or by citing the
documentation, the question is dropped rather than guessed.

That rule exists for two reasons. Certification agreements restrict disclosing exam content,
and a memorised answer to a question you will not be asked is worth nothing anyway.

## What the bank is built from

| Source | What it contributes |
|---|---|
| The official objectives document | The seven domains, their weights, and all 45 sub-objectives. This is the scaffold; coverage is measured against it. |
| The CPython documentation | The authority for every non-executable claim - module contents, exception hierarchy, file modes, Tkinter widget behaviour. |
| The interpreter itself | The authority for every executable claim. See below. |
| NumPy documentation | Domain 4's array, operation and statistical objectives. |

`Src` values in the bank mean:

- **`authored`** - written from the documentation and proved by execution.
- **`docs`** - the documentation states the fact directly and is quoted or paraphrased.
- **`mined`** - a *misconception* was observed in the wild; the question testing it was then
  written from scratch and executed. No wording, options or answer key was copied.

## The interpreter is the authority

Every question with a code block carries a hidden `verify` block. On each build the snippet is
executed in a subprocess, its stdout and any exception are exposed to the verify block as
`_stdout` and `_exc`, and the assertions run against the real result.

**A question whose keyed answer disagrees with CPython fails the build.** It cannot ship.

At the last build: **106 of 106** code questions executed and verified, across **190** questions.

A verify block beginning `# noexec` marks a snippet that must not be run - one that blocks on a
GUI event loop, waits on stdin, or is a directory listing rather than a program. The verify
block then proves the same claim by other means. It is an escape hatch for unrunnable snippets,
not for unproven answers.

Verification interpreter: **CPython 3.12.10** with **NumPy 2.4.4**.

## Two things the vendor has not settled

1. **Question count and format.** The objectives document says 90 questions with multiple-choice
   *and scenario-based* items. The certification web page says 80 questions, 56 marks out of 80,
   multiple choice only. Both are BeingCert's own. This bank follows the objectives document.

2. **Python version.** No BeingCert document states one. This matters for dictionary ordering,
   f-strings, `match`, the walrus operator and integer caching. The bank targets 3.12 and avoids
   questions whose answer turns on a version difference.

Both are worth an email to BeingCert before exam day.

## One objective names something Python does not have

Objective **3.11, "Function Overloading/Polymorphism"**. Python has no function overloading -
there is no dispatch on arity or argument type, and a second `def` of the same name simply
replaces the first. Questions under 3.11 test what the blueprint most plausibly means and say so
in the explanation. It is flagged rather than guessed, because a question keyed on a feature
that does not exist is a coin flip.

## Why practice-site answer keys were not used

Where a "practice" or "dump" pool for an adjacent Python exam was examined, the finding was that
**nobody keys those questions** - the answer is a comment thread, and the thread disagrees with
itself. On one question three different answers were being argued, and part of the disagreement
traced to the code being published as an *image* in which `!=` was typeset with a space, which
would be a syntax error and was not in the original question at all.

Python is the rare subject where that dispute is settleable in seconds: run it. That is why this
bank executes instead of adjudicating.
