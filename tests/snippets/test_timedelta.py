# flake8: noqa: F841

import pandas as pd
import numpy as np

import datetime as dt


def test_types_init() -> None:
    td: pd.Timedelta = pd.Timedelta('1 hour')
    td2: pd.Timedelta = pd.Timedelta(pd.Timedelta('1 hour'))
    td3: pd.Timedelta = pd.Timedelta(dt.timedelta(hours=1))
    td4: pd.Timedelta = pd.Timedelta(1, unit='day')
    td5: pd.Timedelta = pd.Timedelta(value=1.005, unit='second')
    td_kwargs: pd.Timedelta = pd.Timedelta(days=1)
    td_kwargs2: pd.Timedelta = pd.Timedelta(weeks=1, days=1, hours=1, minutes=1)
    td_kwargs3: pd.Timedelta = pd.Timedelta(seconds=1, milliseconds=1, microseconds=1, nanoseconds=1)


def test_to_timedelta() -> None:
    td_no_unit: pd.Timedelta = pd.to_timedelta(1000)
    td: pd.Timedelta = pd.to_timedelta(1, "days")
    tde1: pd.Timedelta = pd.to_timedelta(1.05, "nanos", errors="ignore")
    tde2: pd.Timedelta = pd.to_timedelta(1, "millisecond", errors="raise")
    tde3: pd.Timedelta = pd.to_timedelta(1, "micros", errors="coerce")
    td_string: pd.Timedelta = pd.to_timedelta('1 days 06:05:01.00003')
    td_string2: pd.Timedelta = pd.to_timedelta('15.5us')
    tds: pd.Series = pd.to_timedelta(pd.Series([1, 1]), "hours")
    tdi2: pd.TimedeltaIndex = pd.to_timedelta(['1 days 06:05:01.00003', '15.5us', 'nan'])
    tdi3: pd.TimedeltaIndex = pd.to_timedelta(np.arange(5), unit='s')

