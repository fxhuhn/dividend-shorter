import time
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

from tools import core

symbol = "VOD"


def dividend_details(symbol: str) -> None:
    stock = yf.download(symbol)
    df2 = core.get_dividend_history(symbol)
    name = yf.Ticker(symbol).info.get("longName")

    stock["SMA_50"] = round(stock.Close.rolling(50).mean(), 2)
    stock["Close_Volume"] = round(stock.Close * stock.Volume)
    stock["prev_Close"] = stock.Close.shift(1)

    for i in range(5):
        stock[f"Day_{i}"] = (
            (stock.Open - stock.Close.shift(-i)) / stock.Close.shift(-i) * 100
        )
        stock[f"Day_r_{i}"] = (stock.Open - stock.Close.shift(-i)) / (
            stock.High.shift(1) - stock.Open
        )
        stock[f"Day_r_{i}"] = np.where(
            stock[f"Day_r_{i}"] > -1, stock[f"Day_r_{i}"], -1
        )

    for i in range(4):
        stock[f"Day_r_{i+1}"] = np.where(
            stock[f"Day_r_{i}"] == -1, -1, stock[f"Day_r_{i+1}"]
        )

    stock["ROC_5_Filter"] = (stock.Close > stock.Close.shift(5)).shift(-1)
    stock["above_SMA_50"] = stock.Close > stock.SMA_50.shift(-1)
    stock["Close_Volume_Filter"] = (stock.Close_Volume > 1_000_000).shift(-1)

    df3 = pd.merge(
        df2[["ex_dividend_date", "cash_amount", "dividend_type"]],
        stock[
            [
                "prev_Close",
                "Day_0",
                "Day_1",
                "Day_2",
                "Day_3",
                "Day_4",
                "Day_r_0",
                "Day_r_1",
                "Day_r_2",
                "Day_r_3",
                "Day_r_4",
                "ROC_5_Filter",
                "above_SMA_50",
                "Close_Volume_Filter",
            ]
        ],
        left_on="ex_dividend_date",
        right_index=True,
        how="inner",
    )
    df3 = df3.set_index("ex_dividend_date")

    df3["Dividend_Percentage"] = round((df3.cash_amount / df3.prev_Close) * 100, 2)
    df3["Dividend_Percentage_Filter"] = df3.Dividend_Percentage > 2.75

    # df3[df3.Close_Volume_Filter & df3.Dividend_Percentage_Filter][['Profit_0', 'Profit_1', 'Profit_2', 'Profit_3', 'Profit_4']].T.plot()

    df4 = df3[["Day_r_0", "Day_r_1", "Day_r_2", "Day_r_3", "Day_r_4"]].reset_index(
        drop=True
    )
    df4.index.name = "Gewinn"
    df4.plot.box(title=name).get_figure().savefig(f"./data/{symbol}_box_all.png")
    plt.clf()
    df4.median().plot(kind="bar", title=name).get_figure().savefig(
        f"./data/{symbol}_median_all.png"
    )
    df = df4.median()
    df["Treffer"] = len(df4)
    plt.clf()

    df4 = df3[df3.Close_Volume_Filter & df3.Dividend_Percentage_Filter][
        ["Day_r_0", "Day_r_1", "Day_r_2", "Day_r_3", "Day_r_4"]
    ].reset_index(drop=True)

    df4.index.name = "Gewinn"

    df4.plot.box(title=name, ylabel="R in %", xlabel="Tage").get_figure().savefig(
        f"./data/{symbol}_box_filtered.png"
    )
    plt.clf()
    df4.median().plot(
        kind="bar", title=name, ylabel="R in %", xlabel="Tage"
    ).get_figure().savefig(f"./data/{symbol}_median_filtered.png")
    plt.clf()

    df = pd.concat(
        [pd.DataFrame(df).T, pd.DataFrame(df4.median()).T], keys=["ohne", "mit"]
    ).reset_index(level=1, drop=True)

    df.iloc[-1, -1] = len(df4)

    with open("template.md", "r") as file:
        template = file.read()

    template = template.replace("{table}", df.round(1).to_markdown())
    template = template.replace("{box_all}", f"{symbol}_box_all.png")
    template = template.replace("{box_filtered}", f"{symbol}_box_filtered.png")
    template = template.replace("{median_all}", f"{symbol}_median_all.png")
    template = template.replace("{median_filtered}", f"{symbol}_median_filtered.png")

    with open(f"./data/{symbol}.md", "w") as text_file:
        text_file.write(template)


def get_trading_day() -> datetime:
    today = datetime.now()

    match today.weekday():
        case 5:  # Samstag
            return today + timedelta(days=2)
        case 6:  # Sonntag
            return today + timedelta(days=1)
        # case _:
    return datetime.now()


def main() -> None:
    df = core.update_stock_data(core.get_dividend_day(get_trading_day()))

    df.rename(
        columns={
            # "symbol": "Symbol",
            "ticker": "Ticker",
            "dividend_Ex_Date": "Date",
            "dividend_percentage": "Divid %",
            "Last Close": "Close",
            # "dividend_Rate": "Divid Rate_2",
            "cash_amount": "Divid Rate",
            "roc_5_pos": "5_Days_pos",
        },
        inplace=True,
    )

    print(
        df[
            [
                "Ticker",
                # "Symbol",
                "Volume",
                "Close",
                "Divid Rate",
                # "Divid Rate_2",
                "Divid %",
                "5_Days_pos",
                "above_SMA_50",
            ]
        ]
    )

    with open("shorts.md", "w") as text_file:
        text_file.write(df.to_markdown(index=False))

    for symbol in df.Ticker:
        dividend_details(symbol)
        time.sleep(15)

    readme = "# dividend-shorter\n\nbet on falling prices on payday\n\n"

    with open("./shorts.md", "r") as file:
        short_signals = file.read()
    readme = readme + f"## Signale\n\n{short_signals}\n\n"

    for symbol in df.Ticker:
        with open(f"./data/{symbol}.md", "r") as file:
            stock_report = file.read()
        readme = readme + f"## {symbol}\n\n"
        readme = readme + f"{stock_report}\n\n"

    with open("README.md", "w") as text_file:
        text_file.write(readme)


if __name__ == "__main__":
    main()
