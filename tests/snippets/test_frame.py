import tempfile
import pandas as pd
import numpy as np


def test_types_init() -> None:
    pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
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


def test_types_loc() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.loc[[0], 'col1']


def test_types_boolean_indexing() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df[df > 1]
    df[~(df > 1.0)]


def test_types_setting() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df['col1'] = 1


def test_types_dropping() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df.drop('col1', axis=1)
    df.drop(columns=['col1'])
    df.drop([0, 0])


def test_types_sort_index() -> None:
    df = pd.DataFrame(data={'col1': [1, 2, 3, 4]}, index=[5, 1, 3, 2])
    df.sort_index()
    df.sort_index(ascending=False)
    df.sort_index(kind="mergesort")


def test_types_sort_values() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.sort_values('col1')


def test_types_rank() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.rank(method="average", pct=True)


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


def test_types_idxmin() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.idxmin()
    df.idxmin(axis=0)


def test_types_idxmax() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.idxmax()
    df.idxmax(axis=0)


def test_types_apply() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.apply(lambda x: x**2)
    df.apply(np.exp)
    df.apply(str)


def test_types_applymap() -> None:
    df = pd.DataFrame(data={'col1': [2, 1], 'col2': [3, 4]})
    df.applymap(lambda x: x**2)
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