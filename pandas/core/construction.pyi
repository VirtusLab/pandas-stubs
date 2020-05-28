import numpy.ma as np
from pandas._libs.tslibs import IncompatibleFrequency as IncompatibleFrequency, OutOfBoundsDatetime as OutOfBoundsDatetime
from pandas._typing import ArrayLike as ArrayLike, Dtype as Dtype
from pandas.core.dtypes.cast import construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar, construct_1d_ndarray_preserving_na as construct_1d_ndarray_preserving_na, construct_1d_object_array_from_listlike as construct_1d_object_array_from_listlike, infer_dtype_from_scalar as infer_dtype_from_scalar, maybe_cast_to_datetime as maybe_cast_to_datetime, maybe_cast_to_integer_array as maybe_cast_to_integer_array, maybe_castable as maybe_castable, maybe_convert_platform as maybe_convert_platform, maybe_upcast as maybe_upcast

from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, ExtensionDtype as ExtensionDtype, registry as registry
from pandas.core.dtypes.generic import ABCExtensionArray as ABCExtensionArray, ABCIndexClass as ABCIndexClass, ABCPandasArray as ABCPandasArray, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna
from pandas.core.indexes.api import Index as Index
from pandas.core.series import Series as Series
from typing import Any, Optional, Sequence, Union

def array(data: Sequence[object], dtype: Optional[Union[str, np.dtype, ExtensionDtype]]=..., copy: bool=...) -> ABCExtensionArray: ...
def extract_array(obj: Any, extract_numpy: bool = ...) -> Any: ...
def sanitize_array(data: Any, index: Any, dtype: Any = ..., copy: bool=..., raise_cast_failure: bool=...) -> Any: ...
def is_empty_data(data: Any) -> bool: ...
def create_series_with_explicit_dtype(data: Any = ..., index: Optional[Union[ArrayLike, Index]]=..., dtype: Optional[Dtype]=..., name: Optional[str]=..., copy: bool=..., fastpath: bool=..., dtype_if_empty: Dtype=...) -> Series: ...
