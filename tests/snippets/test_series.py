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
