import pandas as pd
import numpy as np


def test_mypy_test_init() -> None:
    pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    pd.DataFrame(data=[1, 2, 3, 4], dtype=np.int8)
    pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'], dtype=np.int8, copy=True)
