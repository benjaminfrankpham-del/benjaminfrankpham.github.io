CREATE TABLE customers (

    Customer_ID TEXT PRIMARY KEY,

    Customer_Gender TEXT,

    Senior_Customer TEXT,

    Has_Partner TEXT,

    Has_Dependents TEXT,

    City TEXT,

    State TEXT,

    Zip_Code INTEGER

);



CREATE TABLE accounts (

    Customer_ID TEXT,

    Account_Contract TEXT,

    Payment_Method TEXT,

    Digital_Billing TEXT,

    Customer_Tenure_Months INTEGER,

    FOREIGN KEY(Customer_ID)
    REFERENCES customers(Customer_ID)

);



CREATE TABLE revenue (

    Customer_ID TEXT,

    Monthly_Revenue REAL,

    Lifetime_Revenue REAL,

    Customer_Lifetime_Value INTEGER,

    Revenue_Segment TEXT,

    Customer_Value_Segment TEXT,

    FOREIGN KEY(Customer_ID)
    REFERENCES customers(Customer_ID)

);



CREATE TABLE customer_behavior (

    Customer_ID TEXT,

    Phone_Service TEXT,

    Digital_Service TEXT,

    Security_Product TEXT,

    Backup_Product TEXT,

    Device_Protection TEXT,

    Customer_Support TEXT,

    Entertainment_Service TEXT,

    Media_Service TEXT,

    FOREIGN KEY(Customer_ID)
    REFERENCES customers(Customer_ID)

);



CREATE TABLE churn_analysis (

    Customer_ID TEXT,

    Customer_Churn TEXT,

    Churn_Flag INTEGER,

    Tenure_Category TEXT,

    FOREIGN KEY(Customer_ID)
    REFERENCES customers(Customer_ID)

);