import pendulum
import time
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow import DAG

def task_a_callable():
    # Python code for task_a with random wait time between 10 and 15 seconds
    wait_time = 120
    time.sleep(wait_time)
    print()
    print(f"Task_c executed with a random wait time of {wait_time} seconds.")
    print()
default_args = {
    "owner": "panthakij.p",
    "retries": 2,
    "retry_delay": pendulum.duration(minutes=1),
}

with DAG(
    dag_id="Dag_task_d",
    start_date=pendulum.datetime(2024,1, 11,13,22,0, tz="Asia/Bangkok"),
    schedule_interval= '45 13 * * *',
    catchup=False,
    dagrun_timeout=pendulum.duration(hours=1),
    tags=["test", "panthakij.p", "2.0.0"],
    default_args=default_args,
    description="test tasksensor",
) as dag:
    start = EmptyOperator(task_id="Start")
    task_a = PythonOperator(
        task_id="task_d",
        python_callable=task_a_callable,
    )
    end = EmptyOperator(task_id="End")
    
    start >> task_a >> end



### 