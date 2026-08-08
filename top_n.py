# ETL Log Processing
from collections import defaultdict
import heapq

def top_spenders(logs, n=3):
    """
    Parse log lines of format: timestamp,user_id,action,amount
    Return top_n users by total PURCHASE amount, descending.
    """
    spend_by_user = defaultdict(float)

    for log in logs:
        parts = log.strip().split(',')
        if len(parts) != 4:
            continue  # Skip malformed lines
        timestamp, user_id, action, amount_str = parts
        if action == 'PURCHASE':
            try:
                amount = float(amount_str)
                spend_by_user[user_id] += amount
            except ValueError:
                continue  # Skip lines with invalid amount

    # Return the top N users by total purchase amount
    top_spenders= heapq.nlargest(n, spend_by_user.items(), key=lambda x: x[1])
    return top_spenders

logs = [
    "2024-01-01T12:00:00Z,user1,PURCHASE,100.50",
    "2024-01-01T12:05:00Z,user2,PURCHASE,200.00",
    "2024-01-01T12:10:00Z,user1,PURCHASE,50.00",
    "2024-01-01T12:15:00Z,user3,PURCHASE,300.00",
    "2024-01-01T12:20:00Z,user2,PURCHASE,150.00",
    "2024-01-01T12:25:00Z,user4,PURCHASE,400.00",
    "2024-01-01T12:30:00Z,user5,PURCHASE,250.00",
]

top_users = top_spenders(logs, n=3)
print("Top spenders:")