# Start Here — GitHub + Visual Studio Code

How to take this starter project from this folder to GitHub, in VS Code, step by step. No step here publishes anything or contacts Zoom. Publishing the repo and sending anything to Zoom are separate steps, on Jazz's word.

## What you already have

- This folder: `punjabi-captions-formal-proof-project/` — README, `src/proof.py`, `src/coverage.py`, `docs/FORMAL-MODEL.md`, this file.
- GitHub: your account is connected to Muse (OAuth done Nov 1, 2026). Repositories were **not** selected yet — you choose them.
- VS Code: free, from https://code.visualstudio.com — install it if it is not on your computer yet.

## Step 1 — Open it in VS Code (2 minutes)

1. Open VS Code.
2. **File → Open Folder…** and choose `punjabi-captions-formal-proof-project/`.
3. Open the Terminal in VS Code: **Terminal → New Terminal** (or Ctrl + ` ).
4. Check the proof runs:
   ```bash
   python3 src/proof.py
   python3 src/coverage.py
   ```
   You should see the chain, the falsifying row, and the coverage numbers with their verification flags.

## Step 2 — Turn the folder into a Git repo (1 minute)

In the VS Code terminal, in the project folder:

```bash
git init
git add .
git commit -m "Starter proof: Punjabi captions are practicable, using formal logic"
```

## Step 3 — Create the repo on GitHub (3 minutes)

1. Go to https://github.com/new — sign in with your GitHub account.
2. Repository name: `CanLearnUniversal` — the name you chose Nov 5, 2026.
3. Description: "Formal proof that adding Punjabi to Zoom captions is practicable, much needed, and improves quality and procedural fairness."
4. Choose **Public** or **Private** — Private is the safer choice while it is a draft. You can make it Public later, on your word.
5. Do **not** tick "Add a README" / ".gitignore" / "license" — this folder already has a README.
6. Click **Create repository**.

## Step 4 — Push it from VS Code (2 minutes)

GitHub will show you commands after creating the repo. In the VS Code terminal, use the ones for an existing repo — they look like this (replace `YOUR-USERNAME` with your GitHub username):

```bash
git remote add origin https://github.com/YOUR-USERNAME/CanLearnUniversal.git
git branch -M main
git push -u origin main
```

VS Code will ask you to sign in to GitHub the first time — use the browser sign-in it offers. After that, every change is:

```bash
git add .
git commit -m "Describe what you changed, in one line"
git push
```

Or use VS Code's Source Control panel (the branching icon on the left): Stage → Commit → Push. Same result, no terminal needed.

## Step 5 — What to do next, in order

1. **You review and correct this draft.** Nothing here is published yet.
2. **Verify the numbers** at Statistics Canada before any public use — `src/coverage.py` flags them on purpose. Update Nov 5, 2026: the Brampton mother-tongue figure (141,005, 23.7%) and the Canada-wide 942,000 speakers are now verified; the Brampton 189,235 / 29.1% "could speak" figure is still unverified — do not use it publicly.
3. **Decide Public or Private**, and whether to send the argument to Zoom (access@zoom.us) with this proof attached. The Nov 3 email already asked for Punjabi in automated and translated captions; this proof would strengthen it, not replace it.
4. **Only then** publish the repo and/or send anything.

## If you get stuck

- "Python not found" — install Python 3 from https://www.python.org, then close and reopen VS Code.
- "git not found" — install Git from https://git-scm.com, then close and reopen VS Code.
- "Permission denied on push" — you are signed in to the wrong GitHub account, or the repo name in the remote URL does not match the repo you created. Check `git remote -v`.
- Nothing here deletes or overwrites anything on GitHub until you push. Until then, everything is only on your computer.
