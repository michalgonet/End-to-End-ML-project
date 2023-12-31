from CNN_Classifier.constants import *
from CNN_Classifier.utils.common import read_yaml, create_directories
from CNN_Classifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig, \
    TrainingConfig, EvaluationConfig


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath),
        self.params = read_yaml(params_filepath)
        create_directories([self.config[0].artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config[0].data_ingestion
        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config[0].prepare_base_model

        create_directories([config.root_dir])

        return PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config[0].prepare_callbacks
        model_checkpoint_dir = Path(config.checkpoint_model_filepath).parent
        create_directories([
            Path(model_checkpoint_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        return PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )

    def get_training_config(self) -> TrainingConfig:
        training = self.config[0].training
        prepare_base_model = self.config[0].prepare_base_model
        params = self.params
        training_data = Path(self.config[0].data_ingestion.unzip_dir) / UNZIP_FOLDER_NAME
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config

    def get_validation_config(self) -> EvaluationConfig:
        return EvaluationConfig(
            path_to_model=Path("artifacts/training/model.h5"),
            training_data=Path("artifacts/data_ingestion/Chicken-fecal-images"),
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
