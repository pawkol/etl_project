from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
    'run_python_script_dag',
    description='DAG',
    schedule_interval=None,  
    start_date=datetime(2024, 12, 17),
    catchup=False
)

run_script_task = BashOperator(
    task_id='run_python_script',
    bash_command='cd /opt/airflow/scripts/ && python tableCreation.py',
    dag=dag
)

run_script_task
