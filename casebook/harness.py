"""Executable checks for the beacon-mesh-clock-hub casebook."""

from __future__ import annotations

from collections import Counter

from . import beacon_mesh_clock_hub_segment_00
from . import beacon_mesh_clock_hub_segment_01
from . import beacon_mesh_clock_hub_segment_02
from . import beacon_mesh_clock_hub_segment_03
from . import beacon_mesh_clock_hub_segment_04
from . import beacon_mesh_clock_hub_segment_05
from . import beacon_mesh_clock_hub_segment_06
from . import beacon_mesh_clock_hub_segment_07
from . import beacon_mesh_clock_hub_segment_08
from . import beacon_mesh_clock_hub_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from beacon_mesh_clock_hub_segment_00.iter_beacon_mesh_clock_hub_00()
    yield from beacon_mesh_clock_hub_segment_01.iter_beacon_mesh_clock_hub_01()
    yield from beacon_mesh_clock_hub_segment_02.iter_beacon_mesh_clock_hub_02()
    yield from beacon_mesh_clock_hub_segment_03.iter_beacon_mesh_clock_hub_03()
    yield from beacon_mesh_clock_hub_segment_04.iter_beacon_mesh_clock_hub_04()
    yield from beacon_mesh_clock_hub_segment_05.iter_beacon_mesh_clock_hub_05()
    yield from beacon_mesh_clock_hub_segment_06.iter_beacon_mesh_clock_hub_06()
    yield from beacon_mesh_clock_hub_segment_07.iter_beacon_mesh_clock_hub_07()
    yield from beacon_mesh_clock_hub_segment_08.iter_beacon_mesh_clock_hub_08()
    yield from beacon_mesh_clock_hub_segment_09.iter_beacon_mesh_clock_hub_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def beacon_mesh_clock_hub_summary() -> dict:
    return assert_expected()
