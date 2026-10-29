"""
fetch_flunet.py
Fetch WHO FluNet case-reporting data via the public xMART API.
Outputs: data/raw/flunet_raw.csv

No account required. Data is publicly licensed under CC BY-NC-SA 3.0 IGO.
API docs: https://xmart-api-public.who.int/FLUMART/VIW_FNT
"""

import json
import time
import pathlib
import requests
import pandas as pd

RAW_DIR = pathlib.Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://xmart-api-public.who.int/FLUMART/VIW_FNT"
PAGE_SIZE = 1000  # API maximum


def fetch_page(skip: int) -> dict:
    params = {
        "$format": "json",
        "$top": PAGE_SIZE,
        "$skip": skip,
    }
    resp = requests.get(BASE_URL, params=params, timeout=60)
    resp.raise_for_status()
    return resp.json()


def fetch_all() -> pd.DataFrame:
    records = []
    skip = 0
    while True:
        print(f"  fetching rows {skip}–{skip + PAGE_SIZE}...")
        data = fetch_page(skip)
        batch = data.get("value", [])
        if not batch:
            break
        records.extend(batch)
        skip += PAGE_SIZE
        time.sleep(0.5)  # be a polite client
    return pd.DataFrame(records)


def main():
    print("Fetching WHO FluNet data...")
    df = fetch_all()
    print(f"  {len(df):,} rows retrieved")

    out_path = RAW_DIR / "flunet_raw.csv"
    df.to_csv(out_path, index=False)
    print(f"  saved → {out_path}")

    # Save metadata
    meta = {
        "source": "WHO FluNet xMART API",
        "url": BASE_URL,
        "rows": len(df),
        "columns": list(df.columns),
        "fetch_date": pd.Timestamp.now().isoformat(),
    }
    with open(RAW_DIR / "flunet_meta.json", "w") as f:
        json.dump(meta, f, indent=2)
    print(f"  metadata saved → {RAW_DIR / 'flunet_meta.json'}")


if __name__ == "__main__":
    main()
