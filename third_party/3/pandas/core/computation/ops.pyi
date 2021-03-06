import numpy as np
from pandas._libs.tslibs import Timestamp as Timestamp
from pandas.core.computation.common import result_type_many as result_type_many

from pandas.io.formats.printing import pprint_thing as pprint_thing, pprint_thing_encoded as pprint_thing_encoded
from typing import Any, Optional

class UndefinedVariableError(NameError):
    def __init__(self, name: Any, is_local: bool) -> None: ...

class Term:
    def __new__(cls, name: Any, env: Any, side: Optional[Any] = ..., encoding: Optional[Any] = ...) -> Any: ...
    is_local: bool
    env: Any = ...
    side: Any = ...
    encoding: Any = ...
    def __init__(self, name: Any, env: Any, side: Optional[Any] = ..., encoding: Optional[Any] = ...) -> None: ...
    @property
    def local_name(self) -> str: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def evaluate(self, *args: Any, **kwargs: Any) -> Any: ...
    def update(self, value: Any) -> None: ...
    @property
    def is_scalar(self) -> bool: ...
    @property
    def type(self) -> Any: ...
    return_type: Any = ...
    @property
    def raw(self) -> str: ...
    @property
    def is_datetime(self) -> bool: ...
    @property
    def value(self) -> Any: ...
    @value.setter
    def value(self, new_value: Any) -> None: ...
    @property
    def name(self) -> Any: ...
    @property
    def ndim(self) -> int: ...

class Constant(Term):
    def __init__(self, value: Any, env: Any, side: Optional[Any] = ..., encoding: Optional[Any] = ...) -> None: ...
    @property
    def name(self) -> Any: ...

class Op:
    op: str
    operands: Any = ...
    encoding: Any = ...
    def __init__(self, op: str, operands: Any, *args: Any, **kwargs: Any) -> None: ...
    def __iter__(self) -> Any: ...
    @property
    def return_type(self) -> Any: ...
    @property
    def has_invalid_return_type(self) -> bool: ...
    @property
    def operand_types(self) -> Any: ...
    @property
    def is_scalar(self) -> bool: ...
    @property
    def is_datetime(self) -> bool: ...

def is_term(obj: Any) -> bool: ...

class BinOp(Op):
    lhs: Any = ...
    rhs: Any = ...
    func: Any = ...
    def __init__(self, op: str, lhs: Any, rhs: Any, **kwargs: Any) -> None: ...
    def __call__(self, env: Any) -> Any: ...
    def evaluate(self, env: Any, engine: str, parser: Any, term_type: Any, eval_in_python: Any) -> Any: ...
    def convert_values(self) -> Any: ...

def isnumeric(dtype: Any) -> bool: ...

class Div(BinOp):
    def __init__(self, lhs: Any, rhs: Any, **kwargs: Any) -> None: ...

class UnaryOp(Op):
    operand: Any = ...
    func: Any = ...
    def __init__(self, op: str, operand: Any) -> None: ...
    def __call__(self, env: Any) -> Any: ...
    @property
    def return_type(self) -> np.dtype: ...

class MathCall(Op):
    func: Any = ...
    def __init__(self, func: Any, args: Any) -> None: ...
    def __call__(self, env: Any) -> Any: ...

class FuncNode:
    name: Any = ...
    func: Any = ...
    def __init__(self, name: str) -> None: ...
    def __call__(self, *args: Any) -> Any: ...
