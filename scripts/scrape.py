import requests
import time


class BinanceApi:
    def get_binance():
        params={"symbol": "BTCUSDT"}
        data = requests.get("https://data-api.binance.vision/api/v3/depth", params).json()
        return(round(float(data['bids'][0][0])))
    

class KucoinApi:
    def get_kucoin():
        data = requests.get("https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=BTC-USDT").json()
        return(round(float(data["data"]["bids"][0][0])))


class BitfinexApi:
    def get_bitfinex():
        data = requests.get("https://api-pub.bitfinex.com/v2/ticker/tBTCUSD").json()
        return(round(float(data[6])))
    

class KrakenApi:
    def get_kraken():
        data = requests.get("https://api.kraken.com/0/public/Ticker?pair=XBTUSD").json()
        return(round(float(data["result"]["XXBTZUSD"]["a"][0])))