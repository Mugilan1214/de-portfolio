from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Step 1: Extracting employee data...")
    print("Loaded 10 employees from CSV")

def clean():
    print("Step 2: Cleaning data...")
    print("Filled missing salaries with mean")
    print("Removed duplicates")

def report():
    print("Step 3: Generating report...")
    print("Engineering: 5 employees")
    print("Marketing: 3 employees")
    print("HR: 2 employees")

with DAG(
    dag_id="employee_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    task2 = PythonOperator(
        task_id="clean",
        python_callable=clean
    )

    task3 = PythonOperator(
        task_id="report",
        python_callable=report
    )

    task1 >> task2 >> task3
