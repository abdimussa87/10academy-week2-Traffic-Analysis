# 10academy-week2-Traffic-Analysis

Reusable Modular ELT(Extract Load Transform) project for the traffic analysis data consisting of a warehouse using Postgresql, DBT(Data Build Tool) and Airflow.

## Data

The data used can be found from [here](https://open-traffic.epfl.ch/index.php/downloads/#1599231663903-a989d87d-e58d)

## Installation

You'll need Docker to install the packages using:

```bash
pip install -r requirements.txt
```

Then you'll need to initialize airflow using:

```bash
export AIRFLOW_HOME=`pwd`
airflow db init
airflow users create --username username --firstname firstname --lastname lastname --role Admin --email email@domain.com
airflow webserver --port 8080
```

Then you can start airflow scheduler using:

```bash
airflow scheduler
```

## Usage

- Check the notebooks folder for the initial view of the csv data
- Go to 0.0.0.0:8080 to access airflow ui

## License

MIT License

## References

[Installing dbt](https://docs.getdbt.com/dbt-cli/installation/#pip)  
[Videos on dbt](https://www.youtube.com/playlist?list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT)
