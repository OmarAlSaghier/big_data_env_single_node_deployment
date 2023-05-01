# Run Airflow with Python Virtual Environments
Ref: https://www.youtube.com/watch?v=z7xyNOF8tak


### Change directory into `Airflow_virtual_venv` directory

* Create virtual environment
```
$ python3 -m venv airflow_venv
```

* Start the venv
```
$ source airflow_venv/bin/activate
```

* From the official github repo:
https://github.com/apache/airflow

Install airflow using the below command
make sure to change the **"`constraints-3.xx`"** to your python version
```
$ pip install 'apache-airflow==2.5.0' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.10.txt"
 ```

* After installation, export `AIRFLOW_HOME` to the desired directory
```
$ export AIRFLOW_HOME=$(pwd)/airflow_venv
```

* Initialize the database with:
```
$ airflow db init
```

* Check db connection using:
```
$ airflow db check
```

* Start Airflow webserver:
```
$ airflow webserver -p 8080
```

* Open another terminal window: 
    * Change your directory into AIRFLOW directory if not
    * Source into your virtual environment
    * Export airflow home by "`export AIRFLOW_HOME=$(pwd)/airflow_venv`"
    * And Create a user for logging into airflow by:
```
$ airflow users create \
    --username airflow \
    --firstname fname \
    --lastname lname \
    --email admin@domain.com \
    --role Admin
```

* In the new terminal window, start airflow scheduler
```
$ airflow scheduler
```

* Create a new folder inside the `airflow_venv` called **"`dags`"**. Inside it, create a new testing dag file called **"`simple_dag.py`"**, with the below content:
```
from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(dag_id="simple_dag", start_date=datetime(2023, 2, 1), schedule="0 0 * * *")as dag:

    hello_task = BashOperator(task_id="Hello_from_bash", bash_command="echo hello from bash")

    @task
    def airflow_task():
        print("hello from airflow task")

    hello_task >> airflow_task()
```

****

### To Rerun Airflow Again After the First Setup
* Terminal window 1:
```
$ export AIRFLOW_HOME=$(pwd)/airflow_venv
$ airflow webserver -p 8080
```
* Terminal window 2:
```
$ export AIRFLOW_HOME=$(pwd)/airflow_venv
$ airflow scheduler
```
