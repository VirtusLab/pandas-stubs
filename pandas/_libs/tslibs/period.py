from typing import Any

import numpy

DIFFERENT_FREQ: str


class IncompatibleFrequency(ValueError):
    ...


class Period:
    ...


def get_period_field_arr(code: int, arr: Any, freq: int) -> Any: ...


def period_asfreq_arr(arr: numpy.ndarray, freq1: int, freq2: int, end: Any) -> Any: ...
