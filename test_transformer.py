from etl.extractor import CSVExtractor
from etl.transformer import DataTransformer

extractor = CSVExtractor()

transformer = DataTransformer()

data = extractor.extract("data/orders.csv")


print("Before transformation.")
print(data)

data = transformer.transform(data)

print("\n afyer transformation.")
print(data)
