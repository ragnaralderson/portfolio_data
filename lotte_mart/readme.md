# Client: Lotte Mart
## Data Flow
- Data flow in general: https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/Data%20Flow%20(in%20general).drawio
    + Download the file.
    + Open the browser.
    + Get to: draw.io (You will get redirected)
    + Open this file with draw.io page.

- Data flow example for one project: MKT-Customers.
    + Link: https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/Data Flow (project_MKT_Customers).drawio
    + Do the same steps as the previous one.


## Projects
1. lotte_data_allocation
    - Task: Internal.
    - Use VBA to automatically forming report from raw data.
    - Summarize: projects of team Products, allocation, man-month, etc.
    - Output: Excel file with aggregated/pivoted data.

2. lotte_data_cdp
    - Task: Internal.
    - CDP Foundation on current data from Lotte Mart/ Lotteria.

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
    - Complese flow from DMS (Operation Service) to form Employee Productivity Reports.
    - Content:
        + Operation Performance (store-level) on pick/pack/delivery.
        + Details on each employee.
    - Output: Tableau on Tableau Cloud. (Auto refreshed daily)

6. ops_late_delivery
    - Task: client side.
    - Complese flow from DMS (Operation Service) to form Late Delivery Reports.
    - Content:
        + Stats on last 1 year data on Late Delivery.
        + Late Delivery Rate of each store.
        + Details on each MKT segments.

7. Many others:
    - Input for AWS Personalize.
    - Stats on syncing across systems.
    - Sending reports to MS Teams.
    - Ad-hoc reports: stats on store performance, district delivery, common district & distance from stores, etc.
