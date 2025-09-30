from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta, date
from utils.sales_prediction import get_monthly_data, model_arima, model_train, write_result 
import os


# DAG args
default_args = {
    'owner': 'tamvo',
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}


# Main Dag run
with DAG(
    default_args = default_args,
    dag_id = 'sales_prediction_v1',
    description = 'Crawl data for monthly prediction',
    start_date = datetime(2025, 1, 9),
    catchup = False,
    schedule = '0 0 1 * *'
) as dag: 
    is_manual = False
    if is_manual:
        start_date = "2025-09-01"
        end_date = "2025-10-01"
    else:
        start_date = (today - timedelta(days=1)).strftime("%Y-%m-01")
        end_date = today.strftime("%Y-%m-01")
    print(f"Start getting data from {start_date} to before {end_date}.")
    

    task1 = PythonOperator(
        task_id = 'get_monthly_data',
        python_callable = get_monthly_data,
        op_kwargs={
            'start_date': start_date, 
            'end_date': end_date
        }
    )
    
    
    task2 = PythonOperator(
        task_id = 'model_train',
        python_callable = model_train,
        op_kwargs={
            'path_data': "output/nsg_sale_data/" 
        }
    )
    
    task3 = PythonOperator(
        task_id = 'write_result',
        python_callable = write_result,
        op_kwargs={
            'predict_month': start_date
        }
    )


    task1 >> task2 >> task3
