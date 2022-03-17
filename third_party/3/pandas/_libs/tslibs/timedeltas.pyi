import sys
from datetime import timedelta
from typing import Union, overload

import numpy as np

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

TimeValue = Union[float, int]

TimedeltaUnitsNano = Literal["ns", "nanoseconds", "nano", "nanos", "nanosecond", "n"]
TimedeltaUnitsMicro = Literal["us","microseconds", "microsecond", "µs", "micro", "micros", "u"]
TimedeltaUnitsMillis = Literal["ms", "milliseconds", "millisecond", "milli", "millis", "l"]
TimedeltaUnitsSec = Literal["s", "seconds", "sec", "second"]
TimedeltaUnitsCalendar = Literal["W", "w", "D", "d", "days", "day"]
TimedeltaUnitsClock = Literal["hours", "hour", "hr", "h", "m", "minute", "min", "minutes", "t"]

TimedeltaUnitChoice = Literal[TimedeltaUnitsClock, TimedeltaUnitsCalendar, TimedeltaUnitsSec,
                              TimedeltaUnitsMicro, TimedeltaUnitsMillis, TimedeltaUnitsNano]

class Timedelta(timedelta):

    @overload
    def __init__(self, value: Union[Timedelta, timedelta, np.timedelta64, float, int], unit: TimedeltaUnitChoice = ...) -> None: ...
    @overload
    def __init__(self, value: str) -> None: ...
    # Wee need so many overloads to ensue that at least one keyword argument is passed e.g. pd.Timedelta() is invalid
    @overload
    def __init__(self, weeks: TimeValue, days: TimeValue = ..., hours: TimeValue = ..., minutes: TimeValue = ..., seconds: TimeValue = ..., milliseconds: TimeValue = ..., microseconds: TimeValue = ..., nanoseconds: TimeValue = ...) -> None: ...
    @overload
    def __init__(self, days: TimeValue, weeks: TimeValue = ..., hours: TimeValue = ..., minutes: TimeValue = ..., seconds: TimeValue = ..., milliseconds: TimeValue = ..., microseconds: TimeValue = ..., nanoseconds: TimeValue = ...) -> None: ...
    @overload
    def __init__(self, hours: TimeValue, days: TimeValue = ..., weeks: TimeValue = ..., minutes: TimeValue = ..., seconds: TimeValue = ..., milliseconds: TimeValue = ..., microseconds: TimeValue = ..., nanoseconds: TimeValue = ...) -> None: ...
    @overload
    def __init__(self, minutes: TimeValue, days: TimeValue = ..., hours: TimeValue = ..., weeks: TimeValue = ..., seconds: TimeValue = ..., milliseconds: TimeValue = ..., microseconds: TimeValue = ..., nanoseconds: TimeValue = ...) -> None: ...
    @overload
    def __init__(self, seconds: TimeValue, days: TimeValue = ..., hours: TimeValue = ..., minutes: TimeValue = ..., weeks: TimeValue = ..., milliseconds: TimeValue = ..., microseconds: TimeValue = ..., nanoseconds: TimeValue = ...) -> None: ...
    @overload
    def __init__(self, milliseconds: TimeValue, days: TimeValue = ..., hours: TimeValue = ..., minutes: TimeValue = ..., seconds: TimeValue = ..., weeks: TimeValue = ..., microseconds: TimeValue = ..., nanoseconds: TimeValue = ...) -> None: ...
    @overload
    def __init__(self, microseconds: TimeValue, days: TimeValue = ..., hours: TimeValue = ..., minutes: TimeValue = ..., seconds: TimeValue = ..., milliseconds: TimeValue = ..., weeks: TimeValue = ..., nanoseconds: TimeValue = ...) -> None: ...
    @overload
    def __init__(self, nanoseconds: TimeValue, days: TimeValue = ..., hours: TimeValue = ..., minutes: TimeValue = ..., seconds: TimeValue = ..., milliseconds: TimeValue = ..., microseconds: TimeValue = ..., weeks: TimeValue = ...) -> None: ...
