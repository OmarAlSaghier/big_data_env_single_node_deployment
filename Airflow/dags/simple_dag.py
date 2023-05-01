from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator


with DAG(dag_id="simple_dag", start_date=datetime(2023, 4, 28), schedule="0 0 * * *")as dag:

    hello_task = BashOperator(task_id="Hello_from_bash", bash_command="echo hello from bash")

    @task
    def airflow_task():
        print("hello from airflow task")

    hello_task >> airflow_task()