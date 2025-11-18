from fastapi import FastAPI, Query
from datetime import datetime, timedelta, timezone
import yfinance as yf

app = FastAPI(
    title="Finance Minute Data API",
    description="Fetch minute-level Yahoo Finance data for BTC, ETH, Gold, and NASDAQ 100.",
    version="1.1.0"
)

SYMBOLS = [
    {"symbol": "BTC-USD", "name": "Bitcoin / US Dollar"},
    {"symbol": "ETH-USD", "name": "Ethereum / US Dollar"},
    {"symbol": "GC=F", "name": "Gold Futures (GC=F)"},

]


@app.get("/get_data")
def get_data(timestamp: str = Query(..., description="UTC datetime in format YYYY-MM-DD HH:MM")):
    """
    Fetch minute-level financial data for a specific UTC timestamp.
    Example: /get_data?timestamp=2025-11-05 14:23
    """
    try:
        # Make the datetime UTC-aware
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
    except ValueError:
        return {"error": "Invalid datetime format. Use 'YYYY-MM-DD HH:MM'."}

    start = dt - timedelta(minutes=2)
    end = dt + timedelta(minutes=2)

    results = []
    for item in SYMBOLS:
        symbol = item["symbol"]
        name = item["name"]

        # Fetch 1-minute interval data from Yahoo Finance
        data = yf.download(symbol, start=start, end=end, interval="1m", progress=False)

        if data.empty:
            results.append({
                "symbol": symbol,
                "name": name,
                "error": f"No data found near {timestamp} UTC"
            })
            continue

        # Ensure index is timezone-aware and in UTC
        data.index = data.index.tz_convert("UTC") if data.index.tz else data.index.tz_localize("UTC")

        # Try to get the exact timestamp, else nearest available
        if dt in data.index:
            row = data.loc[dt]
            closest_idx = dt
        else:
            closest_idx = min(data.index, key=lambda x: abs(x - dt))
            row = data.loc[closest_idx]

        results.append({
            "symbol": symbol,
            "name": name,
            "datetime": closest_idx.strftime("%Y-%m-%d %H:%M UTC"),
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        })

    return {"requested_timestamp": timestamp + " UTC", "results": results}



#http://127.0.0.1:8000/get_data?timestamp=2025-11-05%2014:23
