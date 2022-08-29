from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta


def get_dag_ids():
    postgres_hook = PostgresHook(postgres_conn_id="airflow_db")
    records = postgres_hook.get_records(sql="select dag_id from dag")
    print(f'the dag id of this test is record with{records}')


with DAG(
    "connect_dag",
    start_date=datetime(2022, 8, 29),
    max_active_runs=1,
    schedule_interval=None,
    catchup=False # enable if you don't want historical dag runs to run
) as dag:

    t1 = PythonOperator(
        task_id="get_dag_nums",
        python_callable=get_dag_ids,
    )
