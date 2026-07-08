from etl.extractor import CSVExtractor
from etl.validator import DataValidator
from etl.transformer import DataTransformer
from etl.loader import DataLoader

extractor = CSVExtractor()
validator = DataValidator()
transformer = DataTransformer()
loader = DataLoader()


data = extractor.extract("data/orders.csv")

errors = validator.validate(data)

if errors:
    print("validation failed")
    for error in errors:
        print(error)
else:
    print("Data validation sucessfull")

    data = transformer.transform(data)

    loader.load(data)
