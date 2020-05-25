from pandas import DataFrame as DataFrame, Int64Index as Int64Index, RangeIndex as RangeIndex
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.io.common import stringify_path as stringify_path
from typing import Any

def to_feather(df: DataFrame, path: Any) -> Any: ...
def read_feather(path: Any, columns: Any = ..., use_threads: bool=...) -> Any: ...
