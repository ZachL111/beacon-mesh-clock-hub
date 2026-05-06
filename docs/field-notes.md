# Field Notes

The useful part of this repository is the small rule set around quorum health and replica lag.

The domain cases cover `quorum health`, `lease drift`, `replica lag`, and `membership churn`. They sit beside the smaller starter fixture so the project has both a compact scoring check and a domain-flavored review check.

`stale` is the strongest case at 209 on `quorum health`. `recovery` is the cautious anchor at 146 on `membership churn`.

The extra check gives the repository a behavior path that can fail for a domain reason, not only a syntax reason.
