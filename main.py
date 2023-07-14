from scripts.scrape import BinanceApi, KucoinApi, BitfinexApi, KrakenApi, BybitApi, GateApi, PoloniexApi


prices = [
    [BinanceApi.get_binance_btc(), "Binance"],
    [KucoinApi.get_kucoin_btc(), "Kucoin"],
    [BitfinexApi.get_bitfinex_btc(), "Bitfinex"],
    [KrakenApi.get_kraken_btc(), "Kraken"],
    [GateApi.get_gate_btc(), "Gate"],
    [PoloniexApi.get_poloniex_btc(), "Poloniex"]
]

btc_prices = [
    BinanceApi.get_binance_btc(), 
    KucoinApi.get_kucoin_btc(), 
    BitfinexApi.get_bitfinex_btc(), 
    KrakenApi.get_kraken_btc(), 
    GateApi.get_gate_btc(), 
    PoloniexApi.get_poloniex_btc(), 
]

exchanges = [
    "Binance",
    "Kucoin",
    "Bitfinex",
    "Kraken",
    "Gate",
    "Poloniex"
]

print(f"Maximum: {max(btc_prices)}, {exchanges[btc_prices.index(max(btc_prices))]}")
print(f"Minimum: {min(btc_prices)}, {exchanges[btc_prices.index(min(btc_prices))]}")
print(f"Margin: {round(max(btc_prices)/min(btc_prices)*100-100, 2)}%")

#print(exchanges[btc_prices.index(max(btc_prices))], max(btc_prices))
#print(exchanges[btc_prices.index(min(btc_prices))], min(btc_prices))
