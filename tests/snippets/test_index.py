# flake8: noqa: F841
import pandas as pd
import numpy as np


def test_boolean() -> None:
    base: pd.Index = pd.Index([-1, 2, 5])

    idx: np.ndarray = base > 0
    idx2: np.ndarray = base >= 0
    idx3: np.ndarray = base < 0
    idx4: np.ndarray = base <= 0
    idx5: np.ndarray = base == 0
    idx6: np.ndarray = base != 0

