# flake8: noqa: F841

import tempfile
from pathlib import Path

import pandas as pd
import numpy as np


def test_types_init() -> None:
    pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]}, index=[2, 1])
    pd.DataFrame(data=[1, 2, 3, 4], dtype=np.int8)
    pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'], dtype=np.int8, copy=True)


def test_types_csv() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    csv_df: str = df.to_csv()

    with tempfile.NamedTemporaryFile() as file:
        df.to_csv(file.name)
        df2: pd.DataFrame = pd.read_csv(file.name)

    with tempfile.NamedTemporaryFile() as file:
        df.to_csv(Path(file.name))
        df3: pd.DataFrame = pd.read_csv(Path(file.name))

    # This keyword was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    with tempfile.NamedTemporaryFile() as file:
        df.to_csv(file.name, errors='replace')
        df4: pd.DataFrame = pd.read_csv(file.name)


def test_types_getitem() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4], 5: [6, 7]})
    i = pd.Index(['col1', 'col2'])
    s = pd.Series(['col1', 'col2'])
    select_df = pd.DataFrame({'col1': [True, True], 'col2': [False, True]})
    a = np.array(['col1', 'col2'])
    df['col1']
    df[5]
    df[['col1', 'col2']]
    df[1:]
    df[s]
    df[a]
    df[select_df]
    df[i]


def test_slice_setitem() -> None:
    # Due to the bug in pandas 1.2.3(https://github.com/pandas-dev/pandas/issues/40440), this is in separate test case
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4], 5: [6, 7]})
    df[1:] = ['a', 'b', 'c']


def test_types_setitem() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4], 5: [6, 7]})
    i = pd.Index(['col1', 'col2'])
    s = pd.Series(['col1', 'col2'])
    select_df = pd.DataFrame({'col1': [True, True], 'col2': [False, True]})
    a = np.array(['col1', 'col2'])
    df['col1'] = [1, 2]
    df[5] = [5, 6]
    df[['col1', 'col2']] = [[1, 2], [3, 4]]
    df[s] = [5, 6]
    df[a] = [[1, 2], [3, 4]]
    df[select_df] = [1, 2, 3]
    df[i] = [8, 9]


def test_types_iloc_iat() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.iloc[1, 1]
    df.iloc[[1], [1]]
    df.iat[0, 0]


def test_types_loc_at() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.loc[[0], 'col1']
    df.at[0, 'col1']


def test_types_boolean_indexing() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df[df > 1]
    df[~(df > 1.0)]


def test_types_head_tail() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.head(1)
    df.tail(1)


def test_types_assign() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.assign(col3=lambda frame: frame.sum(axis=1))
    df['col3'] = df.sum(axis=1)


def test_types_sample() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.sample(frac=0.5)
    df.sample(n=1)


def test_types_nlargest_nsmallest() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.nlargest(1, 'col1')
    df.nsmallest(1, 'col2')


def test_types_filter() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.filter(items=['col1'])
    df.filter(regex='co.*')
    df.filter(like='1')


def test_types_setting() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df['col1'] = 1
    df[df == 1] = 7


def test_types_drop() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    res: pd.DataFrame = df.drop('col1', axis=1)
    res2: pd.DataFrame = df.drop(columns=['col1'])
    res3: None = df.drop([0, 0], inplace=True)


def test_types_dropna() -> None:
    df = pd.DataFrame(data={'col1': [np.nan, np.nan], 'col2': [3, np.nan]})
    res: pd.DataFrame = df.dropna()
    res2: pd.DataFrame = df.dropna(axis=1, thresh=1)
    res3: None = df.dropna(axis=0, how='all', subset=['col1'], inplace=True)


def test_types_fillna() -> None:
    df = pd.DataFrame(data={'col1': [np.nan, np.nan], 'col2': [3, np.nan]})
    res: pd.DataFrame = df.fillna(0)
    res2: None = df.fillna(method='pad', axis=1, inplace=True)


