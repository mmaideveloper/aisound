from services.logger_service import get_logger, log_function
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os
import pickle

logger = get_logger("bee-illness-detection")

#model per https://github.com/Shaddyjr/bee-image-classifier/blob/master/code/project_notebook.ipynb
@log_function
def analyze_bee(image_path):
    
    # Load the model, trained on flattened image input of shape (39936,) and size 50x54
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, '..', '..', 'models', 'bee-image-classifier','best_bright.h5')
    model = load_model(model_path)
    
    logger.info(f"Model loaded from {model_path} model shape: {model.input_shape}")
    print(f"Model loaded from {model_path} model shape: {model.input_shape}")

    #p_path = os.path.join(base_dir, '..', '..', 'models', 'bee-image-classifier','bright_model.p')

    #with open(p_path, "rb") as f:
    #    data = pickle.load(f)

    #print(type(data))
    #print(data)


    # Load and preprocess image
    img = Image.open(image_path).convert("RGB").resize((50, 54))
    img_array = np.array(img) / 255.0  # Normalize
    # Model was trained on flattened images

    # Flatten the image to match model input
    # Reshape to match model input: (1, 54, 50, 3)
    img_array = img_array.reshape((1, 54, 50, 3)) 
    # Shape becomes (1, 224*224*3) = (1, 150528)

    
    #img = Image.open(image_path).convert("RGB").resize((224, 224))  # Adjust size to match model input
    #img_array = np.array(img) / 255.0  # Normalize
    #img_array = img_array.reshape((1, 224, 224, 3))  # Add batch dimension

    # Predict
    prediction = model.predict(img_array)
    print("Prediction:", prediction)

    # Get top N predictions
    #top_n = 3
    #top_indices = preds[0].argsort()[-top_n:][::-1]
    #top_scores = preds[0][top_indices]

    # Decode using your .p file
    #labels = data  # assuming data is a dict from the .p file
    #results = [(labels[i], float(top_scores[idx])) for idx, i in enumerate(top_indices)]

    #print("Top predictions:")
    #for label, score in results:
    #    print(f"{label}: {score:.4f}")


    return {
        "prediction_illness": prediction.tolist(),
        "success": True,
        "status": "healthy" if prediction[0].argmax() == 0 else "ill",
        "status_confidence": float(prediction[0].max())
    }
