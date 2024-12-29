from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    'warsaw_data_update_dag',
    description='DAG',
    schedule_interval='*/10 8-16 * * *',
    start_date=datetime(2024, 12, 17), 
    catchup=False
) as dag:
    run_script_task = BashOperator(
        task_id='warsaw_data_update_dag_script',
        bash_command='cd /opt/airflow/scripts/ && python warsawUpdate.py'
    )


