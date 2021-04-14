from __future__ import annotations

import sys

import numpy as np

from pandas import datetime
from pandas._typing import Axes, Axis, Dtype as Dtype, FilePathOrBuffer, Level, Renamer, Column, Label, FrameOrSeries, \
    ArrayLike, AnyArrayLike, GoogleCredentials, Scalar, ReplaceMethod, ToReplace, ReplaceValue, Frequency, AxisOption, \
    Orientation, Function, AggregationFunction, GroupByObject, GeneralDuplicatesKeepStrategy, InterpolationMethod, \
    CorrelationMethod, SortKind, JoinType, FillMethod, ErrorsStrategy, NaSortPosition, FillValue, TimestampMethod, \
    ValueKeyFunc, IndexKeyFunc
from pandas.core.accessor import CachedAccessor
from pandas.core.base import PandasObject
from pandas.core.generic import NDFrame
from pandas.core.groupby import generic as groupby_generic
from pandas.core.groupby.grouper import Grouper
from pandas.core.indexes.api import Index
from pandas.core.series import Series
from pandas.io.formats import format as fmt
from pandas.io.formats.format import formatters_type, VALID_JUSTIFY_PARAMETERS, FloatFormatType
from pandas.io.formats.style import Styler
from typing import Any, Hashable, IO, Iterable, List, Optional, Sequence, Tuple, Union, Dict, Mapping, Type, \
    overload, Iterator, Callable, AnyStr

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

ExportOrientation = Literal['dict', 'list', 'series', 'split', 'records', 'index']
CompressionType = Literal['snappy', 'gzip', 'brotli']
IfExistStrategy = Literal['fail', 'replace', 'append']
ParquetEngine = Literal['auto', 'pyarrow', 'fastparquet']
DropTypes = Literal['any', 'all']
KeepStrategy = Literal['first', 'last', 'all']
UpdateJoinType = Literal['left']
UpdateErrorsStrategy = Literal['raise', 'ignore']
ApplyResultType = Literal['expand', 'reduce', 'broadcast']
MergeType = JoinType
MergeValidationMethod = Literal["one_to_one", "1:1", "one_to_many", "1:m", "many_to_one", "m:1", "many_to_many", "m:m"]

IndexArray = Union[Series, Index, np.ndarray, Iterator]
CoercibleIntoDataFrame = Union[Dict[str, Scalar], Dict[str, Series], Dict[str, Tuple[Scalar, ...]], Dict[str, Iterable[Scalar]]]

ColumnWidth = Union[str, int]
ColumnSpace = Union[ColumnWidth, Sequence[ColumnWidth], Dict[Column, ColumnWidth]]

TransformFunction = AggregationFunction

