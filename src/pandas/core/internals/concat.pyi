from pandas._libs import tslibs as tslibs
from pandas.core.dtypes.cast import maybe_promote as maybe_promote

from pandas.core.dtypes.missing import isna as isna
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Any, Optional

def get_mgr_concatenation_plan(mgr: Any, indexers: Any) -> Any: ...

class JoinUnit:
    block: Any = ...
    indexers: Any = ...
    shape: Any = ...
    def __init__(self, block: Any, shape: Any, indexers: Optional[Any] = ...) -> None: ...
    def needs_filling(self) -> Any: ...
    def dtype(self) -> Any: ...
    def is_na(self) -> Any: ...
    def get_reindexed_values(self, empty_dtype: Any, upcasted_na: Any) -> Any: ...

def concatenate_join_units(join_units: Any, concat_axis: Any, copy: Any) -> Any: ...
def is_uniform_join_units(join_units: Any) -> Any: ...
def combine_concat_plans(plans: Any, concat_axis: Any) -> Any: ...
