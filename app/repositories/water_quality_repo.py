import pandas as pd

class WaterQualityRepository:
    def __init__(self, data_path):
        self.data_path = data_path

    def get_all_data(self):
        data = pd.read_excel(self.data_path)
        # Convert data to list of dictionaries
        return data.to_dict(orient='records')
