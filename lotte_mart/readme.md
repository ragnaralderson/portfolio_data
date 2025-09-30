# Client: Lotte Mart
## Data Flow (Pipelines and Reports Datasources)
- Data flow in general: 
https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/Data%20Flow%20(in%20general).drawio
    + Download the file.
    + Open the browser.
    + Get to: draw.io (You will get redirected)
    + Open this file with draw.io page.
    + Incase you can't open it:
    ![alt text]( https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/images/Data_Flow_general.png)

- Data flow example for one project: MKT-Customers.
    + Link: https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/Data Flow (project_MKT_Customers).drawio
    + Do the same steps as the previous one.
    + Incase you can't open it:
    ![alt text]( https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/images/Data_Flow_MKT_Part_1.png)
    ![alt text]( https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/images/Data_Flow_MKT_Part_2.png)
    ![alt text]( https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/images/Data_Flow_MKT_Part_3.png)



## Projects
1. lotte_data_allocation
    - Task: Internal.
    - Use VBA to automatically forming report from raw data.
    - Summarize: projects of team Products, allocation, man-month, etc.
    - Output: Excel file with aggregated/pivoted data.

2. lotte_data_cdp
    - Task: client side.
    - Use AWS Glue (with Pyspark) + AWS Worflow to orchestrate ETL Pipelines for CDP Foundation.

3. mkt_customers_demographic
    - Task: client side.
    - Complex flow from OMS data & other sources to form Customers Demographic and Behavior.
    - Content:
        + Stats by segments: nation, gender, age, grade, etc.
        + Stats by MKT segments: Churn, Loyal, Frequent, etc.
        + Change Rate in MKT segments.
        + Distribution of MKT segments in each store.
        + etc.
    - Output: Tableau on Tableau Cloud. (Auto refreshed daily)
    - Example:
    ![alt text](https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/mkt_customers_demographic/CUSTOMERS.png)

4. mkt_promotion
    - Task: client side.
    - Complex flow from OMS data to form Promotion Reports.
    - Content:
        + Promotion (Coupon, Gift, Point) Performance.
        + Redeemtion Rate. (Conversion rate)
    - Output: Tableau on Tableau Cloud. (Auto refreshed daily)

5. ops_employee_productivity
    - Task: client side.
    - Complex flow from DMS (Operation Service) to form Employee Productivity Reports.
    - Content:
        + Operation Performance (store-level) on pick/pack/delivery.
        + Details on each employee.
    - Output: Tableau on Tableau Cloud. (Auto refreshed daily)

6. ops_late_delivery
    - Task: client side.
    - Complex flow from DMS (Operation Service) to form Late Delivery Reports.
    - Content:
        + Stats on last 1 year data on Late Delivery.
        + Late Delivery Rate of each store.
        + Details on each MKT segments.

7. sales_prediction
    - Task: client side.
    - Based on historical data, since 2017, to predict future orders demand.
    - Purpose: Resources (Employee: Picker, Packer, Drivers) Allocation.
    - Content:
        + Apply models: Statistics, Machine Learning, Deep Learning.
        + After using data to train with multiple models.
        + Based on MAE, RMSE and MAPE, Model {Private} (Stats) is good enough for Mart business models.
        + MAPE for each month is under 10%. But in the future, models with external additions might get better result.
        + This is example of MAPE from prediction results from 2024-04 to 2025-08: 
        ![alt text](https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/sales_prediction/mape_from_techniques.png)

8. Basket Analysis.
    - Task: client side.
    - Analyze with category should go with another.
    - For sale boosting by better zones placement on the web.
    - Example on "triggered to buy" categories for "Hot & Cold Tea, Coffee":
    [comment]: #![alt text](https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/basket_analysis/Lift_Tea_n_Coffee.png)

9. Many others:
    - Input for AWS Personalize.
    - Stats on syncing across systems.
    - Sending reports to MS Teams.
    - Ad-hoc reports: stats on store performance, district delivery, common district & distance from stores, etc.
