import re
import pandas as pd


def test_types_split() -> None:
    s = pd.Series(['cat', 'dog', 'cow', 'coconut'])
    s2: pd.Series = s.str.split('o')
    s3: pd.Series = s.str.split('o', n=1)
    s4: pd.Series = s.str.split('o', expand=False)
    s5: pd.DataFrame = s.str.split('o', expand=True)


def test_types_replace() -> None:
    s = pd.Series(['cat', 'Dog', 'coconut'])
    s2: pd.Series = s.str.replace('do', 'ra')
    s3: pd.Series = s.str.replace('co', 'do', n=1)
    s4: pd.Series = s.str.replace('co', 'do', case=True)
    s5: pd.Series = s.str.replace(re.compile(r'(co)+'), repl='do', regex=True)
    s6: pd.Series = s.str.replace(re.compile(r'(co)+'), repl='do', flags=0)
