import pandas as pd

class DataUtils:
    def __init__(self):
        pass

    def df_from_csv(self, file_path):
        delimiter = ';'

        with open(file_path, 'r') as file:
            lines = file.readlines()
            # lines = lines[1:]
            common_information = []
            trajectory_information = []
                # jumping the first line which is the header ['track_id', ' type', ' traveled_d', ' avg_speed', ' lat', ' lon', ' speed', ' lon_acc', ' lat_acc', ' time']
            lines = lines[1:]
            for line in lines:
                # removing the \n at the end of the line
                line = line.strip('\n').strip(' ')
                contents = line.split(delimiter)
                # removing the white spaces
                contents = [contents[i].strip() for i in range(len(contents))]

                common_information.append(contents[:4])

                k = 4 # skipping the first 4 columns which are track_id, type, traveled_d, avg_speed
                for i in range(k, len(contents),6):
                    # concatenating the track_id with the trajectory information
                    trajectory_information.append([contents[0],*contents[i:i+6]])

        df_common = pd.DataFrame(data= common_information,columns=['track_id','type','traveled_d','avg_speed'])
        df_trajectory = pd.DataFrame(data= trajectory_information ,columns=['track_id','lat','lon','speed','lon_acc','lat_acc','time'])

        # dropping any rows with NaN values
        df_trajectory.dropna(subset=['lat','lon','speed','lon_acc','time'],inplace=True)
        
        return df_common, df_trajectory

