from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from pathlib import Path
import sys
import config

dir = config.dir
env_path = config.env_path
python_path = config.python_path
conda_env_name = config.conda_env_name

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # 'email': ['abdi@gmail.com'],
    # 'email_on_failure': True,
    'email_on_retry': False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id ='load_data_to_db_dag',
    description = "Dag to load data from csv files to database",
    start_date = datetime(2021, 1, 1),
    schedule_interval = None,
    catchup = False,
    default_args = default_args
) as dag:
    run_dbt = BashOperator(
        task_id= "load_data_into_db",
        bash_command = f"/usr/bin/python3 {dir}/src/some_test.py",
        cwd= f"{dir}/src",
    )