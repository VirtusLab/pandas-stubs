# flake8: noqa: F841
import tempfile
from typing import Any, Dict, List, Union

from pandas.io.parsers import TextFileReader

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


def test_types_concat_series() -> None:
    s = pd.Series([0, 1, -10])
    s2 = pd.Series([7, -5, 10])

    # Mypy works differently for a variable and inline expression - possible unwanted behaviour
    series_list = [s, s2]
    result_list: pd.Series = pd.concat(series_list)
    result_list_axis: pd.DataFrame = pd.concat(series_list, axis=1)
    result_list_inline: pd.Series = pd.concat([s, s2])
    result_list_inline_axis: pd.DataFrame = pd.concat([s, s2], axis=1)

    result_list_special: pd.Series = pd.concat([s, s2], keys=['first', 'second'], sort=True)
    result_list_special2: pd.Series = pd.concat([s, s2], keys=['first', 'second'], names=["source", "row"])

    # Mypy works differently for a variable and inline expression - possible unwanted behaviour
    # Return type depends on the axis
    dict_str = {'a': s, 'b': s2}
    result_dict_str: pd.Series = pd.concat(dict_str)
    result_dict_str_axis: pd.DataFrame = pd.concat(dict_str, axis=1)
    result_dict_str_inline: pd.Series = pd.concat({'a': s, 'b': s2})
    result_dict_str_inline_axis: pd.DataFrame = pd.concat({'a': s, 'b': s2}, axis=1)
    dict_int = {1: s, 2: s2}
    result_dict_int: pd.Series = pd.concat(dict_int)
    result_dict_int_axis: pd.DataFrame = pd.concat(dict_int, axis=1)
    result_dict_inline: pd.Series = pd.concat({1: s, 2: s2})
    result_dict_inline_axis: pd.DataFrame = pd.concat({1: s, 2: s2}, axis=1)
    dict_none = {1: s, None: s2}
    result_dict_none: pd.Series = pd.concat(dict_none)
    result_dict_none_axis: pd.DataFrame = pd.concat(dict_none, axis=1)
    result_dict_none_inline: pd.Series = pd.concat({1: s, None: s2})
    result_dict_none_inline_axis: pd.DataFrame = pd.concat({1: s, None: s2}, axis=1)

    result_special: pd.DataFrame = pd.concat(list(map(lambda x: s2, ["some_value", 3])), axis=1)


def test_types_frame() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    df2 = pd.DataFrame(data={'col1': [10, 20], 'col2': [30, 40]})

    # Mypy works differently for a variable and inline expression - possible unwanted behaviour
    dataframe_list = [df, df2]
    result_list: pd.DataFrame = pd.concat(dataframe_list)
    result_list_axis: pd.DataFrame = pd.concat(dataframe_list, axis=1)
    result_list_inline: pd.DataFrame = pd.concat([df, df2])
    result_list_inline_axis: pd.DataFrame = pd.concat([df, df2], axis=1)

    result_list_special: pd.DataFrame = pd.concat([df, df2], keys=['first', 'second'], sort=True)
    result_list_special2: pd.DataFrame = pd.concat([df, df2], keys=['first', 'second'], names=["source", "row"])

    dict_str = {'a': df, 'b': df2}
    result_dict_str: pd.DataFrame = pd.concat(dict_str)
    result_dict_str_axis: pd.DataFrame = pd.concat(dict_str, axis=1)
    result_dict_str_inline: pd.DataFrame = pd.concat({'a': df, 'b': df2})
    result_dict_str_inline_axis: pd.DataFrame = pd.concat({'a': df, 'b': df2}, axis=1)
    dict_int = {1: df, 2: df2}
    result_dict_int: pd.DataFrame = pd.concat(dict_int)
    result_dict_int_axis: pd.DataFrame = pd.concat(dict_int, axis=1)
    result_dict_inline: pd.DataFrame = pd.concat({1: df, 2: df2})
    result_dict_inline_axis: pd.DataFrame = pd.concat({1: df, 2: df2}, axis=1)
    dict_none = {1: df, None: df2}
    result_dict_none: pd.DataFrame = pd.concat(dict_none)
    result_dict_none_axis: pd.DataFrame = pd.concat(dict_none, axis=1)
    result_dict_none_inline: pd.DataFrame = pd.concat({1: df, None: df2})
    result_dict_none_inline_axis: pd.DataFrame = pd.concat({1: df, None: df2}, axis=1)


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


def test_types_read_csv() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    csv_df: str = df.to_csv()

    with tempfile.NamedTemporaryFile() as file:
        df.to_csv(file.name)
        df2: pd.DataFrame = pd.read_csv(file.name)
        df3: pd.DataFrame = pd.read_csv(file.name, sep="a", squeeze=False)
        df4: pd.DataFrame = pd.read_csv(file.name, header=None, prefix="b", mangle_dupe_cols=True, keep_default_na=False)
        df5: pd.DataFrame = pd.read_csv(file.name, engine='python', true_values=[0, 1, 3], na_filter=False)
        df6: pd.DataFrame = pd.read_csv(file.name, skiprows=lambda x: x in [0, 2], skip_blank_lines=True, dayfirst=False)
        df7: pd.DataFrame = pd.read_csv(file.name, nrows=2)
        df8: pd.DataFrame = pd.read_csv(file.name, names=['col1', 'col2'])
        df9: pd.DataFrame = pd.read_csv(file.name, names=('col1', 'col2'))
        tfr1: TextFileReader = pd.read_csv(file.name, nrows=2, iterator=True, chunksize=3)
        tfr2: TextFileReader = pd.read_csv(file.name, nrows=2, chunksize=1)
        tfr3: TextFileReader = pd.read_csv(file.name, nrows=2, iterator=False, chunksize=1)
        tfr4: TextFileReader = pd.read_csv(file.name, nrows=2, iterator=True)