def test_types_sort_index() -> None:
    df = pd.DataFrame(data={'col1': [1, 2, 3, 4]}, index=[5, 1, 3, 2])
    res: pd.DataFrame = df.sort_index()
    res2: pd.DataFrame = df.sort_index(ascending=False)
    res3: None = df.sort_index(kind="mergesort", inplace=True)


# This was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_sort_index_with_key() -> None:
    df = pd.DataFrame(data={'col1': [1, 2, 3, 4]}, index=['a', 'b', 'C', 'd'])
    res: pd.DataFrame = df.sort_index(key=lambda k: k.str.lower())


def test_types_set_index() -> None:
    df = pd.DataFrame(data={'col1': [1, 2, 3, 4], 'col2': ['a', 'b', 'c', 'd']}, index=[5, 1, 3, 2])
    res: pd.DataFrame = df.set_index('col1')
    res2: pd.DataFrame = df.set_index('col1', drop=False)
    res3: pd.DataFrame = df.set_index('col1', append=True)
    res4: pd.DataFrame = df.set_index('col1', verify_integrity=True)
    res5: pd.DataFrame = df.set_index(['col1', 'col2'])
    res6: None = df.set_index('col1', inplace=True)


def test_types_query() -> None:
    df = pd.DataFrame(data={'col1': [1, 2, 3, 4], 'col2': [3, 0, 1, 7]})
    res: pd.DataFrame = df.query("col1 > col2")
    res2: None = df.query("col1 % col2 == 0", inplace=True)


def test_types_eval() -> None:
    df = pd.DataFrame(data={'col1': [1, 2, 3, 4], 'col2': [3, 0, 1, 7]})
    df.eval("col1 > col2")
    res: None = df.eval("C = col1 % col2 == 0", inplace=True)


def test_types_sort_values() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    res: pd.DataFrame = df.sort_values('col1')
    res2: None = df.sort_values('col1', ascending=False, inplace=True)


# This was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_sort_values_with_key() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    res: pd.DataFrame = df.sort_values(by='col1', key=lambda k: -k)


def test_types_shift() -> None:
    df = pd.DataFrame(data={'col1': [1, 1], 'col2': [3, 4]})
    df.shift()
    df.shift(1)
    df.shift(-1)


def test_types_rank() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.rank(axis=0, na_option='bottom')
    df.rank(method="min", pct=True)
    df.rank(method="dense", ascending=True)
    df.rank(method="first", numeric_only=True)


def test_types_mean() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.mean()
    df.mean(axis=0)


def test_types_median() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.median()
    df.median(axis=0)


def test_types_sum() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.sum()
    df.sum(axis=1)


def test_types_cumsum() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.cumsum()
    df.sum(axis=0)


def test_types_min() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.min()
    df.min(axis=0)


def test_types_max() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.max()
    df.max(axis=0)


def test_types_quantile() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.quantile([0.25, 0.5])
    df.quantile(0.75)
    df.quantile()


def test_types_clip() -> None:
    df = pd.DataFrame(data={'col1': [20, 12], 'col2': [3, 14]})
    df.clip(lower=5, upper=15)


def test_types_abs() -> None:
    df = pd.DataFrame(data={'col1': [-5, 1], 'col2': [3, -14]})
    df.abs()


def test_types_var() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [1, 4]})
    df.var()
    df.var(axis=1, ddof=1)
    df.var(skipna=True, numeric_only=False)


def test_types_std() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [1, 4]})
    df.std()
    df.std(axis=1, ddof=1)
    df.std(skipna=True, numeric_only=False)


def test_types_idxmin() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.idxmin()
    df.idxmin(axis=0)


def test_types_idxmax() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.idxmax()
    df.idxmax(axis=0)


# This was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_value_counts() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [1, 4]})
    df.value_counts()


def test_types_unique() -> None:
    # This is really more for of a Series test
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [1, 4]})
    df['col1'].unique()


def test_types_apply() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.apply(lambda x: x ** 2)
    df.apply(np.exp)
    df.apply(str)


