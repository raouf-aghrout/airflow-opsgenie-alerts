from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from an_opsgenie_hook import opsgenie_hook

dag = DAG('eternal_failure')

task_that_always_fails = BashOperator(
    task_id='task_that_always_fails',
    bash_command='exit 1',
    on_failure_callback=opsgenie_hook,
    dag=dag,
)