class DataFrame(NDFrame):
    plot: CachedAccessor = ...
    hist: Callable[..., Any] = ...
    boxplot: Callable[..., Any] = ...
    sparse: CachedAccessor = ...
    def __init__(self, data: Any = ..., index: Optional[Axes[Any]] = ..., columns: Optional[Axes[Any]] = ..., dtype: Optional[Dtype] = ..., copy: bool = ...) -> None: ...
    def __len__(self) -> int: ...
    def __le__(self, other: Scalar) -> DataFrame: ...
    def __lt__(self, other: Scalar) -> DataFrame: ...
    def __ge__(self, other: Scalar) -> DataFrame: ...
    def __gt__(self, other: Scalar) -> DataFrame: ...
    def __mul__(self, other: Scalar) -> DataFrame: ...
    def __truediv__(self, other: Union[Scalar, DataFrame]) -> DataFrame: ...
    def __floordiv__(self, other: Union[Scalar, DataFrame]) -> DataFrame: ...
    def __mod__(self, other: Union[Scalar, DataFrame]) -> DataFrame: ...
    def __and__(self, other: DataFrame) -> DataFrame: ...
    def __or__(self, other: DataFrame) -> DataFrame: ...
    def __add__(self, other: Union[Scalar, DataFrame]) -> DataFrame: ...
    def __sub__(self, other: Union[Scalar, DataFrame]) -> DataFrame: ...
    def __matmul__(self, other: Union[FrameOrSeries, ArrayLike]) -> FrameOrSeries: ...
    def __rmatmul__(self, other: Union[FrameOrSeries, ArrayLike]) -> FrameOrSeries: ...
    # Type ignoring the first declaration because for some reason mypy thinks that np.ndarray overlaps Column
    @overload
    def __getitem__(self, key: Column) -> Series: ...  # type: ignore
    @overload
    def __getitem__(self, key: Union[Series, Index, DataFrame, List[Column], slice, np.ndarray]) -> DataFrame: ...
    @overload
    def __setitem__(self, key: Column, value: Any) -> DataFrame: ...
    @overload
    def __setitem__(self, key: Union[Series, Index, DataFrame, List[Column], slice, np.ndarray], value: Any) -> DataFrame: ...
    @property
    def axes(self) -> List[Index]: ...
    @property
    def shape(self) -> Tuple[int, int]: ...
    def to_string(self, buf: Optional[FilePathOrBuffer[str]] = ..., columns: Optional[Sequence[str]] = ..., col_space: Optional[Union[int, Sequence[int], Dict[str, int]]] = ..., header: Union[bool, Sequence[str]] = ..., index: bool = ..., na_rep: str = ..., formatters: Optional[fmt.formatters_type] = ..., float_format: Optional[fmt.float_format_type] = ..., sparsify: Optional[bool] = ..., index_names: bool = ..., justify: Optional[str] = ..., max_rows: Optional[int] = ..., min_rows: Optional[int] = ..., max_cols: Optional[int] = ..., show_dimensions: bool = ..., decimal: str = ..., line_width: Optional[int] = ..., max_colwidth: Optional[int] = ..., encoding: Optional[str] = ...) -> Optional[str]: ...
    @property
    def style(self) -> Styler: ...
    def items(self) -> Iterable[Tuple[Label, Series]]: ...
    def iteritems(self) -> Iterable[Tuple[Label, Series]]: ...
    def iterrows(self) -> Iterable[Tuple[Label, Series]]: ...
    # This isn't exact, first argument could(!) be an Index, the rest column values
    def itertuples(self, index: bool = ..., name: str = ...) -> Iterable[Tuple[Any, ...]]: ...
    def dot(self, other: Union[FrameOrSeries, ArrayLike]) -> FrameOrSeries: ...
    @classmethod
    def from_dict(cls: Any, data: Dict[str, Union[AnyArrayLike, Series, Dict[Column, Dtype]]], orient: Orientation = ..., dtype: Optional[Dtype] = ..., columns: Optional[Sequence[str]] = ...) -> DataFrame: ...
    def to_numpy(self, dtype: Union[str, np.dtype] = ..., copy: bool = ..., na_value: Optional[Any] = ...) -> np.ndarray: ...
    def to_dict(self, orient: ExportOrientation = ..., into: Type[Mapping[Column, Any]] = ...) -> Union[Mapping[Column, Any], List[Any]]: ...
    def to_gbq(self, destination_table: str, project_id: Optional[str] = ..., chunksize: Optional[int] = ..., reauth: bool = ..., if_exists: IfExistStrategy = ..., auth_local_webserver: bool = ..., table_schema: Optional[List[Dict[str, Any]]] = ..., location: Optional[str] = ..., progress_bar: bool = ..., credentials: Optional[GoogleCredentials] = ...) -> None: ...
    @classmethod
    def from_records(cls: Any, data: Union[np.ndarray, List[Tuple[Any, ...]], Dict[Any, Any], DataFrame], index: Union[Sequence[str], ArrayLike] = ..., exclude: Sequence[Column] = ..., columns: Sequence[Column] = ..., coerce_float: bool = ..., nrows: Optional[int] = ...) -> DataFrame: ...
    def to_records(self, index: bool = ..., column_dtypes: Optional[Union[str, type, Dict[Column, Dtype]]] = ..., index_dtypes: Optional[Union[str, type, Dict[Column, Dtype]]] = ...) -> np.recarray: ...
    def to_stata(self, path: FilePathOrBuffer[AnyStr], convert_dates: Optional[Dict[Label, str]] = ..., write_index: bool = ..., byteorder: Optional[str] = ..., time_stamp: Optional[datetime.datetime] = ..., data_label: Optional[str] = ..., variable_labels: Optional[Dict[Label, str]] = ..., version: int = ..., convert_strl: Optional[Sequence[Label]] = ...) -> None: ...
    def to_feather(self, path: str, **kwargs: Any) -> None: ...
    def to_markdown(self, buf: Optional[IO[str]] = ..., mode: Optional[str] = ..., index: bool = ..., **kwargs: Any) -> Optional[str]: ...
    def to_parquet(self, path: str, engine: ParquetEngine = ..., compression: Optional[CompressionType] = ..., index: Optional[bool] = ..., partition_cols: Optional[List[Column]] = ..., **kwargs: Any) -> None: ...
    def to_html(self, buf: Optional[Any] = ..., columns: Optional[Sequence[str]] = ..., col_space: ColumnSpace = ..., header: Union[bool, Sequence[str]] = ..., index: bool = ..., na_rep: str = ..., formatters: Optional[formatters_type] = ..., float_format: Optional[FloatFormatType] = ..., sparsify: Optional[bool] = ..., index_names: bool = ..., justify: Optional[VALID_JUSTIFY_PARAMETERS] = ..., max_rows: Optional[int] = ..., max_cols: Optional[int] = ..., show_dimensions: Union[bool, str] = ..., decimal: str = ..., bold_rows: bool = ..., classes: Optional[Sequence[str]] = ..., escape: bool = ..., notebook: bool = ..., border: Optional[int] = ..., table_id: Optional[str] = ..., render_links: bool = ..., encoding: Optional[str] = ...) -> str: ...
    def info(self, verbose: Optional[bool] = ..., buf: Optional[IO[str]] = ..., max_cols: Optional[int] = ..., memory_usage: Optional[Union[bool, str]] = ..., null_counts: Optional[bool] = ...) -> None: ...
    def memory_usage(self, index: Optional[bool] = ..., deep: Optional[bool] = ...) -> Series: ...
    def transpose(self, *args: Any, copy: bool = ...) -> DataFrame: ...
    @property
    def T(self) -> DataFrame: ...
    @overload
    def query(self, expr: str, inplace: Literal[False] = ..., **kwargs: Any) -> DataFrame: ...
    @overload
    def query(self, expr: str, inplace: Literal[True], **kwargs: Any) -> None: ...
    @overload
    def eval(self, expr: str, inplace: Literal[False] = ..., **kwargs: Any) -> Union[np.ndarray, int, float, PandasObject]: ...
    @overload
    def eval(self, expr: str, inplace: Literal[True], **kwargs: Any) -> None: ...
    def select_dtypes(self, include: Optional[Sequence[Union[str, Dtype]]] = ..., exclude: Optional[Sequence[Union[str, Dtype]]] = ...) -> DataFrame: ...
    def insert(self, loc: int, column: Union[Column, Hashable], value: Union[int, Series, ArrayLike], allow_duplicates: Optional[bool] = ...) -> None: ...
    def assign(self, **kwargs: Any) -> DataFrame: ...
    def lookup(self, row_labels: Sequence[Any], col_labels: Sequence[Column]) -> np.ndarray: ...
    def align(self, other: FrameOrSeries, join: JoinType = ..., axis: AxisOption = ..., level: Level = ..., copy: bool = ..., fill_value: Scalar = ..., method: Optional[FillMethod] = ..., limit: Optional[int] = ..., fill_axis: AxisOption = ..., broadcast_axis: AxisOption = ...) -> DataFrame: ...
    def reindex(self, *args: Any, **kwargs: Any) -> DataFrame: ...
    @overload
    def drop(self, labels: Optional[Sequence[Label]] = ..., axis: AxisOption = ..., index: Optional[Sequence[Label]] = ..., columns: Optional[Sequence[Label]] = ..., level: Optional[Level] = ..., errors: ErrorsStrategy = ..., *, inplace: Literal[False] = ...) -> DataFrame: ...
    @overload
    def drop(self, labels: Optional[Sequence[Label]] = ..., axis: AxisOption = ..., index: Optional[Sequence[Label]] = ..., columns: Optional[Sequence[Label]] = ..., level: Optional[Level] = ..., errors: ErrorsStrategy = ..., *, inplace: Literal[True]) -> None: ...
    @overload
    def rename(self, mapper: Optional[Renamer] = ..., *, index: Optional[Renamer] = ..., columns: Optional[Renamer] = ..., axis: Optional[Axis] = ..., copy: bool = ..., inplace: Literal[False] = ..., level: Optional[Level] = ..., errors: ErrorsStrategy = ...) -> DataFrame: ...
    @overload
    def rename(self, mapper: Optional[Renamer] = ..., *, index: Optional[Renamer] = ..., columns: Optional[Renamer] = ..., axis: Optional[Axis] = ..., copy: bool = ..., inplace: Literal[True], level: Optional[Level] = ..., errors: ErrorsStrategy = ...) -> None: ...
    @overload
    def fillna(self, value: FillValue = ..., method: Optional[FillMethod] = ..., axis: Optional[Axis] = ...,  limit: int = ..., downcast: Optional[Dict[Any, Dtype]] = ..., *, inplace: Literal[False] = ...) -> DataFrame: ...
    @overload
    def fillna(self, value: FillValue = ..., method: Optional[FillMethod] = ..., axis: Optional[Axis] = ..., limit: int = ..., downcast: Optional[Dict[Any, Dtype]] = ..., *, inplace: Literal[True]) -> None: ...
    @overload
    def replace(self, to_replace: Optional[ToReplace] = ..., value: Optional[ReplaceValue] = ..., limit: Optional[int] = ..., regex: bool = ..., method: ReplaceMethod = ..., *, inplace: Literal[False] = ...) -> DataFrame: ...
    @overload
    def replace(self, to_replace: Optional[ToReplace] = ..., value: Optional[ReplaceValue] = ..., limit: Optional[int] = ..., regex: bool = ..., method: ReplaceMethod = ..., *,  inplace: Literal[True]) -> None: ...
    def shift(self, periods: int = ..., freq: Optional[Frequency] = ..., axis: AxisOption = ..., fill_value: Scalar = ...) -> DataFrame: ...
    @overload
    def set_index(self, keys: Union[Label, IndexArray, List[Union[Label, IndexArray]]], drop: bool = ..., append: bool = ..., verify_integrity: bool = ..., *, inplace: Literal[False] = ...) -> DataFrame: ...
    @overload
    def set_index(self, keys: Union[Label, IndexArray, List[Union[Label, IndexArray]]], drop: bool = ..., append: bool = ..., verify_integrity: bool = ..., *, inplace: Literal[True]) -> None: ...
    @overload
    def reset_index(self, level: Optional[Union[Hashable, Sequence[Hashable]]] = ..., drop: bool = ..., col_level: Hashable = ..., col_fill: Optional[Hashable] = ..., *, inplace: Literal[False] = ...) -> DataFrame: ...
    @overload
    def reset_index(self, level: Optional[Union[Hashable, Sequence[Hashable]]] = ..., drop: bool = ..., col_level: Hashable = ..., col_fill: Optional[Hashable] = ..., *, inplace: Literal[True]) -> None: ...
    def isna(self) -> DataFrame: ...
    def isnull(self) -> DataFrame: ...
    def notna(self) -> DataFrame: ...
    def notnull(self) -> DataFrame: ...
    @overload
    def dropna(self, axis: AxisOption = ..., how: DropTypes = ..., thresh: Optional[int] = ..., subset: Optional[Any] = ..., inplace: Literal[False] = ...) -> DataFrame: ...
    @overload
    def dropna(self, axis: AxisOption = ..., how: DropTypes = ..., thresh: Optional[int] = ..., subset: Optional[Any] = ..., *, inplace: Literal[True]) -> None: ...
    @overload
    def drop_duplicates(self, subset: Optional[Union[Hashable, Sequence[Hashable]]] = ..., keep: GeneralDuplicatesKeepStrategy = ..., inplace: Literal[False] = ..., ignore_index: bool = ...) -> DataFrame: ...
    @overload
    def drop_duplicates(self, subset: Optional[Union[Hashable, Sequence[Hashable]]] = ..., keep: GeneralDuplicatesKeepStrategy = ..., ignore_index: bool = ..., *, inplace: Literal[True]) -> None: ...
    def duplicated(self, subset: Optional[Union[Hashable, Sequence[Hashable]]] = ..., keep: Union[str, bool] = ...) -> Series: ...
    @overload    # type: ignore[override]
    def sort_values(self, by: Union[str, List[str]], axis: AxisOption = ..., ascending: bool = ..., kind: SortKind = ..., na_position: NaSortPosition = ..., ignore_index: bool = ...,  key: ValueKeyFunc = ..., *, inplace: Literal[False] = ...) -> DataFrame: ...
    @overload
    def sort_values(self, by: Union[str, List[str]], axis: AxisOption = ..., ascending: bool = ..., kind: SortKind = ..., na_position: NaSortPosition = ..., ignore_index: bool = ...,  key: ValueKeyFunc = ..., *, inplace: Literal[True]) -> None: ...
    @overload
    def sort_index(self, axis: AxisOption = ..., level: Optional[Union[Level, List[Level]]] = ..., ascending: bool = ..., kind: SortKind = ..., na_position: NaSortPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ...,  key: IndexKeyFunc = ..., *, inplace: Literal[False] = ...) -> DataFrame: ...
    @overload
    def sort_index(self, axis: AxisOption = ..., level: Optional[Union[Level, List[Level]]] = ..., ascending: bool = ..., kind: SortKind = ..., na_position: NaSortPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ...,  key: IndexKeyFunc = ..., *, inplace: Literal[True]) -> None: ...
    def nlargest(self, n: int, columns: Union[Label, List[Label]], keep: KeepStrategy = ...) -> DataFrame: ...
    def nsmallest(self, n: int, columns: Union[Label, List[Label]], keep: KeepStrategy = ...) -> DataFrame: ...
    def swaplevel(self, i: Level = ..., j: Level = ..., axis: AxisOption = ...) -> DataFrame: ...
    def reorder_levels(self, order: Union[List[int], List[str]], axis: AxisOption = ...) -> DataFrame: ...
    def combine(self, other: DataFrame, func: Union[np.func, Callable[[Series, Series], Union[Series, Scalar]]], fill_value: Optional[Scalar] = ..., overwrite: bool = ...) -> DataFrame: ...
    def combine_first(self, other: DataFrame) -> DataFrame: ...
    def update(self, other: Union[DataFrame, CoercibleIntoDataFrame], join: UpdateJoinType = ..., overwrite: bool = ..., filter_func: Optional[Callable[..., bool]] = ..., errors: UpdateErrorsStrategy = ...) -> None: ...
    def groupby(self, by: Optional[GroupByObject] = ..., axis: AxisOption = ..., level: Optional[Sequence[Level]] = ..., as_index: bool = ..., sort: bool = ..., group_keys: bool = ..., squeeze: bool = ..., observed: bool = ..., dropna: bool = ...) -> groupby_generic.DataFrameGroupBy: ...
    def pivot(self, index: Optional[Union[Label, Sequence[Label]]] = ..., columns: Optional[Union[Label, Sequence[Label]]] = ..., values: Optional[Union[Label, Sequence[Label]]] = ...) -> DataFrame: ...
    def pivot_table(self, values: Optional[Sequence[Column]] = ..., index: Optional[Union[Column, Grouper, np.ndarray, List[Union[Column, Grouper, np.ndarray]]]] = ..., columns: Optional[Union[Column, Grouper, np.ndarray, List[Union[Column, Grouper, np.ndarray]]]] = ..., aggfunc: AggregationFunction = ..., fill_value: Scalar = ..., margins: bool = ..., dropna: bool = ..., margins_name: str = ..., observed: bool = ...) -> DataFrame: ...
    def stack(self, level: Union[Level, List[Level]] = ..., dropna: bool = ...) -> FrameOrSeries: ...
    def explode(self, column: Union[Column, Tuple[Column, ...]]) -> DataFrame: ...
    def unstack(self, level: Union[Level, List[Level]] = ..., fill_value: Optional[Scalar] = ...) -> FrameOrSeries: ...
    def melt(self, id_vars: Optional[Union[Tuple[Column], List[Column], np.ndarray]] = ..., value_vars: Optional[Union[Sequence[Column], np.ndarray]] = ..., var_name: Optional[Scalar] = ..., value_name: Scalar = ..., col_level: Optional[Level] = ...) -> DataFrame: ...
    def diff(self, periods: int = ..., axis: AxisOption = ...) -> DataFrame: ...
    def aggregate(self, func: AggregationFunction = ..., axis: AxisOption = ..., *args: Any, **kwargs: Any) -> Union[Scalar, FrameOrSeries]: ...
    def agg(self, func: AggregationFunction = ..., axis: AxisOption = ..., *args: Any, **kwargs: Any) -> Union[Scalar, FrameOrSeries]: ...
    def transform(self, func: TransformFunction, axis: AxisOption = ..., *args: Any, **kwargs: Any) -> DataFrame: ...
    def apply(self, func: Function, axis: AxisOption = ..., raw: bool = ..., result_type: Optional[ApplyResultType] = ..., args: Any = ..., **kwds: Any) -> FrameOrSeries: ...
    def applymap(self, func: Callable[[Any], Any]) -> DataFrame: ...
    def append(self, other: Union[FrameOrSeries, Dict[Column, Any], List[Union[FrameOrSeries, Dict[Column, Any]]]], ignore_index: bool = ..., verify_integrity: bool = ..., sort: bool = ...) -> DataFrame: ...
    def join(self, other: Union[FrameOrSeries, List[DataFrame]], on: Optional[Union[str, List[str], ArrayLike]] = ..., how: JoinType = ..., lsuffix: str = ..., rsuffix: str = ..., sort: bool = ...) -> DataFrame: ...
    def merge(self, right: FrameOrSeries, how: MergeType = ..., on: Optional[Union[Label, List[Label]]] = ..., left_on: Optional[Union[Label, List[Label], ArrayLike]] = ..., right_on: Optional[Union[Label, List[Label], ArrayLike]] = ..., left_index: bool = ..., right_index: bool = ..., sort: bool = ..., suffixes: Tuple[str, str] = ..., copy: bool = ..., indicator: Union[bool, str] = ..., validate: Optional[MergeValidationMethod] = ...) -> DataFrame: ...
    def round(self, decimals: Union[int, Dict[Column, int], Series] = ..., *args: Any, **kwargs: Any) -> DataFrame: ...
    def corr(self, method: CorrelationMethod = ..., min_periods: Optional[int] = ...) -> DataFrame: ...
    def cov(self, min_periods: Optional[int] = ..., ddof: Optional[int] = ...) -> DataFrame: ...
    def corrwith(self, other: FrameOrSeries, axis: AxisOption = ..., drop: bool = ..., method: CorrelationMethod = ...) -> Series: ...
    def count(self, axis: AxisOption = ..., level: Optional[Level] = ..., numeric_only: bool = ...) -> FrameOrSeries: ...
    def nunique(self, axis: AxisOption = ..., dropna: Optional[bool] = ...) -> Series: ...
    def idxmin(self, axis: AxisOption = ..., skipna: Optional[bool] = ...) -> Series: ...
    def idxmax(self, axis: AxisOption = ..., skipna: Optional[bool] = ...) -> Series: ...
    def mode(self, axis: AxisOption = ..., numeric_only: bool = ..., dropna: Optional[bool] = ...) -> DataFrame: ...
    def quantile(self, q: Union[float, ArrayLike] = ..., axis: AxisOption = ..., numeric_only: bool = ..., interpolation: InterpolationMethod = ...) -> FrameOrSeries: ...
    def to_timestamp(self, freq: Optional[str] = ..., how: TimestampMethod = ..., axis: AxisOption = ..., copy: bool = ...) -> DataFrame: ...
    def to_period(self, freq: Optional[str] = ..., axis: AxisOption = ..., copy: bool = ...) -> DataFrame: ...
    def isin(self, values: Union[Sequence[Scalar], FrameOrSeries, Dict[Column, Scalar], np.ndarray]) -> DataFrame: ...
    def compare(self, other: DataFrame, align_axis: AxisOption = ..., keep_shape: bool = ..., keep_equal: bool = ...) -> DataFrame: ...

