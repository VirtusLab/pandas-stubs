from collections import abc
from pandas._typing import ArrayLike, FilePathOrBuffer as FilePathOrBuffer, Scalar
from pandas.core import algorithms as algorithms
from pandas.core.arrays import Categorical as Categorical
from pandas.core.dtypes.cast import astype_nansafe as astype_nansafe
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, RangeIndex as RangeIndex, ensure_index_from_sequences as ensure_index_from_sequences
from pandas.core.series import Series as Series
from pandas.errors import AbstractMethodError as AbstractMethodError, EmptyDataError as EmptyDataError, ParserError as ParserError, ParserWarning as ParserWarning
from pandas.io.date_converters import generic_parser as generic_parser
from pandas.util._decorators import Appender as Appender
from typing import Any, Callable, Dict, List, Literal, Optional, AnyStr, overload, Sequence, Union

# not checking types in Callable params for read_csv, the documentation is too ambiguous
AnyCallable = Callable[[Any], Any]

@overload
def read_csv(filepath_or_buffer: FilePathOrBuffer[Any], sep: str = ..., delimiter: Optional[str] = ..., header: Optional[Union[int, List[int], str]] = ...,
             names: Optional[ArrayLike] = ..., index_col: Optional[Union[int, str, Sequence[int], Sequence[str], bool]] = None,
             usecols: Optional[Union[ArrayLike, AnyCallable]] = ..., squeeze: bool = ..., prefix: str = ..., mangle_dupe_cols: bool = ...,
             dtype: Any = ..., engine: Optional[Literal['c', 'python']] = ..., converters: Optional[Dict[Any, Any]] = ...,
             true_values: Optional[List[Any]] = ..., false_values: Optional[List[Any]] = ..., skipinitialspace: bool = ...,
             skiprows: Optional[Union[ArrayLike, int, AnyCallable]] = ..., skipfooter: int = ..., nrows: Optional[int] = ...,
             na_values: Optional[Union[Scalar, str, ArrayLike, Dict[Any, Any]]] = ..., keep_default_na: bool = ...,
             na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ...,
             parse_dates: Union[bool, List[int], List[str], List[List[Any]], Dict[Any, Any]] = ..., infer_datetime_format: bool = ...,
             keep_date_col: bool = ..., date_parser: Optional[AnyCallable] = ..., dayfirst: bool = ..., cache_dates: bool = ...,
             *, iterator: Literal[True], chunksize: Optional[int] = ..., **kwargs: Any) -> TextFileReader: ...

@overload
def read_csv(filepath_or_buffer: FilePathOrBuffer[Any], sep: str = ..., delimiter: Optional[str] = ..., header: Optional[Union[int, List[int], str]] = ...,
             names: Optional[ArrayLike] = ..., index_col: Optional[Union[int, str, Sequence[int], Sequence[str], bool]] = None,
             usecols: Optional[Union[ArrayLike, AnyCallable]] = ..., squeeze: bool = ..., prefix: str = ..., mangle_dupe_cols: bool = ...,
             dtype: Any = ..., engine: Optional[Literal['c', 'python']] = ..., converters: Optional[Dict[Any, Any]] = ...,
             true_values: Optional[List[Any]] = ..., false_values: Optional[List[Any]] = ..., skipinitialspace: bool = ...,
             skiprows: Optional[Union[ArrayLike, int, AnyCallable]] = ..., skipfooter: int = ..., nrows: Optional[int] = ...,
             na_values: Optional[Union[Scalar, str, ArrayLike, Dict[Any, Any]]] = ..., keep_default_na: bool = ...,
             na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ...,
             parse_dates: Union[bool, List[int], List[str], List[List[Any]], Dict[Any, Any]] = ..., infer_datetime_format: bool = ...,
             keep_date_col: bool = ..., date_parser: Optional[AnyCallable] = ..., dayfirst: bool = ..., cache_dates: bool = ...,
             *, iterator: Literal[False] = ..., chunksize: int, **kwargs: Any) -> TextFileReader: ...

@overload
def read_csv(filepath_or_buffer: FilePathOrBuffer[Any], sep: str = ..., delimiter: Optional[str] = ..., header: Optional[Union[int, List[int], str]] = ...,
             names: Optional[ArrayLike] = ..., index_col: Optional[Union[int, str, Sequence[int], Sequence[str], bool]] = None,
             usecols: Optional[Union[ArrayLike, AnyCallable]] = ..., squeeze: bool = ..., prefix: str = ..., mangle_dupe_cols: bool = ...,
             dtype: Any = ..., engine: Optional[Literal['c', 'python']] = ..., converters: Optional[Dict[Any, Any]] = ...,
             true_values: Optional[List[Any]] = ..., false_values: Optional[List[Any]] = ..., skipinitialspace: bool = ...,
             skiprows: Optional[Union[ArrayLike, int, AnyCallable]] = ..., skipfooter: int = ..., nrows: Optional[int] = ...,
             na_values: Optional[Union[Scalar, str, ArrayLike, Dict[Any, Any]]] = ..., keep_default_na: bool = ...,
             na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ...,
             parse_dates: Union[bool, List[int], List[str], List[List[Any]], Dict[Any, Any]] = ..., infer_datetime_format: bool = ...,
             keep_date_col: bool = ..., date_parser: Optional[AnyCallable] = ..., dayfirst: bool = ..., cache_dates: bool = ...,
             *, iterator: Literal[False] = ..., chunksize: None = ..., **kwargs: Any) -> DataFrame: ...

