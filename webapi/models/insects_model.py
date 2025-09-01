from services.logger_service import get_logger, log_function
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model

import numpy as np

logger = get_logger("insect-detection")

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

@log_function
def detect_insect(image_path):

    # Load pretrained EfficientNetB0
    input_tensor = Input(shape=(224, 224, 3))
    model = EfficientNetB0(weights='imagenet', include_top=True, input_tensor=input_tensor)

    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = preprocess_input(x)
    x = np.expand_dims(x, axis=0)

    # Predict using pretrained model
    preds = model.predict(x)

    # Decode top prediction
    decoded = decode_predictions(preds, top=3)[0]  # Top 3 predictions
    for i, (imagenet_id, label, confidence) in enumerate(decoded):
        print(f"{i+1}. {label} ({confidence:.2f})")

    # Return top result
    insect_type, confidence = decoded[0][1], float(decoded[0][2])

    return {
        "type": insect_type,
        "confidence": confidence
    }
