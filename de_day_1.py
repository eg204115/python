# Deduplicate records based on a specified key preseiving order
def dedup_records(records, key):
    seen =set()
    unique_records = []
    for record in records:
        key_value = record[key]
        if key_value not in seen:
            unique_records.append(record)
            seen.add(key_value)
    return unique_records

# Batching an iterable (pagination-style)

def batch(iterable, batch_size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
for chunk in batch(range(10), 3):
    print(chunk)


def batch(iterable, n):
	batch = []
	for item in iterable:
		batch.append(item)
		if len(batch) == n:
			yield batch
			batch = []
	if batch:
		yield batch
for chunk in batch(range(10),3):
 	print(chunk)

# Watermarking: Get the maximum timestamp from a list of records based on a specified timestamp field

from datetime import datetime

def get_watermark(records, timestamp_field, current_watermark=None):
    max_ts = current_watermark
    for record in records:
        ts = record[timestamp_field]
        if max_ts is None or ts > max_ts:
            max_ts = ts
    return max_ts

records = [{"id": 1, "updated_at": datetime(2026, 8, 1)},
           {"id": 2, "updated_at": datetime(2026, 8, 10)}]
print(get_watermark(records, "updated_at"))


import time
import requests

def fetch_with_retry(url, max_retries=3, backoff_base=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:  # rate limited
                wait = backoff_base ** attempt
                time.sleep(wait)
                continue
            raise
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(backoff_base ** attempt)
    raise RuntimeError("Max retries exceeded")