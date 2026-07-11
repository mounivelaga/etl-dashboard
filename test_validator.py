from etl.extractor import CSVExtractor
from etl.validator import DataValidator

extractor = CSVExtractor()
validator = DataValidator()

data = extractor.extract("data/orders.csv")

errors = validator.validate(data)

if errors:
    print("Validation Failed")
    for error in errors:
        print("-", error)
else:
    print("Validation Successful.")
