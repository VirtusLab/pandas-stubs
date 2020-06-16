from datetime import datetime
from pandas._typing import ArrayLike as ArrayLike
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCDatetimeIndex as ABCDatetimeIndex, ABCIndex as ABCIndex, ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries
from typing import Any, Optional, TypeVar, Union

ArrayConvertible = Union[list, tuple, ArrayLike, ABCSeries]
Scalar = Union[int, float, str]
DatetimeScalar = TypeVar('DatetimeScalar', Scalar, datetime)
DatetimeScalarOrArrayConvertible = Union[DatetimeScalar, list, tuple, ArrayLike, ABCSeries]

def should_cache(arg: ArrayConvertible[Any], unique_share: float=..., check_count: Optional[int]=...) -> bool: ...
def to_datetime(arg: Any, errors: str = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: Optional[Any] = ..., format: Optional[Any] = ..., exact: bool = ..., unit: Optional[Any] = ..., infer_datetime_format: bool = ..., origin: str = ..., cache: bool = ...) -> Any: ...
def to_time(arg: Any, format: Optional[Any] = ..., infer_time_format: bool = ..., errors: str = ...) -> Any: ...
