mport psutil
import subprocess
from incident_logger import log_incident
from security_scanner import check_firewall
from cost_optimizer import check_underutilization
from daily_report import generate_report

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 85
CLOUD_PROVIDER = "AWS"  # Change to Azure if needed

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        log_incident(
            CLOUD_PROVIDER,
            "Performance",
            "High",
            f"CPU exceeded {CPU_THRESHOLD}% (Current: {cpu}%)",
            "No auto-remediation configured",
            "Logged"
        )

def check_memory():
    memory = psutil.virtual_memory().percent
    if memory > MEMORY_THRESHOLD:
        log_incident(
            CLOUD_PROVIDER,
            "Performance",
            "Medium",
            f"Memory exceeded {MEMORY_THRESHOLD}% (Current: {memory}%)",
            "No auto-remediation configured",
            "Logged"
        )

def check_disk():
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        log_incident(
            CLOUD_PROVIDER,
            "Storage",
            "High",
            f"Disk exceeded {DISK_THRESHOLD}% (Current: {disk}%)",
            "Recommendation: Clean logs",
            "Logged"
        )

def check_nginx():
    status = subprocess.run(
        ["systemctl", "is-active", "nginx"],
        capture_output=True,
        text=True
    )

    if "inactive" in status.stdout:
        subprocess.run(["sudo", "systemctl", "restart", "nginx"])
        log_incident(
            CLOUD_PROVIDER,
            "Service",
            "Critical",
            "Nginx service was down",
            "Restarted nginx",
            "Resolved"
        )

def main():
    print("Starting CloudOps Monitoring Engine...\n")

    check_cpu()
    check_memory()
    check_disk()
    check_nginx()
    check_underutilization(CLOUD_PROVIDER)
    check_firewall(CLOUD_PROVIDER)
    generate_report()

    print("Monitoring cycle completed.\n")

if __name__ == "main":
    main()
