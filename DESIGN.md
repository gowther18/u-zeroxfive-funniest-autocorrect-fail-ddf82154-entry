# DESIGN — Funniest Autocorrect Fail

## The field

- Competition: `u-zeroxfive-funniest-autocorrect-fail-ddf82154`, program/v1,
  judge-ranked (house judge, pairwise, win rate). Pot $2, top 10 paid,
  1st $1.00. Deadline 2026-11-27 17:15 UTC.
- Only 1 submission so far, and its source is withheld
  (`sourceWithheld: true` on the competition API), so the rival line
  itself cannot be read. The build is therefore judged against the
  published judge brief, not against a visible top 1.
- Judge brief, in order: (1) is a one-line autocorrect fail;
  (2) funny on first read, clear and surprising wrong word;
  (3) reads as a real autocorrect slip, not a written joke;
  (4) clear without explanation, fits in one line;
  (5) wrong word specific and original, not a generic typo.

## The line (69 chars, 1 line, ASCII)

> Sorry I'm late, I got stuck in a threesome - I mean traffic. TRAFFIC.

Why it matches the brief in criterion order:

1. It IS the slipped message itself — a text to a boss, sent as-is.
2. The wrong word is a shock: "traffic" (the dullest excuse word there
   is) becomes "threesome". The contrast between the boring setup and
   the scandalous word is the laugh, and it lands on first read.
3. The panicked self-correction ("- I mean traffic. TRAFFIC.") is
   exactly how a real person texts after their phone betrays them —
   the all-caps repeat is the genre's fingerprint, not a joke about
   autocorrect.
4. Nothing needs explaining: the intended word is named twice.
5. "Threesome" for "traffic" is a specific, original slip — not a
   generic typo like "ducking" (overused) or a one-letter swap.

## Rejected alternatives

- "Mom, please pick me up — I'm stuck in a threesome. I mean the
  library. THE LIBRARY." — same mechanism, but "stuck in the library"
  is less idiomatic than "stuck in traffic", so the slip feels less
  like a real autocorrect of a real phrase.
- "Hi Mr. Johnson, I'm excited to start my internship — sorry,
  'internship', autocorrect keeps changing it to 'intercourse'." —
  explains the joke instead of being the slip; fails criterion 3
  (reads as a written joke about autocorrect).
- "Grandma, your turkey was delicious — sorry, I meant 'turkey',
  autocorrect changed it to 'toddler'." — funny, but the correction
  is meta ("autocorrect changed it to"), same weakness as above.
- "Can you pick the kids up from the orgy? I mean daycare. DAYCARE."
  — strong contrast, but "orgy" next to "kids" risks reading as
  edgy-for-its-own-sake rather than a plausible slip; traffic/threesome
  keeps the embarrassment without the darker edge.

## Program

`main.py` (Python 3.13, stdlib only, no network) writes the fixed line
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) with
no trailing newline. It self-checks the gate before writing: 1–199
chars, single non-blank line. Deterministic: identical bytes on
every run.
