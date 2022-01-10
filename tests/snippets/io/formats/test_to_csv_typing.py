# flake8: noqa: F841
import tempfile

import pandas as pd
from pandas.io.parsers import TextFileReader


def test_types_read_csv() -> None:
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    csv_df: str = df.to_csv()

    with tempfile.NamedTemporaryFile() as file:
        df.to_csv(file.name)
        df2: pd.DataFrame = pd.read_csv(file.name)
        df3: pd.DataFrame = pd.read_csv(file.name, sep="a", squeeze=False)
        df4: pd.DataFrame = pd.read_csv(file.name, header=None, prefix="b", mangle_dupe_cols=True, keep_default_na=False)
        df5: pd.DataFrame = pd.read_csv(file.name, engine='python', true_values=[0, 1, 3], na_filter=False)
        df6: pd.DataFrame = pd.read_csv(file.name, skiprows=lambda x: x in [0, 2], skip_blank_lines=True, dayfirst=False)
        df7: pd.DataFrame = pd.read_csv(file.name, nrows=2)
        tfr1: TextFileReader = pd.read_csv(file.name, nrows=2, iterator=True, chunksize=3)
        tfr2: TextFileReader = pd.read_csv(file.name, nrows=2, chunksize=1)
        tfr3: TextFileReader = pd.read_csv(file.name, nrows=2, iterator=False, chunksize=1)
        tfr4: TextFileReader = pd.read_csv(file.name, nrows=2, iterator=True)
