import sys
from pathlib import Path
import os, sys
# Add parent directory to path to import modules from src
rpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if rpath not in sys.path:
    sys.path.append(rpath)

# sys.path.append(str(Path(__file__).parent.parent.parent))
from src.data_utils import DataUtils

def _extract_data_from_csv():
    data_utils = DataUtils()
    vehicle_df, trajectory_df = data_utils.df_from_csv('/Users/abdi/Development/10academy/10academy-week2-Traffic-Analysis' + "/data/20181024_d1_0830_0900.csv")
    return [vehicle_df, trajectory_df]

