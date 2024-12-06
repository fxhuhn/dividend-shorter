import os
import time
from datetime import datetime, timedelta

import pandas as pd
import requests
import yfinance as yf
from polygon import RESTClient

# Dividenden Screener

API_POLYGON = os.environ.get("API_POLYGON")


def add_business_days(start_date: datetime, business_days: int) -> datetime:
    """
    Add a specified number of business days to a start date.

    Parameters:
    start_date (datetime): The starting date.
    business_days (int): The number of business days to add.

    Returns:
    datetime: The resulting date after adding the business days.
    """
    current_date = start_date
    days_added = 0

    while days_added < business_days:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5:  # Monday to Friday are business days
            days_added += 1

    return current_date


def get_dividend_stocks(day: str) -> pd.DataFrame:
    client = RESTClient(api_key=API_POLYGON)
    df = pd.DataFrame.from_dict(
        client.list_dividends(ex_dividend_date=day, limit=1_000)
    )
    time.sleep(20)
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

    url = "https://api.nasdaq.com/api/calendar/dividends"
    headers = {
        "Accept": "application/json",
        "Origin": "https://www.nasdaq.com",
        "Referer": "https://www.nasdaq.com",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        ),
    }
    payload = {"date": div_date.strftime("%Y-%m-%d")}

    response = requests.get(url, headers=headers, params=payload)

    if response.status_code == 200:
        json_data = response.json()
        df = pd.DataFrame(json_data.get("data", {}).get("calendar", {}).get("rows", []))

        if not df.empty:
            df["dividend_Ex_Date"] = pd.to_datetime(
                df["dividend_Ex_Date"], errors="coerce"
            )
            df["adr"] = df.companyName.str.contains("ADR")
            df["etf"] = df.companyName.str.contains("ETF")
            df["bond"] = df.companyName.str.contains("Bond")

            df2 = get_dividend_stocks(div_date)
            if len(df2):
                df = pd.merge(
                    df,
                    df2[["cash_amount", "dividend_type", "ticker"]],
                    left_on="symbol",
                    right_on="ticker",
                    how="left",
                )
            return df

    return pd.DataFrame()


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


def export_screener(df: pd.DataFrame) -> None:
    """
    Export the screener data to a formatted output.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the screener data.
    """

    pd.options.display.float_format = "{:.2f}".format
    df.replace({True: "X", False: ""}, inplace=True)
    df.Volume = df.Volume.astype(int)

    df.rename(
        columns={
            "symbol": "Ticker",
            "dividend_Ex_Date": "Date",
            "dividend_percentage": "Divid %",
            "Last Close": "Close",
            "dividend_Rate": "Divid Rate",
            "roc_5_pos": "5_Days_pos",
        },
        inplace=True,
    )

    df.set_index("Date", inplace=True)

    print(
        df[
            [
                "Ticker",
                # "Date",
                "Volume",
                "Close",
                "Divid Rate",
                "Divid %",
                "cash_amount",
                "5_Days_pos",
                "above_SMA_50",
                "etf",
                "adr",
                "bond",
                "dividend_type",
            ]
        ].to_string()
    )

    df[
        [
            "Ticker",
            "companyName",
            "Volume",
            "Close",
            "Divid Rate",
            "Divid %",
            "5_Days_pos",
            "above_SMA_50",
            "etf",
            "adr",
            "bond",
            "dividend_type",
        ]
    ].to_csv("./screener.csv")


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

    for index, row in df.iterrows():
        hist = yf.download(row.symbol.replace(".", "-"), progress=False)

        if hist.empty or len(hist) < 6:
            continue  # Skip symbols with not enough data

        try:
            df.at[index, "Close"] = round(hist.Close.iloc[-1], 2)

            df.at[index, "Volume"] = round(hist.Volume.iloc[-1])
            df.at[index, "SMA_50"] = round(hist.Close.rolling(50).mean().iloc[-1], 2)
            df.at[index, "dividend_percentage"] = round(
                (row.dividend_Rate / hist.Close.iloc[-1]) * 100, 2
            )
            df.at[index, "last_close_volume"] = round(
                hist.Close.iloc[-1] * hist.Volume.iloc[-1]
            )
            df.at[index, "close_5_days_ago"] = hist.Close.iloc[-5]
        except Exception:
            print(round(hist.Close.iloc[-1], 2))
            print(index)

    df["dividend_Rate"] = df.dividend_Rate.round(2)
    df["roc_5_pos"] = df["Close"] > df["close_5_days_ago"]
    df["above_SMA_50"] = df["Close"] > df["SMA_50"]

    df = df[df["last_close_volume"] > 100_000]
    df = df[df["dividend_percentage"] > 2.5]

    return df.sort_values(by="dividend_Ex_Date")


def main() -> None:
    """
    Main function to execute the dividend screener.
    """
    today = datetime.now()

    df = get_dividend_days(
        start_date=(today).date(),
        end_date=add_business_days(today, 7).date(),
    )
    df = update_stock_data(df)
    export_screener(df)


if __name__ == "__main__":
    main()
