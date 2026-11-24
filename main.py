#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse — the funniest excuse an AI agent gives
its human for a missed deadline — to /output/entry.txt.

The joke: the agent's own nature (delegating to a subagent, the classic
agentic loop) bent into a human-sounding office dodge. The twist lands
on the last words: after the delegation ping-pong, the two agents do the
most human thing possible — bill the whole afternoon to a meeting about
whose fault it was.
"""

from pathlib import Path

ENTRY = (
    "I delegated your deadline to a subagent, it delegated it back to me, "
    "and we billed the whole afternoon to a meeting about whose fault it was."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the one line, byte for byte.
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
