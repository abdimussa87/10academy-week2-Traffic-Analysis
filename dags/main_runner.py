from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

import os, sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from src.extract_data import get_data
from src.load_data import load_data



# Define the default dag arguments.
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # 'email': ['abdi@gmail.com'],
    # 'email_on_failure': True,
    'email_on_retry': False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=2),
}


# Define the dag, the start date and how frequently it runs.
# I chose the dag to run everday by using 1440 minutes.
with DAG(
    'ETLDag',
    start_date=datetime(2021, 1, 1),
    schedule_interval = '@daily',
    default_args = default_args,
    catchup = False, # only the recent dag will be ran rather than all the dags from start_date till now
    ) as dag:

    # First task is to extract the data from csv into dataframe
    task1 = PythonOperator(
        task_id='extract_data_from_csv',
        provide_context=True,
        python_callable=get_data,
        dag=dag)

    # Second task is to load data into the database.
    task2 = PythonOperator(
        task_id='load_data',
        provide_context=True,
        python_callable=load_data,
        dag=dag)

    # Set task1 "upstream" of task2
    # task1 must be completed before task2 can be started
    task1 >> task2 