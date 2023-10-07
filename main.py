from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\nx=========================================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    base_model = PrepareBaseModelTrainingPipeline()
    base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\nx=========================================x")
except Exception as e:
    logger.exception(e)
    raise e
