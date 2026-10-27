
import csv
from datetime import datetime, timedelta
from pathlib import Path

events = []
start = datetime(2026, 10, 27, 10, 0, 0)

def add_event(minutes, seconds, ip, username, status):
    events.append({
        "timestamp": (
            start + timedelta(minutes=minutes, seconds=seconds)
        ).isoformat(),
        "source_ip": ip,
        "username": username,
        "event_type": "login",
        "status": status
    })

# Connexions normales
add_event(0, 0, "192.168.1.10", "alice", "success")
add_event(1, 0, "192.168.1.11", "bob", "success")
add_event(2, 0, "192.168.1.10", "alice", "success")

# Simulation de tentatives de connexion échouées
for i in range(8):
    add_event(3, i * 30, "203.0.113.25", "admin", "failed")

# Une dernière connexion normale
add_event(8, 0, "192.168.1.12", "carol", "success")

with Path("logs.csv").open(
    "w", newline="", encoding="utf-8"
) as file:
    writer = csv.DictWriter(
        file, fieldnames=events[0].keys()
    )
    writer.writeheader()
    writer.writerows(events)

print(f"{len(events)} événements créés dans logs.csv")
