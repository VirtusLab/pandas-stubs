from datetime import timedelta
from typing import Any, Union
import numpy as np

class Timedelta(timedelta):

    def __init__(self, value: Union[Timedelta, timedelta, np.timedelta64, str, int], unit: str = ..., **kwargs: Any) -> None: ...