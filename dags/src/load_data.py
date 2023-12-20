import os, sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from src.db_utils import DBUtils

def _extract_data_from_csv(ti):
    common_df,trajectory_df =  ti.xcom_pull(task_ids='extract_data_from_csv')

    db = DBUtils()
    db.insert_common_information_df_to_db(common_df,'common_information')
    db.insert_trajectory_df_to_db(trajectory_df,'trajectory_information')


