# Client: Neyu Corporation
## Data Flow (Pipelines and Datasources)
- Data flow in general: 
https://github.com/ragnaralderson/portfolio_data/blob/main/neyu/Data_Infrastructure_20260910.drawio
    + Download the file.
    + Open the browser.
    + Get to: draw.io (You will get redirected)
    + Open this file with draw.io page.
    + Incase you can't open it, I just seperate the DrawIO file into pieces as below.


## Responsibility
- First of all, about infrastructure, You can view this following diagram: https://github.com/ragnaralderson/portfolio_data/blob/main/neyu/Data_Infrastructure_20260910.drawio


1. Topics for Kafka Connectors.
    - We have many seperate Database for each countries (currently: 7). I will create topics for Kafka Connectors to capture CDC as records.
    - Dev-ops will setup MirrorMaker2 to centralize these topics for me. From Kafka Standalone to Kafka Central only.
    ![alt text](https://github.com/ragnaralderson/portfolio_data/blob/main/neyu/images/topics_for_kafka_connectors.png)


2. Consume CDC data.
    - On Processing Server, I set consumers to digest exact topics as configed in python scripts. From Kafka Central to Data Warehouse.
    - These streamed data will applied into Data Warehouse in real-time.
    ![alt text](https://github.com/ragnaralderson/portfolio_data/blob/main/neyu/images/data_digest.png)


3. Data Orchestration.
    - We use Dagster (old version & already setup by previous Data Engineers) to orchestrate data flow.

    - Scraping.
        + Beside Operation data from 7 countries above. 
        + I also get data from: Google Sheet, SharePoint, 3rd-party Portals to unify into Data Warehouse.

    - Aggregation.
        + Data Analysts will need to aggregate raw data to form datamarts. I will setup these scripts and utils for them to actively work on their own.
        + Example: Materialized Views are prefered by DAs in my team. I left utils with examples for them. Then, they just need to work on that by themself.


4. Reporting.
    - I also involving in some Reports Building: Telegram reports, Email reports. DAs give me logic, then I form data as give template.


5. The rest of Data Flow. (Just to be clear)
    - Dev-ops will sync from Data Warehouse into "Report Read Database" only to reduce workload for our Data Warehouse.


6. Debug and Data Quality Control.
    - Alert Mechanisms will always be applied for parts of my responsibility.
    - Some parts, like Connectors State checking on Debezium servers, these will be setup by Dev-ops. MirrorMaker2 state. etc.
    - Sometimes, I will involve by DAs' requests on Data Quality check.
