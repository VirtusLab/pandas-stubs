from pandas import get_option as get_option, option_context as option_context
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame
from typing import Any, Optional

def read_clipboard(sep: str = ..., **kwargs: Any) -> Any: ...
def to_clipboard(obj: Any, excel: bool = ..., sep: Optional[Any] = ..., **kwargs: Any) -> None: ...
