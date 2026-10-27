
import pandas as pd

WINDOW = pd.Timedelta(minutes=5)
THRESHOLD = 5


def detect_brute_force(logs):
    logs = logs.copy()

    logs["timestamp"] = pd.to_datetime(
        logs["timestamp"],
        errors="coerce",
        utc=True
    )

    logs = logs.dropna(
        subset=["timestamp", "source_ip", "status"]
    )

    failed = logs[
        (logs["event_type"] == "login")
        & (logs["status"] == "failed")
    ]

    alerts = []

    for ip, group in failed.groupby("source_ip"):
        group = group.sort_values("timestamp")
        times = group["timestamp"].tolist()
        left = 0

        for right, current_time in enumerate(times):
            while current_time - times[left] > WINDOW:
                left += 1

            count = right - left + 1

            if count == THRESHOLD:
                alerts.append({
                    "timestamp": current_time.isoformat(),
                    "source_ip": ip,
                    "rule": "BRUTE_FORCE_SUSPECT",
                    "severity": "HIGH",
                    "count_5min": count,
                    "description": (
                        f"{count} echecs en 5 minutes ou moins"
                    )
                })

    return pd.DataFrame(alerts)


if __name__ == "__main__":
    logs = pd.read_csv("logs.csv")
    alerts = detect_brute_force(logs)

    print("\n--- Resultat de l'analyse ---")
    print("Nombre d'alertes :", len(alerts))

    if alerts.empty:
        print("Aucune alerte detectee.")
    else:
        print(alerts.to_string(index=False))

    alerts.to_csv("alerts.csv", index=False)
    print("\nRapport enregistre dans alerts.csv")
