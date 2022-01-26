import sys
from collections import abc
from pandas._typing import ArrayLike, FilePathOrBuffer as FilePathOrBuffer, Scalar
from pandas.core.frame import DataFrame as DataFrame
from typing import Any, Callable, Dict, List, Optional, AnyStr, overload, Sequence, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


# not checking types in Callable params for read_csv, the documentation is too ambiguous
AnyCallable = Callable[[Any], Any]
CompressionFormat = Literal["infer", "gzip", "bz2", "zip", "xz"]
BadLineOption = Literal["error", "warn", "skip"]

@overload
def read_csv(filepath_or_buffer: Any, sep: str = ..., delimiter: Optional[str] = ..., header: Optional[Union[int, List[int], str]] = ...,
             names: Optional[Union[ArrayLike, Sequence[str]]] = ..., index_col: Optional[Union[int, str, Sequence[int], Sequence[str], bool]] = None,
             usecols: Optional[Union[int, str, List[str], List[int], ArrayLike, AnyCallable]] = ..., squeeze: bool = ..., prefix: str = ..., mangle_dupe_cols: bool = ...,
             dtype: Any = ..., engine: Optional[Literal['c', 'python']] = ..., converters: Optional[Dict[Any, Any]] = ...,
             true_values: Optional[List[Any]] = ..., false_values: Optional[List[Any]] = ..., skipinitialspace: bool = ...,
             skiprows: Optional[Union[ArrayLike, int, AnyCallable]] = ..., skipfooter: int = ..., nrows: Optional[int] = ...,
             na_values: Optional[Union[Scalar, str, ArrayLike, Dict[Any, Any]]] = ..., keep_default_na: bool = ...,
             na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ...,
             parse_dates: Union[bool, List[int], List[str], List[List[Any]], Dict[Any, Any]] = ..., infer_datetime_format: bool = ...,
             keep_date_col: bool = ..., date_parser: Optional[AnyCallable] = ..., dayfirst: bool = ..., cache_dates: bool = ...,
             *, iterator: Literal[True], chunksize: Optional[int] = ..., compression: Optional[Union[str, CompressionFormat]] = ...,
             thousands: Optional[str] = ..., decimal: Optional[str] = ..., lineterminator: Optional[str] = ..., quotechar: str = ...,
             quoting: int = ..., doublequote: bool = ..., escapechar: Optional[str] = ..., comment: Optional[str] = ...,
             encoding: Optional[str] = ..., dialect: Optional[str] = ..., error_bad_lines: bool = ..., warn_bad_lines: bool = ...,
             on_bad_lines: BadLineOption = ..., delim_whitespace: bool = ..., low_memory: bool = ...,
             memory_map: bool = ..., float_precision: Optional[str] = ..., storage_options: Optional[Dict[str, Any]] = ..., ) -> TextFileReader: ...


@overload
def read_csv(filepath_or_buffer: Any, sep: str = ..., delimiter: Optional[str] = ..., header: Optional[Union[int, List[int], str]] = ...,
             names: Optional[Union[ArrayLike, Sequence[str]]] = ..., index_col: Optional[Union[int, str, Sequence[int], Sequence[str], bool]] = None,
             usecols: Optional[Union[int, str, List[str], List[int], ArrayLike, AnyCallable]] = ..., squeeze: bool = ..., prefix: str = ..., mangle_dupe_cols: bool = ...,
             dtype: Any = ..., engine: Optional[Literal['c', 'python']] = ..., converters: Optional[Dict[Any, Any]] = ...,
             true_values: Optional[List[Any]] = ..., false_values: Optional[List[Any]] = ..., skipinitialspace: bool = ...,
             skiprows: Optional[Union[ArrayLike, int, AnyCallable]] = ..., skipfooter: int = ..., nrows: Optional[int] = ...,
             na_values: Optional[Union[Scalar, str, ArrayLike, Dict[Any, Any]]] = ..., keep_default_na: bool = ...,
             na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ...,
             parse_dates: Union[bool, List[int], List[str], List[List[Any]], Dict[Any, Any]] = ..., infer_datetime_format: bool = ...,
             keep_date_col: bool = ..., date_parser: Optional[AnyCallable] = ..., dayfirst: bool = ..., cache_dates: bool = ...,
             *, iterator: Literal[False] = ..., chunksize: int, compression: Optional[Union[str, CompressionFormat]] = ...,
             thousands: Optional[str] = ..., decimal: Optional[str] = ..., lineterminator: Optional[str] = ..., quotechar: str = ...,
             quoting: int = ..., doublequote: bool = ..., escapechar: Optional[str] = ..., comment: Optional[str] = ...,
             encoding: Optional[str] = ..., dialect: Optional[str] = ..., error_bad_lines: bool = ..., warn_bad_lines: bool = ...,
             on_bad_lines: BadLineOption = ..., delim_whitespace: bool = ..., low_memory: bool = ...,
             memory_map: bool = ..., float_precision: Optional[str] = ..., storage_options: Optional[Dict[str, Any]] = ..., ) -> TextFileReader: ...

@overload
def read_csv(filepath_or_buffer: Any, sep: str = ..., delimiter: Optional[str] = ..., header: Optional[Union[int, List[int], str]] = ...,
             names: Optional[Union[ArrayLike, Sequence[str]]] = ..., index_col: Optional[Union[int, str, Sequence[int], Sequence[str], bool]] = None,
             usecols: Optional[Union[int, str, List[str], List[int]]] = ..., squeeze: bool = ..., prefix: str = ..., mangle_dupe_cols: bool = ...,
             dtype: Any = ..., engine: Optional[Literal['c', 'python']] = ..., converters: Optional[Dict[Any, Any]] = ...,
             true_values: Optional[List[Any]] = ..., false_values: Optional[List[Any]] = ..., skipinitialspace: bool = ...,
             skiprows: Optional[Union[ArrayLike, int, AnyCallable]] = ..., skipfooter: int = ..., nrows: Optional[int] = ...,
             na_values: Optional[Union[Scalar, str, ArrayLike, Dict[Any, Any]]] = ..., keep_default_na: bool = ...,
             na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ...,
             parse_dates: Union[bool, List[int], List[str], List[List[Any]], Dict[Any, Any]] = ..., infer_datetime_format: bool = ...,
             keep_date_col: bool = ..., date_parser: Optional[AnyCallable] = ..., dayfirst: bool = ..., cache_dates: bool = ...,
             *, iterator: Literal[False] = ..., chunksize: None = ..., compression: Optional[Union[str, CompressionFormat]] = ...,
             thousands: Optional[str] = ..., decimal: Optional[str] = ..., lineterminator: Optional[str] = ..., quotechar: str = ...,
             quoting: int = ..., doublequote: bool = ..., escapechar: Optional[str] = ..., comment: Optional[str] = ...,
             encoding: Optional[str] = ..., dialect: Optional[str] = ..., error_bad_lines: bool = ..., warn_bad_lines: bool = ...,
             on_bad_lines: BadLineOption = ..., delim_whitespace: bool = ..., low_memory: bool = ...,
             memory_map: bool = ..., float_precision: Optional[str] = ..., storage_options: Optional[Dict[str, Any]] = ..., ) -> DataFrame: ...


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

def TextParser(*args: Any, **kwds: Any) -> Any: ...