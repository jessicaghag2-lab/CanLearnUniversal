# Punjabi Captions Are Practicable — A Formal Proof

**Status: DRAFT, PRIVATE, NOT PUBLISHED, NOT SENT. A starter project, built Nov 5, 2026, at Jazz's direction — to get it initiated, to show that adding Punjabi to Zoom's captions is practicable and much needed, and that including the people who speak that language is a great advantage that improves quality and procedural fairness. Using formal logic and mathematics.**

**Question:** Should Punjabi be added to Zoom's automated and translated captions?

**Answer this project proves, in symbols:** Yes — because inclusion is not a favour. It is a requirement in the chain that makes a process fair.

## The chain, in symbols

From the Precedentory work (corpus §27, Principle 16; law reform paper §11):

- **A** = absence of fear, anxiety, or insecurity
- **E** = efficiency
- **C** = certainty
- **J** = fairness — a process in which each party is heard, the decision is made on the evidence and the stated rule rather than on power or favour, the reasons are given in words that can be checked, the decision can be challenged, and the outcome can be relied on

**A → E → C → J**

Applied to captions, let:

- **I** = inclusion — a participant can follow the meeting in a language they understand (here: Punjabi captions, automated and translated)
- **U** = understanding — the participant knows what is happening, why, and how
- **P** = participation — the participant can speak, ask, challenge, and be heard, on the same terms as everyone else

**I → U → P → J**

Read it as a chain of requirements:

- **I → U:** Without captions in a language they understand, a Punjabi-speaking participant cannot understand what is happening in real time. They are not slow. They are excluded.
- **U → P:** Without understanding, there is no participation. A person who cannot follow the discussion cannot ask a question about it, challenge a claim in it, or consent to a decision made in it.
- **P → J:** Without participation, there is no procedural fairness — because procedural fairness *is* being heard, on the evidence and the stated rule, with reasons that can be checked. A process that decides a person's matter in a language they cannot follow is unfair *because* it excludes them, not in spite of it.

Remove I, and U collapses. Remove U, and P collapses. Remove P, and J collapses with it.

## The falsifying row

The claim "captions in other languages are enough" is busted by one row:

**¬I ∧ ¬J** — a Punjabi-speaking participant, no Punjabi captions, and an unfair process, *because* there were no Punjabi captions.

One such row is enough. It is not a hypothetical: Zoom's own translated-captions page, updated November 3, 2026, does not list Punjabi, while it lists Hindi, Bengali, Tamil, Telugu, and many others. A participant who speaks Punjabi and not those languages is the falsifying row, in real life.

## Practicability — why "it can't be done" fails

Practicability is proved, not asserted, by three facts:

1. **The pipeline already exists.** Zoom already does automated captions and translated captions in many languages. Adding a language is adding a language model to an existing pipeline, not inventing captioning.
2. **The language already exists in the data.** Punjabi is one of the most widely spoken languages in Canada — in Brampton, 141,005 people reported Punjabi as a mother tongue (23.7% of single responses, 2021 Census, verified Nov 5, 2026 in the City of Brampton Census Bulletin #3 compiling Statistics Canada), and 942,000 people across Canada could speak Punjabi (Statistics Canada, The Daily, Jan 22, 2025). The 189,235 (29.1%) "could speak Punjabi in Brampton" figure from the Nov 3 summary could **not** be verified — it is not in Bulletin #3, which instead gives 114,145 (17.54%) speaking Punjabi most often at home — so it stays flagged unverified in `src/coverage.py` and must not be used publicly until found at Statistics Canada. The speakers, the text, and the demand are already there.
3. **The test is the same test.** A proof that is testable, workable, learnable, and improvable is the procedure by which fear is removed (corpus §27–§28). Caption accuracy can be tested, measured, and improved in Punjabi exactly as it is tested, measured, and improved in every other language Zoom already supports.

A claim that it is impracticable would have to show which of those three fails. None of them does on the evidence available.

## Quality and procedural fairness — the advantage

Inclusion is a great advantage, not a cost, because it improves the process itself:

- **Quality:** a meeting where everyone can follow it produces better questions, better challenges, and better decisions. Errors that would have passed unnoticed get caught, because more people can actually hear them.
- **Procedural fairness:** a participant who can follow, ask, and challenge is a participant who has been heard. That is the definition of J above — and it is the definition that does not use the word "fair" in it.

## Why this matters

It helps advocate for the greater Punjabi community, wherever they may be. To empower and uplift. Despite bad, horrible pasts. To move from bitterness and cynicism — to better, and optimistic, and hopeful. ☺️

A language is not only a way of speaking. It is a way of belonging. When a Punjabi speaker can follow a meeting, a class, a hearing, or a family call in their own language, they are not only included. They are empowered — and a community that is empowered, wherever its people are, can move forward together, from what was, toward what can be.

It ties into our mental health advocacy passions and hobbies, too. Being heard in your own language — being understood, not talked past — is mental health. It is what "be someone's owl" means in practice: the lookout who makes sure nobody is left out of the conversation because of the language they speak.

## What this project is, and is not

- **Is:** a starter proof, in formal logic and mathematics, that Punjabi captions are practicable, much needed, and fairness-improving — built to be tested, corrected, and improved.
- **Is not:** a claim that any specific person at Zoom acted in bad faith, a legal finding, or a published paper. It is a draft argument, to be verified at primary sources before any public use.
- **Next step, on Jazz's word:** send the argument to Zoom (access@zoom.us — the email already sent Nov 3, 2026 asked for Punjabi in automated and translated captions), with this proof attached, or publish it as a standalone opinion.

## How to run it

```bash
# 1. Open this folder in Visual Studio Code
code .

# 2. Run the proof checker (Python 3, no extra packages)
python3 src/proof.py

# 3. Run the coverage check
python3 src/coverage.py
```

See `docs/START-HERE.md` for the full GitHub + VS Code setup, step by step.

## Files

- `README.md` — this file: the argument, in full
- `src/proof.py` — the chain and the falsifying row, as runnable logic
- `src/coverage.py` — the coverage numbers, with their sources and verification flags
- `docs/START-HERE.md` — how to start this project on GitHub and in Visual Studio Code
- `docs/FORMAL-MODEL.md` — the formal model, in symbols, with truth tables
