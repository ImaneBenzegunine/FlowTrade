import json
import csv
import os

# 1️⃣ Load your JSON file
with open("ev1-messages.json", "r") as f:
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

# 3️⃣ Ensure folder exists
output_folder = "../data/transformed_data"
os.makedirs(output_folder, exist_ok=True)

# 4️⃣ CSV file path
csv_file_path = os.path.join(output_folder, "eventhub_flattened.csv")

# 5️⃣ Create CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8") as f:
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

print(f"✅ CSV file generated successfully: {csv_file_path}")
