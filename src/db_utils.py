import os,sys
from sqlalchemy import Float, Integer, String, create_engine
import pandas as pd

# Add parent directory to path to import modules from src
rpath = os.getcwd()
if rpath not in sys.path:
    sys.path.append(rpath)

from data_utils import DataUtils

from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")



import logging
import os



class Logger:
    """Logger class for logging messages to a file."""

    def __init__(self, file_name: str='logs.log', level=logging.INFO):
        """Initilize logger class with file name to be written and default log level.
        Args:
            file_name(str): _description_
            basic_level(_type_, optional): _description_. Defaults to logging.INFO.
        """

        path = "../logs"
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)

        # Create a new directory because it does not exist 
        if not isExist:
            os.makedirs(path)

        #  # Gets or creates a logger
        logger = logging.getLogger(__name__)

        logging.basicConfig(filename=f'../logs/{file_name}', encoding='utf-8', level=level,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.logger = logger

    def get_app_logger(self) -> logging.Logger:
        """Return the logger object.
        Returns:
            logging.Logger: logger object.
        """
        return self.logger

class DBUtils:
    def __init__(self):
        self.engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    def insert_vehicle_information_df_to_db(self, vehicle_information_df, table_name):
        vehicle_information_df.to_sql(
            table_name,
            self.engine,
            if_exists='replace',
            index=False,
            chunksize=10000,
            dtype={
                "track_id": Integer,
                "type": String,
                "traveled_d": Float,
                "avg_speed":  Float
            }
        )

    def insert_trajectory_df_to_db(self, trajectory_df, table_name):
         trajectory_df.to_sql(
             table_name,
             self.engine,
             if_exists='replace',
             index=False,
             chunksize=10000,
             dtype={
                "track_id": Integer,
                "lat": Float,
                "lon": Float,
                "speed":  Float,
                "lon_acc":  Float,
                "lat_acc":  Float,
                "time":  Float
            }

         )
        
    def read_data_from_db(self, table_name):
        return pd.read_sql(f"SELECT * FROM {table_name}", self.engine)
    


# add the data to the database
def data_to_db(data_file):
    data_reader = DataUtils()
    db = DBUtils()

    vehicle_df, trajectory_df = data_reader.df_from_csv(data_file)

    db.insert_vehicle_information_df_to_db(vehicle_df,'vehicle_information')
    db.insert_trajectory_df_to_db(trajectory_df,'trajectory_information')



if __name__ == "__main__":
    data_file = '/Users/abdi/Development/10academy/10academy-week2-Traffic-Analysis' + "/data/20181024_d1_0830_0900.csv" 

    data_to_db(data_file)

    print('Data inserted to db successfully')