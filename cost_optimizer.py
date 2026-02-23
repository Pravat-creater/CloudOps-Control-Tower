import psutil
from incident_logger import log_incident

LOW_CPU_THRESHOLD = 10

def check_underutilization(cloud):
    cpu = psutil.cpu_percent(interval=1)

    if cpu < LOW_CPU_THRESHOLD:
        log_incident(
            cloud,
            "Cost Optimization",
            "Low",
            f"CPU usage below {LOW_CPU_THRESHOLD}% (Current: {cpu}%)",
            "Recommendation: Consider downsizing instance",
            "Advisory"
        )
