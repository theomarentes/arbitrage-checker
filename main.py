from scripts.scrape import BinanceApi, KucoinApi, BitfinexApi, KrakenApi


print(BinanceApi.get_binance())
print(KucoinApi.get_kucoin())
print(BitfinexApi.get_bitfinex())
print(KrakenApi.get_kraken())