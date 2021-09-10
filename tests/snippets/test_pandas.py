# flake8: noqa: F841
from typing import Any, Dict, List, Union

import pandas as pd


def test_types_to_datetime() -> None:
    df = pd.DataFrame({'year': [2015, 2016],
                       'month': [2, 3],
                       'day': [4, 5]})
    pd.to_datetime(df)
    pd.to_datetime(df, unit="s", origin="unix", infer_datetime_format=True)
    pd.to_datetime(df, unit="ns", dayfirst=True, utc=None, format="%M:%D", exact=False)
    pd.to_datetime([1, 2], unit="D", origin=pd.Timestamp("01/01/2000"))
    pd.to_datetime([1, 2], unit="D", origin=3)


def test_types_concat() -> None:
    s = pd.Series([0, 1, -10])
    s2 = pd.Series([7, -5, 10])

    pd.concat([s, s2])
    pd.concat([s, s2], axis=1)
    pd.concat([s, s2], keys=['first', 'second'], sort=True)
    pd.concat([s, s2], keys=['first', 'second'], names=["source", "row"])

    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df2 = pd.DataFrame(data={'col1': [10, 20], 'col2': [30, 40]})

    pd.concat([df, df2])
    pd.concat([df, df2], axis=1)
    pd.concat([df, df2], keys=['first', 'second'], sort=True)
    pd.concat([df, df2], keys=['first', 'second'], names=["source", "row"])

    result: pd.DataFrame = pd.concat({"a": pd.DataFrame([1, 2, 3]), "b": pd.DataFrame([4, 5, 6])}, axis=1)
    result2: Union[pd.DataFrame, pd.Series] = pd.concat({"a": pd.Series([1, 2, 3]), "b": pd.Series([4, 5, 6])}, axis=1)


def test_types_json_normalize() -> None:
    data1: List[Dict[str, Any]] = [{'id': 1, 'name': {'first': 'Coleen', 'last': 'Volk'}},
                                  {'name': {'given': 'Mose', 'family': 'Regner'}},
                                  {'id': 2, 'name': 'Faye Raker'}]
    df1: pd.DataFrame = pd.json_normalize(data=data1)
    df2: pd.DataFrame = pd.json_normalize(data=data1, max_level=0, sep=";")
    df3: pd.DataFrame = pd.json_normalize(data=data1, meta_prefix="id", record_prefix="name", errors='raise')
    df4: pd.DataFrame = pd.json_normalize(data=data1, record_path=None, meta='id')
    data2: Dict[str, Any] = {'name': {'given': 'Mose', 'family': 'Regner'}}
    df5: pd.DataFrame = pd.json_normalize(data=data2)
