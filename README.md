# CloudOps-Control-Tower
Multi-Cloud Monitoring; Automated Incident Response System
# CloudOps Control Tower  
### Multi-Cloud Reliability, Monitoring & Incident Response Engine (AWS + Azure)

---

## Project Overview

CloudOps Control Tower is a simulated enterprise-grade Cloud Operations monitoring framework designed to proactively monitor, detect, remediate, and document incidents across multi-cloud environments.

This project replicates how IT service organizations manage client cloud infrastructure using structured monitoring, automation, and incident management processes.

The system monitors cloud virtual machines hosted on:

- Amazon Web Services (EC2 – Ubuntu)
- Microsoft Azure (Virtual Machine – Ubuntu)

---

## Problem Statement

In enterprise environments, cloud servers often face:

- High CPU / Memory utilization
- Disk space exhaustion
- Web service failures
- Underutilized instances causing cost waste
- Security misconfigurations
- Manual and reactive monitoring

Most outages happen because monitoring is reactive rather than proactive.

This project solves that problem by implementing:

> A proactive, automated, multi-cloud monitoring and self-healing framework.

---

## Architecture Overview

(Add architecture.png image here)

Architecture Components:

- AWS EC2 (Ubuntu)
- Azure VM (Ubuntu)
- Python-based Monitoring Engine
- Cron Scheduler (runs every 5 minutes)
- Incident Logging Module
- Auto-Healing Engine
- Cost Optimization Detector
- Security Compliance Scanner
- Daily Executive Report Generator

---

## Core Features

### 1. Health Monitoring
- CPU Utilization Tracking
- Memory Usage Monitoring
- Disk Space Monitoring
- Web Server Status Check (Nginx)

---

### 2. Threshold-Based Incident Detection

| Metric | Threshold |
|--------|----------|
| CPU | > 80% |
| Memory | > 85% |
| Disk | > 85% |
| Service Down | Immediate Critical |

Incidents are classified into:
- Low
- Medium
- High
- Critical

---

###  3. Self-Healing Automation
- Automatically restarts failed Nginx service
- Cleans system logs if disk exceeds 90%
- Attempts remediation before escalation
- Logs action taken

This reduces simulated MTTR (Mean Time To Repair).

---

###  4. Cost Optimization Detection
- Detects low CPU utilization (<10%) over extended duration
- Identifies underutilized instances
- Generates optimization recommendations

---

### 5. Security Compliance Scanner
Checks for:
- Open ports (e.g., SSH exposed to public)
- Firewall configuration
- Logging status
- Backup presence (manual validation)

---

### 6. Incident Logging (ITIL-Style)

Example Output:

Incident ID: INC-2026-02-14-001  
Cloud: AWS  
Category: Performance  
Severity: High  
Issue: CPU exceeded 85%  
Auto-Remediation: Restarted nginx  
Final Status: Resolved  
Timestamp: 14-02-2026 18:30 IST  

---

### 7. Daily Executive Report

Sample Summary:

Total Incidents: 5  
Resolved Automatically: 4  
Escalated: 1  
Security Alerts: 2  
Cost Optimization Suggestions: 3  
System Health Score: 92%  

---

##  Cloud Environment Setup

### AWS Setup
- Launched Ubuntu EC2 instance (Free Tier)
- Configured Security Groups (Ports 22 & 80)
- Installed Nginx web server

### Azure Setup
- Created Ubuntu Virtual Machine
- Configured Network Security Group
- Installed Nginx

---

##  Automation Mechanism

Monitoring script is scheduled using Cron:

*/5 * * * * python3 monitor.py

This ensures continuous monitoring every 5 minutes without manual intervention.

---

##  Technologies Used

- Python 3
- psutil
- Linux (Ubuntu)
- Nginx
- CronJobs
- AWS EC2
- Azure Virtual Machine
- GitHub

---

##  Project Structure

CloudOps-Control-Tower/
│
├── monitor.py
├── incident_logger.py
├── security_scanner.py
├── cost_optimizer.py
├── daily_report.py
│
├── outputs/
│   ├── sample_incident.txt
│   └── sample_report.txt
│
├── architecture.png
├── aws_vm.png
├── azure_vm.png
├── script_running.png
├── SOP.pdf
└── README.md

---

## How To Run

1. Install dependencies:
pip install psutil

2. Run monitoring engine:
python3 monitor.py

3. Configure Cron for automation:
crontab -e

Add:
*/5 * * * * python3 /home/ubuntu/monitor.py

---

## Documentation

A detailed Standard Operating Procedure (SOP) document is included covering:

- Architecture
- Incident classification model
- Escalation matrix
- Manual override steps
- Troubleshooting workflow

---

##  Business Impact Simulation

- Reduced simulated downtime through automated remediation
- Improved response time using proactive monitoring
- Increased operational visibility through structured reporting
- Identified cost optimization opportunities
- Enhanced security awareness via compliance checks

---

## Key Concepts Demonstrated

- Multi-Cloud Operations
- Incident Management (ITIL-aligned)
- Self-Healing Infrastructure
- Proactive Monitoring
- Cost Governance
- Security Compliance
- Automation using CronJobs
- MTTR Reduction Strategy

---

##  Future Improvements

- Integrate email alerts
- Add Slack/MS Teams notifications
- Build monitoring dashboard
- Integrate with CloudWatch APIs
- Containerize using Docker
