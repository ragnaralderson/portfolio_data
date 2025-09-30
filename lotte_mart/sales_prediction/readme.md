# Airflow (Workflow Orchestration)
## Steps:
### Get monthly data.
- On the 1st day of each month, I will get data from the last month.
- Export into datapool. (All-time data is here)

### Retrain with specified model.
- I did exploration to choose the most suitable models. (MAE, RMSE, MAPE)
- Then the best model will be chosen.
- All data in datapool will be trained at each RUN.

### Write Forecasting result.
- After make forecastination from model training, we will get the result.
- Data will be written into AWS S3 for later use.


## Flow:
![alt text]( https://github.com/ragnaralderson/portfolio_data/blob/main/lotte_mart/sales_prediction/airflow_dag.png)


## Sample code
- Code: dag_sales_prediction.py
- This dag show the workflow I use for Sales Prediction.
