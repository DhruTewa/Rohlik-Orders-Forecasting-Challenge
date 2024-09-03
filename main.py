from rohlik_forecasting import logger
from rohlik_forecasting.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "STAGE 01: DATA INGESTION"

try:
    logger.logging.info(f"Starting {STAGE_NAME}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.logging.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.logging.exception(e)
    raise e