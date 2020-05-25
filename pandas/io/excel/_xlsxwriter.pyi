from pandas.io.excel._base import ExcelWriter as ExcelWriter
from typing import Any, Optional

class _XlsxStyler:
    STYLE_MAPPING: Any = ...
    @classmethod
    def convert(cls, style_dict: Any, num_format_str: Optional[Any] = ...) -> Any: ...

class _XlsxWriter(ExcelWriter):
    engine: str = ...
    supported_extensions: Any = ...
    book: Any = ...
    def __init__(self, path: Any, engine: Optional[Any] = ..., date_format: Optional[Any] = ..., datetime_format: Optional[Any] = ..., mode: str = ..., **engine_kwargs: Any) -> None: ...
    def save(self) -> Any: ...
    def write_cells(self, cells: Any, sheet_name: Optional[Any] = ..., startrow: int = ..., startcol: int = ..., freeze_panes: Optional[Any] = ...) -> None: ...
