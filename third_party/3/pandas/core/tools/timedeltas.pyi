import sys
from datetime import timedelta

from pandas._libs.tslibs.timedeltas import Timedelta as Timedelta, TimedeltaUnitChoice
from pandas.core.dtypes.generic import ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries
from typing import overload, List, Union

from pandas.core.indexes.timedeltas import TimedeltaIndex
from pandas.core.series import Series

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

ErrorOption = Literal["ignore", "raise", "coerce"]

@overload
def to_timedelta(arg: timedelta, errors: ErrorOption = ...) -> Timedelta: ...
@overload
def to_timedelta(arg: Union[float, int], unit: TimedeltaUnitChoice = ..., errors: ErrorOption = ...) -> Timedelta: ...
@overload
def to_timedelta(arg: List[Union[float, int]], unit: TimedeltaUnitChoice = ..., errors: ErrorOption = ...) -> TimedeltaIndex: ...
@overload
def to_timedelta(arg: str, errors: ErrorOption = ...) -> Timedelta: ...
@overload
def to_timedelta(arg: List[Union[str]], errors: ErrorOption = ...) -> TimedeltaIndex: ...
@overload
def to_timedelta(arg: Series, unit: TimedeltaUnitChoice = ..., errors: ErrorOption = ...) -> Series: ...
