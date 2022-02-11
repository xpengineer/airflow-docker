# We'll start by importing the DAG object
from datetime import timedelta

from airflow import DAG
# We need to import the operators used in our tasks
from airflow.operators.python_operator import PythonOperator
# We then import the days_ago function
from airflow.utils.dates import days_ago

from airflow.utils.helpers import chain
#from airflow.models.baseoperator import chain


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(5)
}

xp_dag = DAG(
    'xp_chain_dag',
    default_args=default_args,
    description='xp testing',
    schedule_interval=timedelta(hours=1),
    catchup=False
)


def xp_func(task_id):
    print(f"in {task_id}")


t0 = PythonOperator(
    task_id='t0',
    op_args=["t0"],
    python_callable=xp_func,
    dag=xp_dag,
)

t1 = PythonOperator(
    task_id='t1',
    op_args=["t1"],
    python_callable=xp_func,
    dag=xp_dag,
)

t2 = PythonOperator(
    task_id='t2',
    op_args=["t2"],
    python_callable=xp_func,
    dag=xp_dag,
)

t11 = PythonOperator(
    task_id='t11',
    op_args=["t11"],
    python_callable=xp_func,
    dag=xp_dag,
)

t12 = PythonOperator(
    task_id='t12',
    op_args=["t12"],
    python_callable=xp_func,
    dag=xp_dag,
)

t21 = PythonOperator(
    task_id='t21',
    op_args=["t21"],
    python_callable=xp_func,
    dag=xp_dag,
)

t22 = PythonOperator(
    task_id='t22',
    op_args=["t22"],
    python_callable=xp_func,
    dag=xp_dag,
)


# chain(t1, [t11, t12])
# chain(t2, [t21, t22])
chain(t0, t1, [t11, t12])
chain(t0, t2, [t21, t22])
