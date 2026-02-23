import os

LOG_FILE = "outputs/incidents.log"
REPORT_FILE = "outputs/sample_report.txt"

def generate_report():
    if not os.path.exists(LOG_FILE):
        print("No incidents logged yet.")
        return

    with open(LOG_FILE, "r") as file:
        logs = file.read()

    total_incidents = logs.count("Incident ID")
    critical_count = logs.count("Critical")
    high_count = logs.count("High")
    medium_count = logs.count("Medium")
    low_count = logs.count("Low")

    report = f"""
Daily Executive Report
------------------------
Total Incidents: {total_incidents}
Critical: {critical_count}
High: {high_count}
Medium: {medium_count}
Low: {low_count}
"""

    with open(REPORT_FILE, "w") as file:
        file.write(report)

    print(report)
