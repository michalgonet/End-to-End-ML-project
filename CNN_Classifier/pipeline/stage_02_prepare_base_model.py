from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.modules.prepare_base_model import PrepareBaseModel
from CNN_Classifier import logger

STAGE_NAME = "Data Ingestion stage"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()
        base_model_config = config.get_prepare_base_model_config()
        base_model = PrepareBaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
