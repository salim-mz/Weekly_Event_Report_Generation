# Weekly Event Report Generation for Mtouch

## Project Overview
This project was developed to generate a weekly report for Mtouch, a client specializing in organizing online events for healthcare stakeholders such as doctors, pharmacists, and labs. The report provides an overview of the events conducted in the past week and insights into their success or failure.

## Tools and Technologies
- **Python**: For data analysis and manipulation.
- **Pandas**: For data processing.
- **Regular Expressions (re)**: For data cleaning.
- **Openpyxl**: For Excel report generation.
- **Apache Airflow**: For scheduling and automating the report generation process.

## Project Structure
```
Weekly_Event_Report_Generation/
│
├── README.md
├── requirements.txt
├── data/
│   └── sample_data.json
├── dags/
│   ├── report_generation_dag.py
│   └── __init__.py
├── scripts/
│   ├── fetch_data.py
│   ├── process_data.py
│   ├── generate_report.py
│   └── __init__.py
├── tests/
│   ├── test_fetch_data.py
│   ├── test_process_data.py
│   ├── test_generate_report.py
│   └── __init__.py
├── config/
│   ├── airflow.cfg
│   └── __init__.py
└── utils/
    ├── api_client.py
    ├── data_transformer.py
    ├── report_writer.py
    └── __init__.py
```


## Setup Instructions
1. Clone the repository:

git clone https://github.com/yourusername/Weekly_Event_Report_Generation.git

2. Navigate to the project directory:

cd Weekly_Event_Report_Generation

3. Install the required dependencies:

pip install -r requirements.txt

4. Configure Airflow:

export AIRFLOW_HOME=$(pwd)/config
airflow db init
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

5. Start the Airflow web server:

airflow webserver --port 8080

6. Start the Airflow scheduler in a new terminal:
airflow scheduler


## Notes
All data and credentials used in this project are fake and created for the purpose of this portfolio.
The sample data provided in the data/sample_data.json file is used to demonstrate the project's functionality.

## Project Contributions
Data Consumption
Consuming data from the Bigmaker API, which contains information about the online events organized by Mtouch.

Data Analysis and Arrangement
Using Python, Pandas, Regular Expressions (re), and Openpyxl, the data is analyzed and arranged to extract relevant information for the report.

Report Generation
Utilizing Airflow, the weekly report is scheduled to be generated and automatically delivered to Mtouch on a regular basis.

## Impact
The weekly event report provides Mtouch with an overview of the past week's events and insights into their success or failure, allowing them to evaluate the effectiveness of their online events and make data-driven decisions to improve future events.
