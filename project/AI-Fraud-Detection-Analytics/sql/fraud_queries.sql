-- ==================================
-- Total Transactions
-- ==================================

SELECT
    COUNT(*) AS total_transactions
FROM transactions;



-- ==================================
-- Fraud Rate
-- ==================================

SELECT

    ROUND(
        AVG(isFraud) * 100,
        2
    ) AS fraud_rate_percentage

FROM transactions;



-- ==================================
-- Fraud by Product
-- ==================================

SELECT

    ProductCD,

    COUNT(*) AS transactions,

    ROUND(
        AVG(isFraud) * 100,
        2
    ) AS fraud_rate

FROM transactions

GROUP BY ProductCD

ORDER BY fraud_rate DESC;



-- ==================================
-- Fraud by Device
-- ==================================

SELECT

    DeviceType,

    COUNT(*) AS transactions,

    ROUND(
        AVG(isFraud) * 100,
        2
    ) AS fraud_rate

FROM transactions

GROUP BY DeviceType;



-- ==================================
-- High Value Fraud Transactions
-- ==================================

SELECT

    TransactionID,

    TransactionAmt,

    ProductCD,

    DeviceType

FROM transactions

WHERE isFraud = 1

ORDER BY TransactionAmt DESC

LIMIT 20;