import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

#number of alerts
number_of_alerts = 5000

#list of soc data
alert_types = [
    "Phishing",
    "Failed Login",
    "Malware",
    "Firewall Alert",
    "Data Exfiltration",
    "Privilege Escalation",
]

severity_levels = [
    "Low",
    "Medium",
    "High",
    "Critical",
]

sources = [
    "Email",
    "VPN",
    "Endpoint",
    "Firewall",
    "DLP",
    "Identity Provider",
]

departments = [
    "Finance",
    "Engineering",
    "Human Resources",
    "Operations",
    "Executive"
]

analysts = [
    "Peter",
    "Clark",
    "Bruce",
    "Tony",
    "Steve",
]

statuses = [
    "Resolved",
    "In Progress",
    "Closed",
    
]

data = []

start_date = datetime(2026, 1, 1)

for i in range(number_of_alerts):

    # -------------------------
    # Alert Type (Realistic Distribution)
    # -------------------------
    alert_type = random.choices(
        alert_types,
        weights=[45, 30, 12, 7, 4, 2],
        k=1
    )[0]

    # -------------------------
    # Severity
    # -------------------------
    severity = random.choices(
        severity_levels,
        weights=[55, 28, 13, 4],
        k=1
    )[0]

    # -------------------------
    # Department
    # -------------------------
    department = random.choices(
        departments,
        weights=[18, 50, 8, 20, 4],
        k=1
    )[0]

    # -------------------------
    # Detection Source
    # -------------------------
    if alert_type == "Phishing":
        source = "Email"

    elif alert_type == "Failed Login":
        source = random.choice(["VPN", "Identity Provider"])

    elif alert_type == "Malware":
        source = "Endpoint"

    elif alert_type == "Firewall Alert":
        source = "Firewall"

    elif alert_type == "Data Exfiltration":
        source = "DLP"

    else:
        source = random.choice(sources)

    # -------------------------
    # Resolution Time
    # -------------------------
    if severity == "Low":
        resolution_time = random.randint(15, 40)

    elif severity == "Medium":
        resolution_time = random.randint(45, 90)

    elif severity == "High":
        resolution_time = random.randint(120, 240)

    else:
        resolution_time = random.randint(300, 720)

    # -------------------------
    # Analyst Assignment
    # -------------------------
    if severity == "Critical":

        analyst = random.choices(
            analysts,
            weights=[5, 10, 10, 70, 5],
            k=1
        )[0]

    elif alert_type == "Malware":

        analyst = random.choices(
            analysts,
            weights=[10, 5, 65, 15, 5],
            k=1
        )[0]

    elif alert_type == "Phishing":

        analyst = random.choices(
            analysts,
            weights=[70, 10, 5, 10, 5],
            k=1
        )[0]

    else:

        analyst = random.choice(analysts)

    # -------------------------
    # False Positives
    # -------------------------
    if alert_type == "Failed Login":

        false_positive = random.choices(
            ["Yes", "No"],
            weights=[85, 15],
            k=1
        )[0]

    elif alert_type == "Phishing":

        false_positive = random.choices(
            ["Yes", "No"],
            weights=[55, 45],
            k=1
        )[0]

    elif alert_type == "Firewall Alert":

        false_positive = random.choices(
            ["Yes", "No"],
            weights=[40, 60],
            k=1
        )[0]

    elif alert_type == "Malware":

        false_positive = random.choices(
            ["Yes", "No"],
            weights=[8, 92],
            k=1
        )[0]

    elif alert_type == "Privilege Escalation":

        false_positive = random.choices(
            ["Yes", "No"],
            weights=[2, 98],
            k=1
        )[0]

    else:

        false_positive = random.choices(
            ["Yes", "No"],
            weights=[1, 99],
            k=1
        )[0]

    # -------------------------
    # Status
    # -------------------------
    status = random.choices(
        statuses,
        weights=[65, 10, 25],
        k=1
    )[0]

    # -------------------------
    # Weekday Bias
    # -------------------------
    day_offset = random.choices(
        range(181),
        weights=[
            3 if (start_date + timedelta(days=d)).weekday() < 5 else 1
            for d in range(181)
        ],
        k=1
    )[0]

    alert_date = start_date + timedelta(days=day_offset)

    # -------------------------
    # Business Hour Bias
    # -------------------------
    hour = random.choices(
        range(24),
        weights=[
            1,1,1,1,1,2,3,5,
            10,12,12,12,12,12,
            10,8,8,6,5,3,2,1,1,1
        ],
        k=1
    )[0]

    minute = random.randint(0,59)

    alert_datetime = alert_date.replace(
        hour=hour,
        minute=minute
    )

    # -------------------------
    # Risk Score
    # -------------------------
    if severity == "Low":

        risk_score = random.randint(5,30)

    elif severity == "Medium":

        risk_score = random.randint(31,60)

    elif severity == "High":

        risk_score = random.randint(61,85)

    else:

        risk_score = random.randint(86,100)

    # -------------------------
    # SLA
    # -------------------------
    sla_met = random.choices(
        ["Yes","No"],
        weights=[93,7],
        k=1
    )[0]

    # -------------------------
    # Device
    # -------------------------
    device = f"HOST-{random.randint(1001,1350)}"

    # -------------------------
    # Build Alert
    # -------------------------
    alert = {

        "Alert_ID": i + 1,

        "Date": alert_datetime,

        "Alert_Type": alert_type,

        "Severity": severity,

        "Source": source,

        "Department": department,

        "Analyst": analyst,

        "Resolution_Time_Minutes": resolution_time,

        "False_Positive": false_positive,

        "Risk_Score": risk_score,

        "SLA_Met": sla_met,

        "Device_Name": device,

        "Status": status

    }

    data.append(alert)

df= pd.DataFrame(data)

output_path = Path(__file__).parent.parent / "data" / "soc_alerts.csv"


print(__file__)
print(output_path)

df.to_csv(output_path, index=False)

print("SOC dataset created!")
print(df.head())
