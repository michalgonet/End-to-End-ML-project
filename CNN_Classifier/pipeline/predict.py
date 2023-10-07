from pathlib import Path

import numpy as np
import tensorflow as tf


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = tf.keras.models.load_model(Path("artifacts/training/model.h5"))
        image_name = self.filename
        test_image = tf.keras.preprocessing.image.load_img(image_name, target_size=(244, 244))
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = "Healthy"
        else:
            prediction = "Coccidiosis"

        return [{"image": prediction}]
