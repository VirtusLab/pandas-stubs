import tempfile
import pandas as pd
import numpy as np


def test_types_init() -> None:
    pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]}, index=[2, 1])
    pd.DataFrame(data=[1, 2, 3, 4], dtype=np.int8)
    pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'], dtype=np.int8, copy=True)


def test_types_csv() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    with tempfile.TemporaryFile() as file:
        df.to_csv()
        df.to_csv(file.name)
        df.to_csv(file)
        pd.read_csv()
        pd.read_csv(file)
        pd.read_csv(file.name)


def test_types_select() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df['col1']
    df[0]
    df[1:]


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


def test_types_dropping() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.drop('col1', axis=1)
    df.drop(columns=['col1'])
    df.drop([0, 0])


def test_types_dropna() -> None:
    df = pd.DataFrame(data={'col1': [np.nan, np.nan], 'col2': [3, np.nan]})
    df.dropna()
    df.dropna(axis=1, thresh=1)
    df.dropna(axis=0, how='all', subset=['col1'])


def test_types_fillna() -> None:
    df = pd.DataFrame(data={'col1': [np.nan, np.nan], 'col2': [3, np.nan]})
    df.fillna(0)
    df.fillna(method='pad', axis=1, inplace=False)


def test_types_sort_index() -> None:
    df = pd.DataFrame(data={'col1': [1, 2, 3, 4]}, index=[5, 1, 3, 2])
    df.sort_index()
    df.sort_index(ascending=False)
    df.sort_index(kind="mergesort")


def test_types_sort_values() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.sort_values('col1')


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


def test_types_value_counts() -> None:
    # This is really more for of a Series test
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [1, 4]})
    df['col1'].value_counts()


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
