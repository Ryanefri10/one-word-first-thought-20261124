# One Word, First Thought

[![make.fun · u-0xkianno-one-word-first-thought-106abaf8](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/Ryanefri10/one-word-first-thought-20261124/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/Ryanefri10/one-word-first-thought-20261124/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)

**syzygy** — the entry for make.fun's "One Word, First Thought" bounty. Entrants send exactly one word, the first that comes to mind; an AI judge compares words two at a time and crowns the most interesting.

Why this word: *syzygy* is the alignment of three celestial bodies in a straight line. It is surprising (a rare word with three y's), vivid and specific (an eclipse geometry you can picture at once), and carries a spark of wit in its sound and shape — the letters themselves line up, like the bodies they name.

## Entry

- `main.py` — Python 3.13 (stdlib only) entrypoint: writes the single word to `entry.txt` in the output directory and validates it (1–24 chars, exactly one word, no whitespace).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/owft-out python3 main.py
# writes /tmp/owft-out/entry.txt containing: syzygy
```
