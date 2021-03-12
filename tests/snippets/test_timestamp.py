# flake8: noqa: F841

import pandas as pd
import datetime as dt

def test_types_init() -> None:
    ts: pd.Timestamp = pd.Timestamp('2021-03-01T12')
    ts1: pd.Timestamp = pd.Timestamp(dt.date(2021, 3, 15))
    ts2: pd.Timestamp = pd.Timestamp(1515590000.1, unit='s')
    ts3: pd.Timestamp = pd.Timestamp(1515590000.1, unit='s', tz='US/Pacific')
    ts4: pd.Timestamp = pd.Timestamp(2021, 3, 10, 12)
    ts5: pd.Timestamp = pd.Timestamp(year=2021, month=3, day=10, hour=12)
    ts6: pd.Timestamp = pd.Timestamp(year=2021, month=3, day=10, hour=12, tz='US/Pacific')
