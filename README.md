# beacon-mesh-clock-hub

`beacon-mesh-clock-hub` keeps a focused SQL implementation around distributed systems. The project goal is to implement an SQL distributed systems project for clock graph analysis, using node-edge fixtures and cycle and reachability reports.

## Why I Keep It Small

I want this repository to be useful as a quick reading exercise: fixtures first, implementation second, verifier last.

## Beacon Mesh Clock Hub Review Notes

For a quick review, compare `quorum health` with `membership churn` before reading the middle cases.

## Included Behavior

- `fixtures/domain_review.csv` adds cases for quorum health and lease drift.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/beacon-mesh-clock-walkthrough.md` walks through the case spread.
- The SQL code includes a review path for `quorum health` and `membership churn`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Internal Model

The core code exposes a scoring path and the added review layer uses `signal`, `slack`, `drag`, and `confidence`. The domain terms are `quorum health`, `lease drift`, `replica lag`, and `membership churn`.

The SQL checks add a separate view over the domain review fixture.

## Try It Locally

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Validation

The same command runs the local verification path. The highest-scoring domain case is `stale` at 209, which lands in `ship`. The most cautious case is `recovery` at 146, which lands in `ship`.

## Scope

This remains a local project with deterministic fixtures. It does not depend on credentials, hosted services, or live data. Future work should add richer malformed inputs before widening the public API.
