import time

import tensorflow as tf

from CNN_Classifier.config.configuration import PrepareCallbacksConfig


class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = self.config.tensorboard_root_log_dir / f"tb_logs_at_{timestamp}"
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_checkpoint_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )

    def get_tb_checkpoint_callback(self):
        return [self._create_tb_callbacks,
                self._create_checkpoint_callbacks]
