import numpy as np
from pandas.core.construction import array as array

from pandas.core.dtypes.generic import ABCExtensionArray as ABCExtensionArray, ABCSeries as ABCSeries
from typing import Any, Union

def should_extension_dispatch(left: ABCSeries, right: Any) -> bool: ...
def should_series_dispatch(left: Any, right: Any, op: Any) -> Any: ...
def dispatch_to_extension_op(op: Any, left: Union[ABCExtensionArray, np.ndarray], right: Any) -> Any: ...
