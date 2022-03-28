# flake8: noqa: F841
from typing import List

import pandas as pd

from pandas import Index


def test_from_arrays() -> None:
    index: pd.MultiIndex = pd.MultiIndex.from_arrays([["foo", "bar"], ["car", "dog"]])


def test_from_tuples() -> None:
    index: pd.MultiIndex = pd.MultiIndex.from_tuples([("foo", "bar"), ("car", "dog")])


def test_from_product() -> None:
    index: pd.MultiIndex = pd.MultiIndex.from_product([["foo"], ["bar"]])


def test_from_frame() -> None:
    index: pd.MultiIndex = pd.MultiIndex.from_frame(pd.DataFrame([["foo", "bar"], ["foo", "bar"]]))


def test_levels() -> None:
    index = pd.MultiIndex.from_product([["foo"], ["bar"]])

    levels: List[Index] = index.levels
    level: Index = index.levels[0]