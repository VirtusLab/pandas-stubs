import re
import pandas as pd


def test_types_split() -> None:
    s = pd.Series(['cat', 'dog', 'cow', 'coconut'])
    s: pd.Series = s.str.split('o')
    s: pd.Series = s.str.split('o', n=1)
    s: pd.Series = s.str.split('o', expand=False)
    s: pd.DataFrame = s.str.split('o', expand=True)


def test_types_replace() -> None:
    s = pd.Series(['cat', 'Dog', 'coconut'])
    s: pd.Series = s.str.replace('do', 'ra')
    s: pd.Series = s.str.replace('co', 'do', n=1)
    s: pd.Series = s.str.replace('co', 'do', case=True)
    s: pd.Series = s.str.replace(re.compile(r'(co)+'), repl='do', regex=True)
    s: pd.Series = s.str.replace(re.compile(r'(co)+'), repl='do', flags=0)
