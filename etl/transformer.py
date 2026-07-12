import pandas as pd

from utils.logger import logger


class DataTransformer:
    def transform(self, data):
        logger.info("Transformation Started.")
        data["customer_name"] = data["customer_name"].str.strip()

        data["email"] = data["email"].str.lower()

        data["order_date"] = pd.to_datetime(data["order_date"]).dt.strftime("%y-%m-%d")

        logger.info("transfermation Sucessfull.")

        return data
