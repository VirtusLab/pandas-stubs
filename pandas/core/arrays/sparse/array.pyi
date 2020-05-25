import numpy as np
from pandas._libs import lib as lib
from pandas._libs.sparse import BlockIndex as BlockIndex, IntIndex as IntIndex, SparseIndex as SparseIndex
from pandas._libs.tslibs import NaT as NaT
from pandas.core.arrays import ExtensionArray as ExtensionArray, ExtensionOpsMixin as ExtensionOpsMixin
from pandas.core.arrays.sparse.dtype import SparseDtype as SparseDtype
from pandas.core.base import PandasObject as PandasObject
from pandas.core.construction import sanitize_array as sanitize_array
from pandas.core.dtypes.cast import astype_nansafe as astype_nansafe, construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar, find_common_type as find_common_type, infer_dtype_from_scalar as infer_dtype_from_scalar

from pandas.core.dtypes.generic import ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries, ABCSparseArray as ABCSparseArray
from pandas.core.dtypes.missing import isna as isna, na_value_for_dtype as na_value_for_dtype, notna as notna
from pandas.core.indexers import check_array_indexer as check_array_indexer
from pandas.core.missing import interpolate_2d as interpolate_2d
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.errors import PerformanceWarning as PerformanceWarning
from typing import Any, Optional

class SparseArray(PandasObject, ExtensionArray, ExtensionOpsMixin):
    def __init__(self, data: Any, sparse_index: Optional[Any] = ..., index: Optional[Any] = ..., fill_value: Optional[Any] = ..., kind: str = ..., dtype: Optional[Any] = ..., copy: bool = ...) -> None: ...
    @classmethod
    def from_spmatrix(cls, data: Any) -> Any: ...
    def __array__(self, dtype: Any = ..., copy: Any = ...) -> np.ndarray: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    @property
    def sp_index(self) -> Any: ...
    @property
    def sp_values(self) -> Any: ...
    @property
    def dtype(self) -> Any: ...
    @property
    def fill_value(self) -> Any: ...
    @fill_value.setter
    def fill_value(self, value: Any) -> None: ...
    @property
    def kind(self) -> str: ...
    def __len__(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    @property
    def density(self) -> Any: ...
    @property
    def npoints(self) -> int: ...
    def isna(self) -> Any: ...
    def fillna(self, value: Optional[Any] = ..., method: Optional[Any] = ..., limit: Optional[Any] = ...) -> Any: ...
    def shift(self, periods: int = ..., fill_value: Optional[Any] = ...) -> Any: ...
    def unique(self) -> Any: ...
    def factorize(self, na_sentinel: int = ...) -> Any: ...
    def value_counts(self, dropna: bool = ...) -> Any: ...
    def __getitem__(self, key: Any) -> Any: ...
    def take(self, indices: Any, allow_fill: bool = ..., fill_value: Optional[Any] = ...) -> Any: ...
    def searchsorted(self, v: Any, side: str = ..., sorter: Optional[Any] = ...) -> Any: ...
    def copy(self) -> Any: ...
    def astype(self, dtype: Optional[Any] = ..., copy: bool = ...) -> Any: ...
    def map(self, mapper: Any) -> Any: ...
    def to_dense(self) -> Any: ...
    def nonzero(self) -> Any: ...
    def all(self, axis: Optional[Any] = ..., *args: Any, **kwargs: Any) -> Any: ...
    def any(self, axis: int = ..., *args: Any, **kwargs: Any) -> Any: ...
    def sum(self, axis: int = ..., *args: Any, **kwargs: Any) -> Any: ...
    def cumsum(self, axis: int = ..., *args: Any, **kwargs: Any) -> Any: ...
    def mean(self, axis: int = ..., *args: Any, **kwargs: Any) -> Any: ...
    def transpose(self, *axes: Any) -> Any: ...
    @property
    def T(self) -> Any: ...
    def __array_ufunc__(self, ufunc: Any, method: Any, *inputs: Any, **kwargs: Any) -> Any: ...
    def __abs__(self) -> Any: ...

def make_sparse(arr: Any, kind: str = ..., fill_value: Optional[Any] = ..., dtype: Optional[Any] = ..., copy: bool = ...) -> Any: ...
