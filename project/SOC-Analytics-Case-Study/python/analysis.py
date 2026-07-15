import pandas as pd
import plotly.express as px
from pathlib import Path

#load the SOC dataset
file_path = Path(__file__).parent.parent / "data" / "soc_alerts.csv"

df = pd.read_csv(file_path)

print(df.head())

#What alerts are generating the most volume?
alert_volume = (
    df["Alert_Type"]
    .value_counts()
    .reset_index()
)

alert_volume.columns = ["Alert_Type", "Count"]



#Which analysts are handling the most alerts?

# Which analysts are handling the most alerts?

analyst_workload = (
    df["Analyst"]
    .value_counts()
    .reset_index()
)

analyst_workload.columns = ["Analyst", "Alerts"]


print("\n" + "=" * 50)
print("         SOC OPERATIONS SUMMARY")
print("=" * 50)

print(f"\n Total Alerts: {len(df):,}")

print(f"\n Most Common Alert Type:")
print(f"   {alert_volume.iloc[0]['Alert_Type']} ({alert_volume.iloc[0]['Count']:,} alerts)")

print(f"\n Top Analyst by Workload:")
print(f"   {analyst_workload.iloc[0]['Analyst']} ({analyst_workload.iloc[0]['Alerts']:,} alerts)")

false_positive_rate = (
    (df["False_Positive"] == "Yes").mean() * 100
)

print(f"\n False Positive Rate:")
print(f"   {false_positive_rate:.1f}%")

average_resolution = df["Resolution_Time_Minutes"].mean()

print(f"\n Average Resolution Time:")
print(f"   {average_resolution:.1f} minutes")

critical_alerts = (
    df["Severity"] == "Critical"
).sum()

print(f"\n Critical Alerts:")
print(f"   {critical_alerts:,}")

print("\n" + "=" * 50)
print("End of Report")
print("=" * 50)


# Capital One-inspired colors
capital_one_colors = [
    "#004977",  # Capital One Blue
    "#D03027",  # Capital One Red
    "#5B9BD5",  # Light Blue
    "#7A8DA6",  # Slate Blue
    "#B0BEC5",  # Light Gray
    "#E8EEF3"   # Very Light Gray
]

fig = px.pie(
    alert_volume,
    names="Alert_Type",
    values="Count",
    hole=0.45,                 # Donut chart
    color="Alert_Type",
    color_discrete_sequence=capital_one_colors
)

fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    pull=[0.03, 0, 0, 0, 0, 0]
)

fig.update_layout(
    title={
        "text": "<b>SOC Alert Distribution</b>",
        "x": 0.5,
        "font": {"size": 24}
    },
    font={
        "family": "Arial",
        "size": 14,
        "color": "#1F2937"
    },
    paper_bgcolor="white",
    plot_bgcolor="white",
    legend_title="Alert Type",
    margin=dict(t=80, b=20, l=20, r=20)
)

fig.show()