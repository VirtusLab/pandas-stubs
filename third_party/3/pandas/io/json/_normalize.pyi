from typing import Any, Literal, Mapping, Optional, Sequence, Union

from pandas import DataFrame


def convert_to_line_delimits(s: Any) -> Any: ...
def nested_to_record(ds: Any, prefix: str=..., sep: str=..., level: int=..., max_level: Optional[int]=...) -> Any: ...

def json_normalize(data: Union[Mapping[Any, Any], Sequence[Mapping[Any, Any]]], record_path: Optional[Union[str, Sequence[str]]] = ..., meta: Optional[Union[str, Sequence[Union[str, Sequence[str]]]]] = ..., meta_prefix: Optional[str] = ..., record_prefix: Optional[str] = ..., errors: Literal['raise', 'ignore'] = ..., sep: str = ..., max_level: Optional[int] = ...) -> DataFrame: ...
