# flake8: noqa: F841

import tempfile
from pathlib import Path

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
    csv_df: str = s.to_csv()

    with tempfile.NamedTemporaryFile() as file:
        s.to_csv(file.name)
        s2: pd.Series = pd.read_csv(file.name)

    with tempfile.NamedTemporaryFile() as file:
        s.to_csv(Path(file.name))
        s3: pd.Series = pd.read_csv(Path(file.name))

def test_types_select() -> None:
    s = pd.Series(data={'row1': 1, 'row2': 2})
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
    s[s]


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


def test_types_drop() -> None:
    s = pd.Series([0, 1, 2])
    s.drop(0)
    s.drop([0, 1])
    s.drop(0, axis=0)
    s.drop([0, 1], inplace=True, errors='raise')
    s.drop([0, 1], inplace=True, errors='ignore')


def test_types_drop_multilevel() -> None:
    index = pd.MultiIndex(levels=[['top', 'bottom'], ['first', 'second', 'third']],
                          codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
    s = pd.Series(data=[1, 2, 3, 4, 5, 6], index=index)
    s.drop(labels='first', level=1)


def test_types_dropna() -> None:
    s = pd.Series([1, np.nan, np.nan])
    s.dropna()
    s.dropna(axis=0, inplace=True)


def test_types_fillna() -> None:
    s = pd.Series([1, np.nan, np.nan, 3])
    s.fillna(0)
    s.fillna(0, axis='index')
    s.fillna(method='backfill', axis=0)
    s.fillna(method='bfill', inplace=True)
    s.fillna(method='pad')
    s.fillna(method='ffill', limit=1)


def test_types_sort_index() -> None:
    s = pd.Series([1, 2, 3], index=[2, 3, 1])
    s.sort_index()
    s.sort_index(ascending=False)
    s.sort_index(kind="mergesort")


def test_types_sort_values() -> None:
    s = pd.Series([4, 2, 1, 3])
    s.sort_values(0)
    s.sort_values(ascending=False)
    s.sort_values(inplace=False, kind='quicksort')
    s.sort_values(na_position='last')
    s.sort_values(ignore_index=True)


def test_types_shift() -> None:
    s = pd.Series([1, 2, 3])
    s.shift()
    s.shift(axis=0, periods=1)
    s.shift(-1, fill_value=0)


def test_types_rank() -> None:
    s = pd.Series([1, 1, 2, 5, 6, np.nan, 'milion'])
    s.rank()
    s.rank(axis=0, na_option='bottom')
    s.rank(method="min", pct=True)
    s.rank(method="dense", ascending=True)
    s.rank(method="first", numeric_only=True)


def test_types_mean() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.mean()
    s.mean(axis=0, level=0)
    s.mean(skipna=False)
    s.mean(numeric_only=False)


def test_types_median() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.median()
    s.median(axis=0, level=0)
    s.median(skipna=False)
    s.median(numeric_only=False)


def test_types_sum() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.sum()
    s.sum(axis=0, level=0)
    s.sum(skipna=False)
    s.sum(numeric_only=False)
    s.sum(min_count=4)


def test_types_cumsum() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.cumsum()
    s.cumsum(axis=0)
    s.cumsum(skipna=False)


def test_types_min() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.min()
    s.min(axis=0)
    s.min(level=0)
    s.min(skipna=False)


def test_types_max() -> None:
    s = pd.Series([1, 2, 3, np.nan])
    s.max()
    s.max(axis=0)
    s.max(level=0)
    s.max(skipna=False)


def test_types_quantile() -> None:
    s = pd.Series([1, 2, 3, 10])
    s.quantile([0.25, 0.5])
    s.quantile(0.75)
    s.quantile()
    s.quantile(interpolation='nearest')


def test_types_clip() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.clip(lower=0, upper=5)
    s.clip(lower=0, upper=5, inplace=True)


def test_types_abs() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.abs()


def test_types_var() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.var()
    s.var(axis=0, ddof=1)
    s.var(skipna=True, numeric_only=False)


def test_types_std() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.std()
    s.std(axis=0, ddof=1)
    s.std(skipna=True, numeric_only=False)


def test_types_idxmin() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.idxmin()
    s.idxmin(axis=0)


def test_types_idxmax() -> None:
    s = pd.Series([-10, 2, 3, 10])
    s.idxmax()
    s.idxmax(axis=0)


def test_types_value_counts() -> None:
    # Added in never Pandas version
    pass


def test_types_unique() -> None:
    s = pd.Series([-10, 2, 2, 3, 10, 10])
    s.unique()


def test_types_apply() -> None:
    s = pd.Series([-10, 2, 2, 3, 10, 10])
    s.apply(lambda x: x ** 2)
    s.apply(np.exp)
    s.apply(str)


def test_types_element_wise_arithmetic() -> None:
    s = pd.Series([0, 1, -10])
    s2 = pd.Series([7, -5, 10])

    s + s2
    s.add(s2, fill_value=0)

    s - s2
    s.sub(s2, fill_value=0)

    s * s2
    s.mul(s2, fill_value=0)

    s / s2
    s.div(s2, fill_value=0)

    s // s2
    s.floordiv(s2, fill_value=0)

    s % s2
    s.mod(s2, fill_value=0)


def test_types_concat() -> None:
    s = pd.Series([0, 1, -10])
    s2 = pd.Series([7, -5, 10])

    pd.concat([s, s2])
    pd.concat([s, s2], axis=1)
    pd.concat([s, s2], keys=['first', 'second'], sort=True)
    pd.concat([s, s2], keys=['first', 'second'], names=["source", "row"])


def test_types_groupby() -> None:
    s = pd.Series([4, 2, 1, 8], index=['a', 'b', 'a', 'b'])
    s.groupby(['a', 'b', 'a', 'b'])
    s.groupby(level=0)
    s.groupby(s > 2)


# This novelty added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_group_by_with_dropna_keyword() -> None:
    s = pd.Series([1, 2, 3, 3], index=['col1', 'col2', 'col3', np.nan])
    s.groupby(level=0, dropna=True).sum()
    s.groupby(level=0, dropna=False).sum()
    s.groupby(level=0).sum()


def test_types_plot() -> None:
    s = pd.Series([0, 1, 1, 0, -10])
    s.plot.hist()


def test_types_window() -> None:
    s = pd.Series([0, 1, 1, 0, 5, 1, -10])
    s.expanding()
    s.expanding(axis=0, center=True)

    s.rolling(2)
    s.rolling(2, axis=0, center=True)
