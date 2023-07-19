from scripts.scrape import BinanceApi, KucoinApi, BitfinexApi, KrakenApi, BybitApi, GateApi, PoloniexApi
from scripts.emailer import Emailer


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


class Logic:
    def logic(email_margin, sender_email, receiver_email, sender_password):
    
        print(f"""
| Maximum: ${max(btc_prices)} ({exchanges[btc_prices.index(max(btc_prices))]})
| Minimum: ${min(btc_prices)} ({exchanges[btc_prices.index(min(btc_prices))]})
| Margin: {round(max(btc_prices)/min(btc_prices)*100-100, 2)}%
        """)


        if (round(max(btc_prices)/min(btc_prices)*100-100, 2) > email_margin):
            Emailer.send_email(round(max(btc_prices)/min(btc_prices)*100-100, 2), max(btc_prices), exchanges[btc_prices.index(max(btc_prices))],
                        min(btc_prices), exchanges[btc_prices.index(min(btc_prices))], sender_email, receiver_email, sender_password)