def test_types_applymap() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.applymap(lambda x: x ** 2)
    df.applymap(np.exp)
    df.applymap(str)


def test_types_element_wise_arithmetic() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df2 = pd.DataFrame(data={'col1': [10, 20], 'col3': [3, 4]})

    df + df2
    df.add(df2, fill_value=0)

    df - df2
    df.sub(df2, fill_value=0)

    df * df2
    df.mul(df2, fill_value=0)

    df / df2
    df.div(df2, fill_value=0)

    df // df2
    df.floordiv(df2, fill_value=0)

    df % df2
    df.mod(df2, fill_value=0)


def test_types_melt() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.melt()
    df.melt(id_vars=['col1'], value_vars=['col2'])
    df.melt(id_vars=['col1'], value_vars=['col2'], var_name="someVariable", value_name="someValue")

    pd.melt(df)
    pd.melt(df, id_vars=['col1'], value_vars=['col2'])
    pd.melt(df, id_vars=['col1'], value_vars=['col2'], var_name="someVariable", value_name="someValue")


def test_types_concat() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df2 = pd.DataFrame(data={'col1': [10, 20], 'col2': [30, 40]})

    pd.concat([df, df2])
    pd.concat([df, df2], axis=1)
    pd.concat([df, df2], keys=['first', 'second'], sort=True)
    pd.concat([df, df2], keys=['first', 'second'], names=["source", "row"])


def test_types_pivot() -> None:
    df = pd.DataFrame(data={'col1': ['first', 'second', 'third', 'fourth'],
                            'col2': [50, 70, 56, 111], 'col3': ['A', 'B', 'B', 'A'], 'col4': [100, 102, 500, 600]})
    df.pivot(index='col1', columns='col3', values='col2')
    df.pivot(index='col1', columns='col3')
    df.pivot(index='col1', columns='col3', values=['col2', 'col4'])


def test_types_groupby() -> None:
    df = pd.DataFrame(data={'col1': [1, 1, 2], 'col2': [3, 4, 5], 'col3': [0, 1, 0]})
    df.index.name = "ind"
    df.groupby(by='col1')
    df.groupby(level="ind")
    df.groupby(by='col1', sort=False, as_index=True)
    df.groupby(by=['col1', 'col2'])


# This was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_group_by_with_dropna_keyword() -> None:
    df = pd.DataFrame(data={'col1': [1, 1, 2, 1], 'col2': [2, None, 1, 2], 'col3': [3, 4, 3, 2]})
    df.groupby(by="col2", dropna=True).sum()
    df.groupby(by="col2", dropna=False).sum()
    df.groupby(by="col2").sum()


def test_types_merge() -> None:
    df = pd.DataFrame(data={'col1': [1, 1, 2], 'col2': [3, 4, 5]})
    df2 = pd.DataFrame(data={'col1': [1, 1, 2], 'col2': [0, 1, 0]})
    df.merge(df2)
    df.merge(df2, on='col1')
    df.merge(df2, on='col1', how='left')


def test_types_plot() -> None:
    df = pd.DataFrame(data={'col1': [1, 1, 2], 'col2': [3, 4, 5]})
    df.plot.hist()
    df.plot.scatter(x='col2', y='col1')


def test_types_window() -> None:
    df = pd.DataFrame(data={'col1': [1, 1, 2], 'col2': [3, 4, 5]})
    df.expanding()
    df.expanding(axis=1, center=True)

    df.rolling(2)
    df.rolling(2, axis=1, center=True)


def test_types_cov() -> None:
    df = pd.DataFrame(data={'col1': [1, 1, 2], 'col2': [3, 4, 5]})
    df.cov()
    df.cov(min_periods=1)
    # ddof param was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    df.cov(ddof=2)


def test_types_to_numpy() -> None:
    df = pd.DataFrame(data={'col1': [1, 1, 2], 'col2': [3, 4, 5]})
    df.to_numpy()
    df.to_numpy(dtype='str', copy=True)
    # na_value param was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    df.to_numpy(na_value=0)


