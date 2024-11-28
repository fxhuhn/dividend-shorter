import os
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf
from polygon import RESTClient

API_POLYGON = os.environ.get("API_POLYGON")


def get_dividend_stocks(day: str) -> pd.DataFrame:
    client = RESTClient(api_key=API_POLYGON)
    df = pd.DataFrame.from_dict(
        client.list_dividends(ex_dividend_date=day, limit=1_000)
    )

    if len(df) > 0:
        return df[df.currency == "USD"]
    return df


def get_dividend_day(div_date: datetime = None) -> pd.DataFrame:
    """
    Fetch dividend data for a specific date from the NASDAQ API.

    Parameters:
    div_date (datetime): The date for which to fetch dividend data. Defaults to today.

    Returns:
    pd.DataFrame: A DataFrame containing the dividend data.
    """
    if div_date is None:
        div_date = datetime.now()

        # df["adr"] = df.companyName.str.contains("ADR")
        # df["etf"] = df.companyName.str.contains("ETF")
        # df["bond"] = df.companyName.str.contains("Bond")

    return get_dividend_stocks(div_date.date().isoformat())


def get_dividend_days(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """
    Fetch dividend data for a range of dates.

    Parameters:
    start_date (datetime): The starting date.
    end_date (datetime): The ending date.

    Returns:
    pd.DataFrame: A DataFrame containing the dividend data for the date range.
    """
    dfs = []

    while start_date <= end_date:
        if start_date.weekday() < 5:  # Only consider weekdays
            dfs.append(get_dividend_day(start_date))
        start_date += timedelta(days=1)

    return pd.concat(dfs, ignore_index=True)


def update_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Update the stock data with additional financial metrics.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the initial stock data.

    Returns:
    pd.DataFrame: The updated DataFrame with additional financial metrics.
    """
    df["Close"] = 0.0
    df["Volume"] = 0.0
    df["dividend_percentage"] = 0.0
    df["last_close_volume"] = 0.0
    df["close_5_days_ago"] = 0.0
    df["SMA_50"] = 0.0

    if len(df) == 0:
        return pd.DataFrame()

    for index, row in df.iterrows():
        hist = yf.download(row.ticker.replace(".", "-"), progress=False)

        if hist.empty or len(hist) < 6:
            continue  # Skip symbols with not enough data

        df.at[index, "Close"] = round(hist.Close.iloc[-1], 2)
        df.at[index, "Volume"] = round(hist.Volume.iloc[-1])
        df.at[index, "SMA_50"] = round(hist.Close.rolling(50).mean().iloc[-1], 2)
        # df.at[index, "dividend_percentage"] = round(
        #    (row.cash_amount / hist.Close.iloc[-1]) * 100, 2
        # )
        # df.at[index, "last_close_volume"] = round(
        #    hist.Close.iloc[-1] * hist.Volume.iloc[-1]
        # )
        df.at[index, "close_5_days_ago"] = hist.Close.iloc[-5]

    df["last_close_volume"] = round(df.Close * df.Volume).astype(int)
    df["dividend_percentage"] = round((df.cash_amount / df.Close) * 100, 2)

    df["cash_amount"] = df.cash_amount.round(2)
    df["roc_5_pos"] = df["Close"] > df["close_5_days_ago"]
    df["above_SMA_50"] = df["Close"] > df["SMA_50"]

    df = df[df["last_close_volume"] > 100_000]
    df = df[df["dividend_percentage"] > 2.5]

    return df[
        [
            "ticker",
            "cash_amount",
            "Close",
            "Volume",
            "last_close_volume",
            "dividend_percentage",
            "roc_5_pos",
            "above_SMA_50",
        ]
    ]  # .sort_values(by="ex_dividend_date")


def get_dividend_history(symbol: str) -> pd.DataFrame:
    API_POLYGON = "RZwsNm2Nt54M1a1w3uvV1vcdNH_NeCv9"

    client = RESTClient(api_key=API_POLYGON)
    df = pd.DataFrame.from_dict(client.list_dividends(ticker=symbol, limit=1_000))

    if len(df) > 0:
        df.ex_dividend_date = pd.to_datetime(df.ex_dividend_date)
        df.declaration_date = pd.to_datetime(df.declaration_date)
        df.pay_date = pd.to_datetime(df.pay_date)
        df.record_date = pd.to_datetime(df.record_date)

    return df
