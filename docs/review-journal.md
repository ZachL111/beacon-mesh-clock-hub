# Review Journal

The cases below are the review handles I would use before changing the implementation.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its distributed systems focus without claiming live deployment or external usage.

## Cases

- `baseline`: `quorum health`, score 187, lane `ship`
- `stress`: `lease drift`, score 162, lane `ship`
- `edge`: `replica lag`, score 157, lane `ship`
- `recovery`: `membership churn`, score 146, lane `ship`
- `stale`: `quorum health`, score 209, lane `ship`

## Note

A future change should add new cases before it changes the scoring rule.
