# Beacon Mesh Clock Hub Walkthrough

This walk-through keeps the domain vocabulary close to the data instead of burying it in prose.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | quorum health | 187 | ship |
| stress | lease drift | 162 | ship |
| edge | replica lag | 157 | ship |
| recovery | membership churn | 146 | ship |
| stale | quorum health | 209 | ship |

Start with `stale` and `recovery`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

The next useful expansion would be a malformed fixture around lease drift and membership churn.
