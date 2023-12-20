import os, sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.data_utils import DataUtils

def _extract_data_from_csv():
    data_utils = DataUtils()
    common_df, trajectory_df = data_utils.df_from_csv('/Users/abdi/Development/10academy/10academy-week2-Traffic-Analysis' + "/data/20181024_d1_0830_0900.csv")
    return [common_df, trajectory_df]

