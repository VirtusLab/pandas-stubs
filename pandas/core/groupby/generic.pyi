from collections import namedtuple
from pandas._libs import Timestamp as Timestamp, lib as lib
from pandas._typing import FrameOrSeries as FrameOrSeries
from pandas.core.base import DataError as DataError, SpecificationError as SpecificationError
from pandas.core.construction import create_series_with_explicit_dtype as create_series_with_explicit_dtype
from pandas.core.dtypes.cast import maybe_convert_objects as maybe_convert_objects, maybe_downcast_numeric as maybe_downcast_numeric, maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import ensure_int64 as ensure_int64, ensure_platform_int as ensure_platform_int, is_bool as is_bool, is_dict_like as is_dict_like, is_integer_dtype as is_integer_dtype, is_interval_dtype as is_interval_dtype, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries, NDFrame as NDFrame
from pandas.core.groupby import base as base
from pandas.core.groupby.groupby import GroupBy as GroupBy, get_groupby as get_groupby
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, all_indexes_same as all_indexes_same
from pandas.core.internals import Block as Block, BlockManager as BlockManager, make_block as make_block
from pandas.core.series import Series as Series
from pandas.plotting import boxplot_frame_groupby as boxplot_frame_groupby
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from typing import Any, Callable, FrozenSet, Optional, Type, Union

NamedAgg = namedtuple('NamedAgg', ['column', 'aggfunc'])
AggScalar = Union[str, Callable[..., Any]]
ScalarResult: Any

def generate_property(name: str, klass: Type[FrameOrSeries]) -> Any: ...
def pin_whitelisted_properties(klass: Type[FrameOrSeries], whitelist: FrozenSet[str]) -> Any: ...

class SeriesGroupBy(GroupBy):
    def apply(self, func: Any, *args: Any, **kwargs: Any) -> Any: ...
    def aggregate(self, func: Optional[Any] = ..., *args: Any, **kwargs: Any) -> Any: ...
    agg: Any = ...
    def transform(self, func: Any, *args: Any, **kwargs: Any) -> Any: ...
    def filter(self, func: Any, dropna: bool = ..., *args: Any, **kwargs: Any) -> Any: ...
    def nunique(self, dropna: bool=...) -> Series: ...
    def describe(self, **kwargs: Any) -> Any: ...
    def value_counts(self, normalize: bool = ..., sort: bool = ..., ascending: bool = ..., bins: Optional[Any] = ..., dropna: bool = ...) -> Any: ...
    def count(self) -> Series: ...  # type: ignore
    def pct_change(self, periods: int = ..., fill_method: str = ..., limit: Optional[Any] = ..., freq: Optional[Any] = ...) -> Any: ...  # type: ignore

class DataFrameGroupBy(GroupBy):
    def aggregate(self, func: Optional[Any] = ..., *args: Any, **kwargs: Any) -> Any: ...
    agg: Any = ...
    def transform(self, func: Any, *args: Any, **kwargs: Any) -> Any: ...
    def filter(self, func: Any, dropna: bool = ..., *args: Any, **kwargs: Any) -> Any: ...
    def __getitem__(self, key: Any) -> Any: ...
    def count(self) -> Any: ...
    def nunique(self, dropna: bool=...) -> Any: ...
    boxplot: Any = ...
