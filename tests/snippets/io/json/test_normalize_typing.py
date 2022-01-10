# flake8: noqa: F841
from typing import Any, Dict, List

import pandas as pd


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
