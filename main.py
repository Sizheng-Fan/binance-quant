from binance.client import Client
import pandas as pd

api_key = 'pw4d3dLx6QEnKoEVMIpNR4tcl3bZiUkq2lqpUE144eMhqKUrQFt2uvAywL6roLvz'
api_secret = 'gL9v3uhgAmjVcG7HzaCyx3Z7gRStMSBt2z6H4y8zZi2ZVtDpAcOgKnNZG777NsD4'


def get_market_data():
    # 创建客户端
    client = Client(api_key, api_secret)

    try:
        # 获取市场深度数据（Order Book）
        depth = client.futures_order_book(symbol='BTCUSDT')
        print("Order Book (Depth Data):")
        print(depth)

        # 获取最近的成交数据
        trades = client.futures_recent_trades(symbol='BTCUSDT')
        print("\nRecent Trades:")
        print(trades)

        # 获取历史K线数据
        klines = client.futures_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR)
        df_klines = pd.DataFrame(klines, columns=[
            'Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
            'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
            'Taker buy quote asset volume', 'Ignore'
        ])
        print("\nHistorical Klines (Candlestick Data):")
        print(df_klines.head())

        # 获取24小时价格变动数据
        ticker_24hr = client.futures_ticker(symbol='BTCUSDT')
        print("\n24hr Ticker Data:")
        print(ticker_24hr)

        # # 获取全市场价格（所有交易对的当前价格）
        # all_prices = client.futures_all_tickers()
        # print("\nAll Market Prices:")
        # print(all_prices)

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get_market_data()
