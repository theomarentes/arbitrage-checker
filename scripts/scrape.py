import requests
import time


class BinanceApi:
    def get_binance_btc():
        params={"symbol": "BTCUSDT"}
        data = requests.get("https://data-api.binance.vision/api/v3/depth", params).json()
        return(round(float(data['bids'][0][0])))
    

class KucoinApi:
    def get_kucoin_btc():
        data = requests.get("https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=BTC-USDT").json()
        return(round(float(data["data"]["bids"][0][0])))


class BitfinexApi:
    def get_bitfinex_btc():
        data = requests.get("https://api-pub.bitfinex.com/v2/ticker/tBTCUSD").json()
        return(round(float(data[6])))
    

class KrakenApi:
    def get_kraken_btc():
        data = requests.get("https://api.kraken.com/0/public/Ticker?pair=XBTUSD").json()
        return(round(float(data["result"]["XXBTZUSD"]["a"][0])))


class BybitApi:
    def get_bybit_btc():
        data = requests.get("https://api-testnet.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSD").json()
        return(data)
    
       
class GateApi:
    def get_gate_btc():
        data = requests.get("https://api.gateio.ws/api/v4/spot/tickers?currency_pair=BTC_USDT").json()
        return(round(float(data[0]["last"])))
    
class PoloniexApi:
    def get_poloniex_btc():
        data = requests.get("https://api.poloniex.com/markets/BTC_USDT/price").json()
        return(round(float(data["price"])))
   