import tempfile

import pandas as pd
import numpy as np


def test_types_init() -> None:
    pd.Series(1)
    pd.Series((1, 2, 3))
    pd.Series(np.array([1, 2, 3]))
    pd.Series(data=[1, 2, 3, 4], name="series")
    pd.Series(data=[1, 2, 3, 4], dtype=np.int8)
    pd.Series(data={'row1': [1, 2], 'row2': [3, 4]})
    pd.Series(data=[1, 2, 3, 4], index=[4, 3, 2, 1], copy=True)


def test_types_csv() -> None:
    s = pd.Series(data=[1, 2, 3])
    with tempfile.TemporaryFile() as file:
        s.to_csv()
        s.to_csv(file.name)
        s.to_csv(file)
        pd.read_csv()
        pd.read_csv(file)
        pd.read_csv(file.name)


def test_types_select() -> None:
    s = pd.Series(data={'row1': 1, 'row2': 2})
    s['col1']
    s[0]
    s[1:]


def test_types_iloc_iat() -> None:
    s = pd.Series(data={'row1': 1, 'row2': 2})
    s2 = pd.Series(data=[1, 2])
    s.loc['row1']
    s.iat[0]
    s2.loc[0]
    s2.iat[0]


def test_types_loc_at() -> None:
    s = pd.Series(data={'row1': 1, 'row2': 2})
    s2 = pd.Series(data=[1, 2])
    s.loc['row1']
    s.at['row1']
    s2.loc[1]
    s2.at[1]


def test_types_boolean_indexing() -> None:
    s = pd.Series([0, 1, 2])
    s[s > 1]
    s[pd]


def test_types_head_tail() -> None:
    s = pd.Series([0, 1, 2])
    s.head(1)
    s.tail(1)


def test_types_sample() -> None:
    s = pd.Series([0, 1, 2])
    s.sample(frac=0.5)
    s.sample(n=1)


def test_types_nlargest_nsmallest() -> None:
    s = pd.Series([0, 1, 2])
    s.nlargest(1)
    s.nlargest(1, 'first')
    s.nsmallest(1, 'last')
    s.nsmallest(1, 'all')


def test_types_filter() -> None:
    s = pd.Series(data=[1, 2, 3, 4], index=['cow', 'coal', 'coalesce', ''])
    s.filter(items=['cow'])
    s.filter(regex='co.*')
    s.filter(like='al')


def test_types_setting() -> None:
    s = pd.Series([0, 1, 2])
    s[3] = 4
    s[s == 1] = 5