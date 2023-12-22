import sys
import os
import os, sys

# Add parent directory to path to import modules from src
rpath = os.getcwd()
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from dags import config

dir = config.dir
def _perform_dbt_transformation():
    return f'cd {dir}/traffic_analysis && dbt run'