def test_to_markdown() -> None:
    df = pd.DataFrame(data={'col1': [1, 1, 2], 'col2': [3, 4, 5]})
    df.to_markdown()
    df.to_markdown(buf=None, mode="wt")
    # index param was added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    df.to_markdown(index=False)


def test_types_to_feather() -> None:
    df = pd.DataFrame(data={'col1': [1, 1, 2], 'col2': [3, 4, 5]})
    df.to_feather("dummy_path")
    # kwargs for pyarrow.feather.write_feather added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    df.to_feather("dummy_path", compression="zstd", compression_level=3, chunksize=2)


# compare() method added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
def test_types_compare() -> None:
    df1 = pd.DataFrame(data={'col1': [1, 1, 2, 1], 'col2': [2, None, 1, 2], 'col3': [3, 4, 3, 2]})
    df2 = pd.DataFrame(data={'col1': [1, 2, 5, 6], 'col2': [3, 4, 1, 1], 'col3': [3, 4, 3, 2]})
    df1.compare(df2)
    df2.compare(df1, align_axis=0, keep_shape=True, keep_equal=True)


def test_types_agg() -> None:
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'])
    df.agg("min")
    df.agg(x=('A', max), y=('B', 'min'), z=('C', np.mean))
    df.agg("mean", axis=1)


def test_types_describe() -> None:
    df = pd.DataFrame(data={'col1': [1, 2, -4], 'col2': [np.datetime64("2000-01-01"), np.datetime64("2010-01-01"),
                                                         np.datetime64("2010-01-01")]})
    df.describe()
    df.describe(percentiles=[0.5], include='all')
    df.describe(exclude=np.number)
    # datetime_is_numeric param added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    df.describe(datetime_is_numeric=True)


def test_types_to_string() -> None:
    df = pd.DataFrame(data={'col1': [1, None, -4], 'col2': [np.datetime64("2000-01-01"), np.datetime64("2010-01-01"),
                                                            np.datetime64("2010-01-01")]})
    df.to_string(index=True, col_space=2, header=['a', 'b'], na_rep='0', justify='left', max_rows=2, min_rows=0,
                 max_cols=2, show_dimensions=True, line_width=3)
    # col_space accepting list or dict added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    df.to_string(col_space=[1, 2])
    df.to_string(col_space={'col1': 1, 'col2': 3})


def test_types_to_html() -> None:
    df = pd.DataFrame(data={'col1': [1, None, -4], 'col2': [np.datetime64("2000-01-01"), np.datetime64("2010-01-01"),
                                                            np.datetime64("2010-01-01")]})
    df.to_html(index=True, col_space=2, header=['a', 'b'], na_rep='0', justify='left', max_rows=2, max_cols=2,
               show_dimensions=True)
    # col_space accepting list or dict added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    df.to_html(col_space=[1, 2])
    df.to_html(col_space={'col1': 1, 'col2': 3})


def test_types_resample() -> None:
    df = pd.DataFrame({'values': [2, 11, 3, 13, 14, 18, 17, 19]})
    df['date'] = pd.date_range('01/01/2018', periods=8, freq='W')
    df.resample('M', on='date')
    # origin and offset params added in 1.1.0 https://pandas.pydata.org/docs/whatsnew/v1.1.0.html
    df.resample('20min', origin='epoch', offset=pd.Timedelta(2, 'minutes'), on='date')


# set_flags() method added in 1.2.0 https://pandas.pydata.org/docs/whatsnew/v1.2.0.html
def test_types_set_flags() -> None:
    pd.DataFrame([[1, 2], [8, 9]], columns=['A', 'B']).set_flags(allows_duplicate_labels=False)
    pd.DataFrame([[1, 2], [8, 9]], columns=['A', 'A']).set_flags(allows_duplicate_labels=True)
    pd.DataFrame([[1, 2], [8, 9]], columns=['A', 'A'])
