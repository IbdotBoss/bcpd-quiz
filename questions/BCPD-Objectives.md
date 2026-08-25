# BCPD — Exam objectives (transcribed from the official PDF)

Source: `BCPD_169.pdf`, BeingCert "Python Developer Exam Objectives", downloaded from
`beingcert.com/ExamCurriculum/BCPD_169.pdf`. This file is a **verbatim transcription of the
blueprint only** — no exam content. It is the scaffold every question in the bank maps to.

## Exam facts

Per the objectives PDF:

- **90 questions · 120 minutes · pass 70%**
- Question types: **multiple choice and scenario-based**
- Certification valid 3 years

> ⚠️ **The vendor contradicts itself.** The certification web page states **80 questions**
> and **56 marks out of 80**, multiple choice only. Both documents are BeingCert's own.
> The bank follows the PDF (90 / MCQ + scenario) because it is the harder case and the
> document carrying the detailed objectives. **Confirm with BeingCert before exam day.**

> ⚠️ **No Python version is stated anywhere.** This matters for dict ordering, f-strings,
> `match`, the walrus operator and `int` caching. The bank assumes **CPython 3.12** and
> every question is executed against it. Ask BeingCert what they test.

## Domain weights

| # | Domain | Weight | Exam sim draw (of 90) |
|---|---|---|---|
| 1 | Introduction and Setup | 20% | 18 |
| 2 | Data Structures | 15% | 14 |
| 3 | Object-Oriented Programming | 15% | 13 |
| 4 | Modules and Libraries | 15% | 14 |
| 5 | Debugging and Error Handling | 15% | 13 |
| 6 | File Handling | 10% | 9 |
| 7 | GUI Programming | 10% | 9 |

Draw totals 90. Weights of 15% do not divide evenly into 90, so the four 15% domains take
14/13/14/13 rather than 13.5 each; the split is fixed so a run is reproducible.

## Sub-objectives

Every question carries an `Obj` tag from this list. Coverage is measured against it, not
against domain totals — domain totals hide empty sub-objectives.

### 01 — Introduction and Setup (20%)

| Obj | Title |
|---|---|
| 1.1 | Introduction to programming language |
| 1.2 | Setting up your programming environment |
| 1.3 | Variables, expressions, and statements |
| 1.4 | Control structures |

### 02 — Data Structures (15%)

| Obj | Title |
|---|---|
| 2.1 | Lists |
| 2.2 | Tuples |
| 2.3 | Dictionaries |
| 2.4 | Sets |

### 03 — Object-Oriented Programming (15%)

| Obj | Title |
|---|---|
| 3.1 | Object-oriented programming concepts |
| 3.2 | Creating classes |
| 3.3 | Creating instance objects |
| 3.4 | Constructors, Initializers |
| 3.5 | Accessing attributes |
| 3.6 | Object-oriented programming terminology |
| 3.7 | Encapsulation |
| 3.8 | Inheritance |
| 3.9 | Overriding methods |
| 3.10 | Data hiding |
| 3.11 | Function Overloading/Polymorphism |

> ⚠️ **3.11 names something Python does not have.** Python has no function overloading —
> no dispatch on arity or argument type; a second `def` of the same name simply replaces
> the first. Questions under 3.11 test what the blueprint most plausibly means
> (polymorphism, duck typing, method overriding, default/`*args` as the Python idiom for
> variable call signatures) and say so in the explanation. Flagged, not guessed.

### 04 — Modules and Libraries (15%)

| Obj | Title |
|---|---|
| 4.1 | Importing a module |
| 4.2 | Standard modules — random, math, sys, re, time, datetime |
| 4.3 | Creating modules |
| 4.4 | Executing modules as scripts |
| 4.5 | Working with packages |
| 4.6 | Numpy — Arrays |
| 4.7 | Numpy |
| 4.8 | Array operations |
| 4.9 | Statistical functions |

> 4.6 and 4.7 are near-duplicates in the source document. Treated as: **4.6 = creating and
> describing arrays** (`array`, `arange`, `zeros`, `dtype`, `shape`, `ndim`), **4.7 = what
> NumPy is and why it differs from a list** (homogeneous, fixed type, contiguous).

### 05 — Debugging and Error Handling (15%)

| Obj | Title |
|---|---|
| 5.1 | Errors and Exceptions |
| 5.2 | Using try-except blocks |
| 5.3 | The else block |
| 5.4 | User defined exceptions |
| 5.5 | Handling the Zero Division error exception |
| 5.6 | Handling the File Not Found error exception |

### 06 — File Handling (10%)

| Obj | Title |
|---|---|
| 6.1 | Files and file paths |
| 6.2 | Absolute and relative paths |
| 6.3 | Reading from a file |
| 6.4 | Writing to a file |
| 6.5 | Working with Directories |
| 6.6 | os and os.path modules |

### 07 — GUI Programming (10%)

| Obj | Title |
|---|---|
| 7.1 | Introduction to GUI Programming |
| 7.2 | Basic GUI Components |
| 7.3 | Event-Driven Programming |
| 7.4 | Layout Management |
| 7.5 | Tkinter |

**45 sub-objectives total.**

## Prerequisites (verbatim from the PDF)

Basic computer skills · basic math skills · familiarity with programming concepts
(helpful, not required) · a computer with internet access.

The exam is pitched at an **entry-level IT professional**. Calibrate difficulty to that,
not to Python Institute's PCAP, which is a tier above.
