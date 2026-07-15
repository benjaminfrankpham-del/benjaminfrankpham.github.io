-- SOC Analytics Case Study
-- SQL Analysis Queries
-- Analyst: Benjamin Pham


--------------------------------------------------
-- Query 1: Total number of alerts
--------------------------------------------------

SELECT

COUNT(*) AS Total_Alerts

FROM soc_alerts;



--------------------------------------------------
-- Query 2: Alert volume by type
--------------------------------------------------

SELECT

Alert_Type,

COUNT(*) AS Alert_Count

FROM soc_alerts

GROUP BY Alert_Type

ORDER BY Alert_Count DESC;



--------------------------------------------------
-- Query 3: Severity distribution
--------------------------------------------------

SELECT

Severity,

COUNT(*) AS Total_Alerts

FROM soc_alerts

GROUP BY Severity

ORDER BY Total_Alerts DESC;



--------------------------------------------------
-- Query 4: Alerts by department
--------------------------------------------------

SELECT

Department,

COUNT(*) AS Alert_Count

FROM soc_alerts

GROUP BY Department

ORDER BY Alert_Count DESC;



--------------------------------------------------
-- Query 5: Analyst workload
--------------------------------------------------

SELECT

Analyst,

COUNT(*) AS Alerts_Handled

FROM soc_alerts

GROUP BY Analyst

ORDER BY Alerts_Handled DESC;



--------------------------------------------------
-- Query 6: Average resolution time
--------------------------------------------------

SELECT

ROUND(AVG(Resolution_Time_Minutes),2) 
AS Avg_Resolution_Minutes

FROM soc_alerts;



--------------------------------------------------
-- Query 7: Resolution time by severity
--------------------------------------------------

SELECT

Severity,

ROUND(AVG(Resolution_Time_Minutes),2)
AS Avg_Resolution_Minutes

FROM soc_alerts

GROUP BY Severity

ORDER BY Avg_Resolution_Minutes DESC;



--------------------------------------------------
-- Query 8: False positive rate
--------------------------------------------------

SELECT

ROUND(
SUM(
CASE
WHEN False_Positive = 'Yes' THEN 1
ELSE 0
END
) * 100.0 / COUNT(*),2)

AS False_Positive_Percentage

FROM soc_alerts;



--------------------------------------------------
-- Query 9: False positives by alert type
--------------------------------------------------

SELECT

Alert_Type,

COUNT(*) AS False_Positive_Count

FROM soc_alerts

WHERE False_Positive = 'Yes'

GROUP BY Alert_Type

ORDER BY False_Positive_Count DESC;



--------------------------------------------------
-- Query 10: Average risk score
--------------------------------------------------

SELECT

ROUND(AVG(Risk_Score),2)

AS Average_Risk_Score

FROM soc_alerts;



--------------------------------------------------
-- Query 11: Critical alerts
--------------------------------------------------

SELECT *

FROM soc_alerts

WHERE Severity = 'Critical'

ORDER BY Risk_Score DESC;



--------------------------------------------------
-- Query 12: Department risk ranking
--------------------------------------------------

SELECT

Department,

COUNT(*) AS Total_Alerts,

ROUND(AVG(Risk_Score),2)
AS Avg_Risk_Score

FROM soc_alerts

GROUP BY Department

ORDER BY Avg_Risk_Score DESC;



--------------------------------------------------
-- Query 13: SLA compliance percentage
--------------------------------------------------

SELECT

ROUND(
SUM(
CASE
WHEN SLA_Met = 'Yes' THEN 1
ELSE 0
END
) * 100.0 / COUNT(*),2)

AS SLA_Percentage

FROM soc_alerts;



--------------------------------------------------
-- Query 14: Alerts by source
--------------------------------------------------

SELECT

Source,

COUNT(*) AS Alert_Count

FROM soc_alerts

GROUP BY Source

ORDER BY Alert_Count DESC;



--------------------------------------------------
-- Query 15: Alert status overview
--------------------------------------------------

SELECT

Status,

COUNT(*) AS Alert_Count

FROM soc_alerts

GROUP BY Status;



--------------------------------------------------
-- Query 16: Monthly alert trends
--------------------------------------------------

SELECT

SUBSTR(Date,1,7) AS Month,

COUNT(*) AS Alert_Count

FROM soc_alerts

GROUP BY Month

ORDER BY Month;



--------------------------------------------------
-- Query 17: Highest risk devices
--------------------------------------------------

SELECT

Device_Name,

ROUND(AVG(Risk_Score),2)
AS Avg_Risk_Score,

COUNT(*) AS Alert_Count

FROM soc_alerts

GROUP BY Device_Name

ORDER BY Avg_Risk_Score DESC

LIMIT 10;



--------------------------------------------------
-- Query 18: Analyst performance
--------------------------------------------------

SELECT

Analyst,

COUNT(*) AS Alerts_Handled,

ROUND(AVG(Resolution_Time_Minutes),2)
AS Avg_Resolution_Time

FROM soc_alerts

GROUP BY Analyst

ORDER BY Avg_Resolution_Time ASC;



--------------------------------------------------
-- Query 19: High severity alert volume
--------------------------------------------------

SELECT

Severity,

COUNT(*) AS High_Risk_Alerts

FROM soc_alerts

WHERE Severity IN ('High','Critical')

GROUP BY Severity;



--------------------------------------------------
-- Query 20: Alert status by severity
--------------------------------------------------

SELECT

Severity,

Status,

COUNT(*) AS Alert_Count

FROM soc_alerts

GROUP BY Severity, Status

ORDER BY Severity;