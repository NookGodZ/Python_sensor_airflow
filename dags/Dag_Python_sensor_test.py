import pendulum
import time
from airflow.operators.python import PythonOperator
from airflow.sensors.python import PythonSensor
from airflow import DAG
from datateam_functions import python_sensor_check_dagrun_before
            
def wait_time():
    # Python code for task_a with random wait time between 10 and 15 seconds
    wait_time = 60
    time.sleep(wait_time)
    print()
    print(f"Task_c executed with a wait time of {wait_time} seconds.")
    print()
    
default_args = {
    "owner": "panthakij.p",
    "retries": 2,
    "retry_delay": pendulum.duration(minutes=1),
}
with DAG(
    "Dag_PanthakijP_PythonSensor_TEST",
    start_date=pendulum.datetime(2024,1, 11,13,30,0, tz="Asia/Bangkok"),
    schedule_interval=None,
    catchup=False,
    dagrun_timeout=pendulum.duration(hours=1),
    tags=["test","panthakij.p", "2.0.1"],
    default_args=default_args,
    description="test tasksensor",
) as dag:
    
    test_sensor = PythonSensor(
        task_id = "test_sensor2",
        python_callable = python_sensor_check_dagrun_before,
        op_kwargs={'target_dag_id': 'Dag_task_d','target_task_id':'task_d'},
        timeout=10*60, ## 60 seconds
        poke_interval=60 ## every 20 seconds
    )

    doneD = PythonOperator(
        task_id="task_doneD2",
        python_callable=wait_time,
    )
    
test_sensor >> doneD

    
    
