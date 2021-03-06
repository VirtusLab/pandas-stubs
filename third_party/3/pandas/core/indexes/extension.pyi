from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_dtype_equal as is_dtype_equal, is_object_dtype as is_object_dtype
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.indexers import deprecate_ndim_indexing as deprecate_ndim_indexing
from pandas.core.indexes.base import Index as Index
from pandas.core.ops import get_op_result_name as get_op_result_name
from pandas.util._decorators import Appender as Appender, cache_readonly as cache_readonly
from typing import Any, List, Optional

def inherit_from_data(name: str, delegate: Any, cache: bool=..., wrap: bool=...) -> Any: ...
def inherit_names(names: List[str], delegate: Any, cache: bool=..., wrap: bool=...) -> Any: ...
def make_wrapped_arith_op(opname: Any) -> Any: ...

class ExtensionIndex(Index):
    __eq__: Any = ...
    __ne__: Any = ...
    __lt__: Any = ...
    __gt__: Any = ...
    __le__: Any = ...
    __ge__: Any = ...
    def __getitem__(self, key: Any) -> Any: ...
    def __iter__(self) -> Any: ...
    def dropna(self, how: str = ...) -> Any: ...
    def repeat(self, repeats: Any, axis: Optional[Any] = ...) -> Any: ...
    def take(self, indices: Any, axis: int = ..., allow_fill: bool = ..., fill_value: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def unique(self, level: Optional[Any] = ...) -> Any: ...
    def map(self, mapper: Any, na_action: Optional[Any] = ...) -> Any: ...
    def astype(self, dtype: Any, copy: bool = ...) -> Any: ...
