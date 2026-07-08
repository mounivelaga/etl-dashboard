from etl.pipeline import ETLPipeline

pipeline = ETLPipeline()

pipeline.run("data/orders.csv")
