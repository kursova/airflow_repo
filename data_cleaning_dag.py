from airflow import DAG
from airflow.operators.ssh import SSHOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 1),
    'retries': 1,
}

with DAG('data_cleaning_dag', default_args=default_args, schedule_interval=None) as dag:
    clean_data_task = SSHOperator(
        task_id='run_clean_data_script',
        ssh_conn_id='spark_ssh',
        command="python /dataops/clean_data.py",
    )