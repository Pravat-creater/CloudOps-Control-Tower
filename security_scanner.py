import subprocess
from incident_logger import log_incident

def check_firewall(cloud):
    try:
        result = subprocess.run(["ufw", "status"], capture_output=True, text=True)

        if "inactive" in result.stdout:
            log_incident(
                cloud,
                "Security",
                "High",
                "Firewall is inactive",
                "Recommendation: Enable UFW firewall",
                "Advisory"
            )
    except:
        pass
