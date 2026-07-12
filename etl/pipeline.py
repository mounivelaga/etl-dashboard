from etl.extractor import CSVExtractor
from etl.validator import DataValidator
from etl.transformer import DataTransformer
from etl.loader import DataLoader
from utils.logger import logger


class ETLPipeline:
    def __init__(self):
        self.extractor = CSVExtractor()
        self.validator = DataValidator()
        self.transformer = DataTransformer()
        self.loader = DataLoader()

    def run(self, file_path):
        logger.info("ETL Pipeline Started.")
        data = self.extractor.extract(file_path)

        errors = self.validator.validate(data)

        if errors:
            logger.error("Validation failed")

            for error in errors:
                print(error)

            return
        data = self.transformer.transform(data)

        self.loader.load(data)
        logger.info("ETL Pipeline Completed.")
