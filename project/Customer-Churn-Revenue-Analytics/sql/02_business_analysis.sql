-- =====================================
-- CUSTOMER CHURN ANALYTICS
-- BUSINESS QUESTIONS
-- =====================================



-- 1. Total Customers

SELECT
    COUNT(*) AS Total_Customers
FROM customers;



-- 2. Overall Churn Rate

SELECT
    Customer_Churn,
    COUNT(*) AS Customer_Count
FROM churn_analysis
GROUP BY Customer_Churn;



-- 3. Monthly Revenue at Risk

SELECT

    SUM(r.Monthly_Revenue) AS Revenue_At_Risk

FROM revenue r

JOIN churn_analysis c

ON r.Customer_ID = c.Customer_ID

WHERE c.Customer_Churn = 'Yes';



-- 4. Churn by Contract Type

SELECT

    a.Account_Contract,

    COUNT(*) AS Total_Customers,

    SUM(
        CASE
            WHEN c.Customer_Churn='Yes'
            THEN 1
            ELSE 0
        END
    ) AS Churned_Customers

FROM accounts a

JOIN churn_analysis c

ON a.Customer_ID=c.Customer_ID

GROUP BY a.Account_Contract;



-- 5. Revenue by Customer Segment

SELECT

    Customer_Value_Segment,

    COUNT(*) AS Customers,

    SUM(Monthly_Revenue) AS Monthly_Revenue

FROM revenue

GROUP BY Customer_Value_Segment;



-- 6. Highest Revenue Customers

SELECT

    Customer_ID,

    Lifetime_Revenue,

    Customer_Lifetime_Value

FROM revenue

ORDER BY Customer_Lifetime_Value DESC

LIMIT 10;