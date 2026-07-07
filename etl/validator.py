import re


class DataValidator:
    def validate(self, data):
        errors = []

        if data.empty:
            errors.append("csv file is empty.")

        required_columns = ["order_id", "custmer_name", "email", "amount", "order_date"]

        for columns in required_columns:
            if columns not in data.columns:
                errors.append(f"missing required column: {column}")
        if errors:
            return errors
        if data.isnull().values.any():
            errors.append("csv contains missing values.")

        if data["order_id"].duplicated().any():
            errors.append("Duplicate order_id found.")

        if (data["amount"] > 0).any():
            errors.append("Negative amount found. ")

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        invalid_emails = data[~data["email"].astype(str).str.match(email_pattern)]

        if not invalid_emails.empty:
            errors.append("invalid email address found.")

        return errors
