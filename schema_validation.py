import re
from datetime import datetime

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validate_records(records, schema):
    """
    Validate records against a schema (field -> expected type).
    Adds extra checks for email format and date format.
    Returns (valid_records, invalid_records_with_reasons).
    """
    valid = []
    invalid = []

    for record in records:
        errors = []

        # 1. Required field + type checks
        for field, expected_type in schema.items():
            if field not in record:
                errors.append(f"missing field: {field}")
                continue
            if not isinstance(record[field], expected_type):
                errors.append(
                    f"wrong type for {field}: expected {expected_type.__name__}, "
                    f"got {type(record[field]).__name__}"
                )

        # 2. Email format check (only if present and right type)
        if "email" in record and isinstance(record["email"], str):
            if not EMAIL_PATTERN.match(record["email"]):
                errors.append("invalid email format")

        # 3. Date format check
        if "signup_date" in record and isinstance(record["signup_date"], str):
            try:
                datetime.strptime(record["signup_date"], "%Y-%m-%d")
            except ValueError:
                errors.append("invalid signup_date format, expected YYYY-MM-DD")

        if errors:
            invalid.append({"record": record, "errors": errors})
        else:
            valid.append(record)

    return valid, invalid


# --- Example usage ---
valid, invalid = validate_records(records, schema)

print("VALID:")
for r in valid:
    print(" ", r)

print("\nINVALID:")
for r in invalid:
    print(" ", r["record"], "->", r["errors"])