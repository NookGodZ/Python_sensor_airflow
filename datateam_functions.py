def python_sensor_check_dagrun_before(target_dag_id: str, target_task_id: str = None):
    """
    This function checks the latest log of the specified DAG and task.

    The result of this function will return only "TRUE". Based on this constant result, 
    you always have to add 'timeout' and 'poke_interval' in your DAG code to return False 
    and make you aware that your DAG has encountered an issue.

    Here's an example of a PythonSensor DAG:

    test_sensor = PythonSensor(
        task_id="test_sensor2",
        python_callable=python_sensor_check_dagrun_before,
        op_kwargs={'target_dag_id': 'Dag_task_d', 'target_task_id': 'task_d'}, ## Sample
        timeout=60,     ## 60 seconds 
        poke_interval=10 ## every 10 seconds
    )

    """

    from airflow.models.dagrun import DagRun
    dag_runs = DagRun.find(dag_id=target_dag_id)
    if target_dag_id and target_task_id : 
        for task_instance in dag_runs[-1].get_task_instances():
            if task_instance.task_id == target_task_id :
                print(f"Task target now state is : {task_instance.state}")
            if task_instance.task_id == target_task_id  and task_instance.state == "success":
                print(f"Task target success ! ")
                return True 

    elif target_dag_id : 
        print(f"Dag target now state is : {dag_runs[-1].state}")
        if dag_runs[-1].state == "success" : 
            print("Dag target success ! ")
            return True