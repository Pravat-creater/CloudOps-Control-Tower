import datetime

INCIDENT_LOG_FILE = "outputs/incidents.log"

def log_incident(cloud, category, severity, issue, action, status):
    incident_id = "INC-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"""
Incident ID: {incident_id}
Cloud: {cloud}
Category: {category}
Severity: {severity}
Issue: {issue}
Action Taken: {action}
Status: {status}
Timestamp: {timestamp}
-------------------------------------------
"""

    with open(INCIDENT_LOG_FILE, "a") as file:
        file.write(log_entry)

    print(log_entry)
