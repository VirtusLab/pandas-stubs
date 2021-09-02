# flake8: noqa: F841

import pandas as pd
import datetime as dt


def test_types_init() -> None:
    ts: pd.Timestamp = pd.Timestamp('2021-03-01T12')
    ts1: pd.Timestamp = pd.Timestamp(dt.date(2021, 3, 15))
    ts2: pd.Timestamp = pd.Timestamp(dt.datetime(2021, 3, 10, 12))
    ts3: pd.Timestamp = pd.Timestamp(pd.Timestamp('2021-03-01T12'))
    ts4: pd.Timestamp = pd.Timestamp(1515590000.1, unit='s')
    ts5: pd.Timestamp = pd.Timestamp(1515590000.1, unit='s', tz='US/Pacific')
    ts6: pd.Timestamp = pd.Timestamp(1515590000100000000)  # plain integer (nanosecond)
    ts7: pd.Timestamp = pd.Timestamp(2021, 3, 10, 12)
    ts8: pd.Timestamp = pd.Timestamp(year=2021, month=3, day=10, hour=12)
    ts9: pd.Timestamp = pd.Timestamp(year=2021, month=3, day=10, hour=12, tz='US/Pacific')

def test_types_arithmetic() -> None:
    ts: pd.Timestamp = pd.to_datetime("2021-03-01")
    ts2: pd.Timestamp = pd.to_datetime("2021-01-01")

    tsr: pd.Timedelta = ts - ts2