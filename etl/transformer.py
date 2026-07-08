import pandas as pd


class DataTransformer:
    def transform(self, data):
        data["customer_name"] = data["customer_name"].str.strip()

        data["email"] = data["email"].str.lower()

        data["order_date"] = pd.to_datetime(data["order_date"]).dt.strftime("%y-%m-%d")

        return data
