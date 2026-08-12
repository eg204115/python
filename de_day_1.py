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
			