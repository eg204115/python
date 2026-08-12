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