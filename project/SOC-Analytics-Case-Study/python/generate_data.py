import pandas as pd
import random
from datatime import datatime, timedelta

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
    "Operation",
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
    "In progress",
    "Closed",
    
]

data = []

start_date = datetime(2026,1,1)

for i in range(number_of_alerts):
    alert = {
        "Alert_ID": i + 1,
        "Date": start_date + timedelta(days=random.randint(0,180)),
        "Alert_Type": random.choice(alert_types),
        "Severity": random.choice(severity_levels),
        "Source": random.choice(sources),
        "Department": random.choice(departments),
        "Analyst": random.choice(analysts),
        "Resolution_Time_Minutes": random.randint(10,300),
        "False_Positive": random.choice(["Yes","No"]),
        "Status": random.choice(statuses)
    }

    data.append(alert)

df= pd.DataFrame(data)

df.to_csv(
    "../data/soc_alerts.csv",
    index=False
)

print("SOC dataset created!")
print(df.head())
