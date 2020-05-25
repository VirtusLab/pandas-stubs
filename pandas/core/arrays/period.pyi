# Removed some imports that were necessary only for implementation
import numpy as np
from pandas._libs.tslibs import NaT as NaT, NaTType as NaTType, iNaT as iNaT
from pandas._libs.tslibs.period import DIFFERENT_FREQ as DIFFERENT_FREQ, IncompatibleFrequency as IncompatibleFrequency, Period as Period
from pandas._libs.tslibs.timedeltas import Timedelta as Timedelta
from pandas.core.arrays import datetimelike as dtl
from pandas.core.dtypes.dtypes import PeriodDtype as PeriodDtype
from pandas.core.dtypes.generic import ABCIndexClass as ABCIndexClass, ABCPeriodArray as ABCPeriodArray, ABCPeriodIndex as ABCPeriodIndex, ABCSeries as ABCSeries
from pandas.tseries import frequencies as frequencies
from pandas.tseries.offsets import DateOffset as DateOffset, Tick as Tick
from typing import Any, Optional, Sequence, Union

class PeriodArray(dtl.DatetimeLikeArrayMixin, dtl.DatelikeOps):
    __array_priority__: int = ...
    def __init__(self, values: Any, freq: Optional[Any] = ..., dtype: Optional[Any] = ..., copy: bool = ...) -> None: ...
    def dtype(self) -> Any: ...
    @property  # type: ignore
    def freq(self) -> Any: ...
    def __array__(self, dtype: Any = ...) -> np.ndarray: ...
    def __arrow_array__(self, type: Optional[Any] = ...) -> Any: ...
    year: Any = ...
    month: Any = ...
    day: Any = ...
    hour: Any = ...
    minute: Any = ...
    second: Any = ...
    weekofyear: Any = ...
    week: Any = ...
    dayofweek: Any = ...
    weekday: Any = ...
    dayofyear: Any = ...
    day_of_year: Any = ...
    quarter: Any = ...
    qyear: Any = ...
    days_in_month: Any = ...
    daysinmonth: Any = ...
    @property
    def is_leap_year(self) -> Any: ...
    @property
    def start_time(self) -> Any: ...
    @property
    def end_time(self) -> Any: ...
    def to_timestamp(self, freq: Optional[Any] = ..., how: str = ...) -> Any: ...
    def asfreq(self, freq: Optional[Any] = ..., how: str = ...) -> Any: ...
    def astype(self, dtype: Any, copy: bool = ...) -> Any: ...

def raise_on_incompatible(left: Any, right: Any) -> Any: ...
def period_array(data: Sequence[Optional[Period]], freq: Optional[Union[str, Tick]]=..., copy: bool=...) -> PeriodArray: ...
def validate_dtype_freq(dtype: Any, freq: Any) -> Any: ...
def dt64arr_to_periodarr(data: Any, freq: Any, tz: Optional[Any] = ...) -> Any: ...