read_table: Any

def read_fwf(filepath_or_buffer: FilePathOrBuffer[AnyStr], colspecs: Any = ..., widths: Any = ..., infer_nrows: Any = ..., **kwds: Any) -> Any: ...

class TextFileReader(abc.Iterator[Any]):
    f: Any = ...
    orig_options: Any = ...
    engine: Any = ...
    chunksize: Any = ...
    nrows: Any = ...
    squeeze: Any = ...
    def __init__(self, f: Any, engine: Optional[Any] = ..., **kwds: Any) -> None: ...
    def close(self) -> None: ...
    def __next__(self) -> Any: ...
    def read(self, nrows: Optional[Any] = ...) -> Any: ...
    def get_chunk(self, size: Optional[Any] = ...) -> Any: ...

class ParserBase:
    names: Any = ...
    orig_names: Any = ...
    prefix: Any = ...
    index_col: Any = ...
    unnamed_cols: Any = ...
    index_names: Any = ...
    col_names: Any = ...
    parse_dates: Any = ...
    date_parser: Any = ...
    dayfirst: Any = ...
    keep_date_col: Any = ...
    na_values: Any = ...
    na_fvalues: Any = ...
    na_filter: Any = ...
    keep_default_na: Any = ...
    true_values: Any = ...
    false_values: Any = ...
    mangle_dupe_cols: Any = ...
    infer_datetime_format: Any = ...
    cache_dates: Any = ...
    header: Any = ...
    handles: Any = ...
    def __init__(self, kwds: Any) -> None: ...
    def close(self) -> None: ...

class CParserWrapper(ParserBase):
    kwds: Any = ...
    unnamed_cols: Any = ...
    names: Any = ...
    orig_names: Any = ...
    index_names: Any = ...
    def __init__(self, src: Any, **kwds: Any) -> None: ...
    def close(self) -> None: ...
    def set_error_bad_lines(self, status: Any) -> None: ...
    def read(self, nrows: Optional[Any] = ...) -> Any: ...

def TextParser(*args: Any, **kwds: Any) -> Any: ...
def count_empty_vals(vals: Any) -> Any: ...

class PythonParser(ParserBase):
    data: Any = ...
    buf: Any = ...
    pos: int = ...
    line_pos: int = ...
    encoding: Any = ...
    compression: Any = ...
    memory_map: Any = ...
    skiprows: Any = ...
    skipfunc: Any = ...
    skipfooter: Any = ...
    delimiter: Any = ...
    quotechar: Any = ...
    escapechar: Any = ...
    doublequote: Any = ...
    skipinitialspace: Any = ...
    lineterminator: Any = ...
    quoting: Any = ...
    skip_blank_lines: Any = ...
    warn_bad_lines: Any = ...
    error_bad_lines: Any = ...
    names_passed: Any = ...
    has_index_names: bool = ...
    verbose: Any = ...
    converters: Any = ...
    dtype: Any = ...
    thousands: Any = ...
    decimal: Any = ...
    comment: Any = ...
    num_original_columns: Any = ...
    columns: Any = ...
    orig_names: Any = ...
    index_names: Any = ...
    nonnum: Any = ...
    def __init__(self, f: Any, **kwds: Any) -> None: ...
    def read(self, rows: Optional[Any] = ...) -> Any: ...
    def get_chunk(self, size: Optional[Any] = ...) -> Any: ...

class FixedWidthReader(abc.Iterator[Any]):
    f: Any = ...
    buffer: Any = ...
    delimiter: Any = ...
    comment: Any = ...
    colspecs: Any = ...
    def __init__(self, f: Any, colspecs: Any, delimiter: Any, comment: Any, skiprows: Optional[Any] = ..., infer_nrows: int = ...) -> None: ...
    def get_rows(self, infer_nrows: Any, skiprows: Optional[Any] = ...) -> Any: ...
    def detect_colspecs(self, infer_nrows: int = ..., skiprows: Optional[Any] = ...) -> Any: ...
    def __next__(self) -> Any: ...

class FixedWidthFieldParser(PythonParser):
    colspecs: Any = ...
    infer_nrows: Any = ...
    def __init__(self, f: Any, **kwds: Any) -> None: ...
