# flake8: noqa: F841

import pandas as pd


def test_interval_init() -> None:
    i1: pd.Interval = pd.Interval(1, 2, closed='both')
    i2: pd.Interval = pd.Interval(1, right=2, closed='right')
    i3: pd.Interval = pd.Interval(left=1, right=2, closed='left')


def test_interval_arithmetic() -> None:
    i1: pd.Interval = pd.Interval(1, 2, closed='both')
    i2: pd.Interval = pd.Interval(1, right=2, closed='right')

    i3: pd.Interval = i1 + 1
    i4: pd.Interval = i1 - 1
    i5: pd.Interval = i1 * 2
    i6: pd.Interval = i1 / 2
    i7: pd.Interval = i1 // 2

