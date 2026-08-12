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
			