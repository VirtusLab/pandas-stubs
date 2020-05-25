from pandas._config import get_option as get_option
from pandas._libs import lib as lib
from pandas.compat._optional import import_optional_dependency as import_optional_dependency

from pandas.util._decorators import Appender as Appender
from typing import Any, Optional

jinja2: Any
has_mpl: bool
no_mpl_message: str

class Styler:
    loader: Any = ...
    env: Any = ...
    template: Any = ...
    ctx: Any = ...
    data: Any = ...
    index: Any = ...
    columns: Any = ...
    uuid: Any = ...
    table_styles: Any = ...
    caption: Any = ...
    precision: Any = ...
    table_attributes: Any = ...
    hidden_index: bool = ...
    hidden_columns: Any = ...
    cell_ids: Any = ...
    na_rep: Any = ...
    def __init__(self, data: Any, precision: Any = ..., table_styles: Any = ..., uuid: Any = ..., caption: Any = ..., table_attributes: Any = ..., cell_ids: Any = ..., na_rep: Optional[str]=...) -> None: ...
    def to_excel(self, excel_writer: Any, sheet_name: str = ..., na_rep: str = ..., float_format: Optional[Any] = ..., columns: Optional[Any] = ..., header: bool = ..., index: bool = ..., index_label: Optional[Any] = ..., startrow: int = ..., startcol: int = ..., engine: Optional[Any] = ..., merge_cells: bool = ..., encoding: Optional[Any] = ..., inf_rep: str = ..., verbose: bool = ..., freeze_panes: Optional[Any] = ...) -> None: ...
    def format(self, formatter: Any, subset: Any = ..., na_rep: Optional[str]=...) -> Any: ...
    def render(self, **kwargs: Any) -> Any: ...
    def __copy__(self) -> Any: ...
    def __deepcopy__(self, memo: Any) -> Any: ...
    def clear(self) -> None: ...
    def apply(self, func: Any, axis: int = ..., subset: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def applymap(self, func: Any, subset: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def where(self, cond: Any, value: Any, other: Optional[Any] = ..., subset: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def set_precision(self, precision: Any) -> Any: ...
    def set_table_attributes(self, attributes: Any) -> Any: ...
    def export(self) -> Any: ...
    def use(self, styles: Any) -> Any: ...
    def set_uuid(self, uuid: Any) -> Any: ...
    def set_caption(self, caption: Any) -> Any: ...
    def set_table_styles(self, table_styles: Any) -> Any: ...
    def set_na_rep(self, na_rep: str) -> Styler: ...
    def hide_index(self) -> Any: ...
    def hide_columns(self, subset: Any) -> Any: ...
    def highlight_null(self, null_color: str = ...) -> Any: ...
    def background_gradient(self, cmap: Any = ..., low: Any = ..., high: Any = ..., axis: Any = ..., subset: Any = ..., text_color_threshold: Any = ..., vmin: Optional[float]=..., vmax: Optional[float]=...) -> Any: ...
    def set_properties(self, subset: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def bar(self, subset: Optional[Any] = ..., axis: int = ..., color: str = ..., width: int = ..., align: str = ..., vmin: Optional[Any] = ..., vmax: Optional[Any] = ...) -> Any: ...
    def highlight_max(self, subset: Optional[Any] = ..., color: str = ..., axis: int = ...) -> Any: ...
    def highlight_min(self, subset: Optional[Any] = ..., color: str = ..., axis: int = ...) -> Any: ...
    @classmethod
    def from_custom_template(cls, searchpath: Any, name: Any) -> Any: ...
    def pipe(self, func: Any, *args: Any, **kwargs: Any) -> Any: ...
