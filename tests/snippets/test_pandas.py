import pandas as pd


def test_types_to_datetime() -> None:
    df = pd.DataFrame({'year': [2015, 2016],
                       'month': [2, 3],
                       'day': [4, 5]})
    pd.to_datetime(df)
    pd.to_datetime(df, unit="s", origin="unix", infer_datetime_format=True)
    pd.to_datetime(df, unit="ns", dayfirst=True, utc=None, format="%M:%D", exact=False)
    pd.to_datetime([1, 2], unit="D", origin=pd.Timestamp("01/01/2000"))
    pd.to_datetime([1, 2], unit="D", origin=3)
