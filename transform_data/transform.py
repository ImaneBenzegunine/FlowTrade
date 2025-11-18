import json
import csv

# 1️⃣ Load your JSON file
#with open("\transform_data\ev1-messages.json", "r") as f:
with open(r"transform_data\ev1-messages.json", "r") as f:
    data = json.load(f)

# 2️⃣ Prepare CSV columns
header = [
    "requested_timestamp",
    "symbol",
    "name",
    "error",
    "datetime",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "query_timestamp"
]

# 3️⃣ Create CSV file
with open("transform_data\eventhub_flattened.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for event in data:
        body = json.loads(event["body"])   # Parse the body JSON

        requested_ts = body["requested_timestamp"]
        query_ts = body["query_timestamp"]

        for result in body["results"]:
            symbol = result.get("symbol")
            name = result.get("name")
            error = result.get("error", "")

            datetime_ = result.get("datetime", "")
            open_ = result.get("open", "")
            high = result.get("high", "")
            low = result.get("low", "")
            close = result.get("close", "")
            volume = result.get("volume", "")

            # Write row
            writer.writerow([
                requested_ts,
                symbol,
                name,
                error,
                datetime_,
                open_,
                high,
                low,
                close,
                volume,
                query_ts
            ])

print("CSV file generated successfully: eventhub_flattened.csv")
