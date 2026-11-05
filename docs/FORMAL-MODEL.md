# Formal Model — Punjabi Captions, in Symbols

**Status: DRAFT. Part of the starter project `punjabi-captions-formal-proof-project`.**

## Notation

| Symbol | Meaning |
|---|---|
| A | Absence of fear, anxiety, or insecurity |
| E | Efficiency — a process that reaches a decision, on the evidence and the law, within a time and at a cost the parties can actually bear, without unnecessary steps, repetitions, or delays |
| C | Certainty — a person can know, in advance, what the rule is, what the process will be, what evidence counts, and what will happen |
| J | Fairness — each party is heard, the decision is made on the evidence and the stated rule rather than on power or favour, the reasons are given in words that can be checked, the decision can be challenged, and the outcome can be relied on |
| I | Inclusion — a participant can follow the meeting in a language they understand (here: Punjabi captions) |
| U | Understanding — the participant knows what is happening, why, and how |
| P | Participation — the participant can speak, ask, challenge, and be heard, on the same terms as everyone else |

## The chains

**A → E → C → J**

**I → U → P → J**

Each arrow is a requirement, not a preference. Read A → E as: if A, then E is possible; if ¬A, E is blocked. The same for each link.

## Truth table — one link

| p | q | p → q |
|---|---|---|
| T | T | T |
| T | F | **F** — the only row where implication fails |
| F | T | T |
| F | F | T |

The chain fails exactly when a link is broken: A true and E false, E true and C false, or C true and J false. Run `python3 src/proof.py` to see all 16 rows of the A/E/C/J chain.

## The falsifying row

Claim to bust: "Captions in other languages are enough for procedural fairness."

Falsifying row: **¬I ∧ ¬J**

A Punjabi-speaking participant, no Punjabi captions, and an unfair process — unfair *because* there were no Punjabi captions. One such row is enough to bust the claim. Zoom's translated-captions page (updated Nov 3, 2026) does not list Punjabi, while listing Hindi, Bengali, Tamil, Telugu, and many others. That participant is the row, in real life.

## Practicability — the three conditions

Let **Pr** = "adding Punjabi captions is practicable."

Pr holds if all three hold:

1. **Pipe** — the caption pipeline already exists in many languages.
2. **Data** — Punjabi speakers and text data already exist at scale.
3. **Test** — caption accuracy can be tested, measured, and improved in Punjabi as in every other supported language.

**Pr ↔ (Pipe ∧ Data ∧ Test)**

To prove ¬Pr, show ¬Pipe, or ¬Data, or ¬Test. On the evidence in the README, none of the three fails. Therefore ¬Pr is not proved.

## What would change the answer

- If Zoom published a test showing Punjabi caption accuracy cannot be measured or improved by the same method as other languages, condition (3) would fail — and this model would say so, on the record.
- If the census figures, once verified at Statistics Canada, turned out materially different, the coverage numbers in `src/coverage.py` must be corrected — the chain does not depend on any single number, only on I being false for a real population.
- If a participant who needs Punjabi captions can already follow every Zoom meeting in another language they understand, then for *that* participant I is not false. The claim is about the population that cannot, not about any one person.
