import requests
from config import API_KEY, FOREX_PAIRS

def generate_signal():
    url = "https://api.twelvedata.com/time_series"
    signals = []

    for pair in FOREX_PAIRS:
        params = {
            "symbol": pair,
            "interval": "1min",
            "apikey": API_KEY,
            "outputsize": 5
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            try:
                close_prices = [float(candle["close"]) for candle in data["values"]]
                if close_prices[0] > close_prices[1] > close_prices[2]:
                    signals.append(f"🔼 BUY Signal for {pair}")
                elif close_prices[0] < close_prices[1] < close_prices[2]:
                    signals.append(f"🔻 SELL Signal for {pair}")
            except:
                continue
    return "\n".join(signals) if signals else None