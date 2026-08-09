from datetime import datetime

def deduplicate_latest(records):
    """
    Deduplicate a list of record dicts by 'customer_id',
    keeping only the one with the most recent 'updated_at'.
    """
    latest = {}

    for record in records:
        cust_id = record.get("customer_id")
        updated_at = record.get("updated_at")

        if not cust_id or not updated_at:
            continue  # skip malformed records

        try:
            ts = datetime.fromisoformat(updated_at)
        except ValueError:
            continue  # bad timestamp, skip

        if cust_id not in latest or ts > latest[cust_id]["_ts"]:
            record_copy = record.copy()
            record_copy["_ts"] = ts
            latest[cust_id] = record_copy

    # strip internal helper field before returning
    result = []
    for rec in latest.values():
        rec.pop("_ts")
        result.append(rec)

    return result
records = [
    {"customer_id": "C1", "name": "Alice", "updated_at": "2024-08-01T10:00:00"},
    {"customer_id": "C2", "name": "Bob",   "updated_at": "2024-08-01T09:00:00"},
    {"customer_id": "C1", "name": "Alice T.", "updated_at": "2024-08-02T11:00:00"},
    {"customer_id": "C3", "name": "Carl",  "updated_at": "2024-08-01T08:00:00"},
    {"customer_id": "C2", "name": "Bobby", "updated_at": "2024-08-01T09:30:00"},
]

# --- Example usage ---
result = deduplicate_latest(records)
for r in result:
    print(r)