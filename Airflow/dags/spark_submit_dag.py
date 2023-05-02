import os
import airflow
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag_spark_submit = DAG(
    dag_id='spark_submit_dag',
    default_args={"retries": 2},
    schedule_interval='0 0 * * *',
    start_date=days_ago(0),
    description='executing spark submit command'
)

WORKING_DIR = str(os.getcwd())
SPARK_SUBMIT_FILE = f"{WORKING_DIR.split('/Training')[0]}/Training/airflow_apis_with_spark_submit/spark_jobs/spark_read_write_job.py"

print("submitting the job")

spark_submit_task = SparkSubmitOperator(
		task_id='spark_submit_task',
		application =SPARK_SUBMIT_FILE,
		conn_id= 'spark_default',
		dag=dag_spark_submit
	)

spark_submit_task

if __name__ == "__main__":
    dag_spark_submit.cli()
