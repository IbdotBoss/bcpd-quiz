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

After you answer, **Ask Claude** / **Ask ChatGPT** open a new tab with the question, your choice,
the correct answer and a short tutoring instruction already filled in. **Copy instead** puts the
same prompt on the clipboard for any other assistant.

No API key, no sign-up, no cost beyond whatever free account you already have.

The buttons appear **only after you answer** — deliberately. A beginner with an always-available
tutor asks before struggling, and the struggle is where the learning happens. Answer first, get
it wrong, then have it explained.

Prefill support is uneven across assistants and changes without notice, so if the prompt arrives
empty, use **Copy instead**. That route works everywhere.

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
