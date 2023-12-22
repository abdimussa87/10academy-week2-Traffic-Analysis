from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


from dag_src.extract_data import _extract_data_from_csv
from dag_src.load_data import _load_data_to_db
from dag_src.dbt_transformation import _perform_dbt_transformation

from dags import config
dir = config.dir

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
    # default_args = default_args,
    catchup = False, # only the recent dag will be ran rather than all the dags from start_date till now
    ) as dag:

    # First task is to extract the data from csv into dataframe
    task1 = PythonOperator(
        task_id='extract_data_from_csv',
        provide_context=True,
        python_callable=_extract_data_from_csv
       )

    # Second task is to load data into the database.
    task2 = PythonOperator(
        task_id='load_data',
        provide_context=True,
        python_callable=_load_data_to_db
        )
    
    task3 = BashOperator(
        task_id='perform_dbt_transformation',
        bash_command=f'cd {dir}/dbt_traffic_analysis && dbt run'
    )

    # Set task1 "upstream" of task2
    # task1 must be completed before task2 can be started
    task1 >>task2 >> task3