import pandas as pd


class CSVExtractor:
    def extract(self, file_path):
        data = pd.read_csv(file_path)
        return data
