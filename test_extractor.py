from etl.extractor import CSVExtractor

extractor = CSVExtractor()

data = extractor.extract("data/orders.csv")

print(data.head())
print(csv_file_path)
