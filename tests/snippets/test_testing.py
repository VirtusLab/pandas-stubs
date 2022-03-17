from pandas._testing import assert_series_equal, assert_frame_equal

import pandas as pd


def test_types_assert_series_equal() -> None:
    s1 = pd.Series([0, 1, 1, 0])
    s2 = pd.Series([0, 1, 1, 0])
    assert_series_equal(left=s1, right=s2)
    assert_series_equal(s1, s2, check_freq=False, check_categorical=True, check_flags=True,
                        check_datetimelike_compat=True)
    assert_series_equal(s1, s2, check_dtype=True, check_less_precise=True, check_names=True)


def test_types_assert_frame_equal() -> None:
    df1 = pd.DataFrame(data={'col1': [1.0, 2.0], 'col2': [3.0, 4.0]})
    df2 = pd.DataFrame(data={'col1': [1.0, 2.0], 'col2': [3.0, 4.0]})
    assert_frame_equal(df1, df2)
    assert_frame_equal(df1, df2, atol=0.1, rtol=0.1)
