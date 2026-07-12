import pandas as pd
from utils.logger import logger


class CSVExtractor:
    def extract(self, file_path):
        logger.info(f"Reading File: {file_path}")
        data = pd.read_csv(file_path)
        logger.info(f"{len(data)} Records extracted.")
        return data
