# ============================================================
# RETANIASCAN-AI INFERENCE ENGINE
# ============================================================

"""
This file handles:

1. Model loading
2. Image preprocessing
3. AI prediction
4. Confidence scoring
5. Medical recommendations
"""

# ============================================================
# IMPORTS
# ============================================================

import torch
import torch.nn as nn

from torchvision import models
from torchvision import transforms

from PIL import Image

# ============================================================
# IMPORT CONFIGURATION
# ============================================================

from app.config import (

    DEVICE,

    MODEL_PATH,

    NUM_CLASSES,

    IMAGE_SIZE,

    CLASS_NAMES,

    RISK_LEVELS,

    RECOMMENDATIONS,

    CONFIDENCE_THRESHOLD
)

# ============================================================
# IMAGE TRANSFORM PIPELINE
# ============================================================

transform = transforms.Compose([

    transforms.Resize(
        (IMAGE_SIZE, IMAGE_SIZE)
    ),

    transforms.ToTensor(),

    transforms.Normalize(

        mean=[0.485, 0.456, 0.406],

        std=[0.229, 0.224, 0.225]
    )
])

# ============================================================
# LOAD TRAINED EFFICIENTNETB2 MODEL
# ============================================================

def load_model():

    """
    Loads trained EfficientNetB2 model.
    """

    # Create EfficientNetB2
    model = models.efficientnet_b2(
        weights=None
    )

    # Replace classifier
    num_features = (
        model.classifier[1].in_features
    )

    model.classifier = nn.Sequential(

        nn.Dropout(0.4),

        nn.Linear(
            num_features,
            NUM_CLASSES
        )
    )

    # Load trained weights
    model.load_state_dict(

        torch.load(

            MODEL_PATH,

            map_location=DEVICE
        )
    )

    # Move model to device
    model.to(DEVICE)

    # Evaluation mode
    model.eval()

    print(
        "EfficientNetB2 Loaded Successfully!"
    )

    return model

# ============================================================
# LOAD MODEL GLOBALLY
# ============================================================

model = load_model()

# ============================================================
# PREPROCESS IMAGE
# ============================================================

def preprocess_image(image):

    """
    Preprocess uploaded retinal image.

    Parameters:
    ----------
    image : PIL.Image

    Returns:
    -------
    input_tensor : torch.Tensor
    """

    # Convert to RGB
    image = image.convert("RGB")

    # Apply transforms
    input_tensor = transform(image)

    # Add batch dimension
    input_tensor = (
        input_tensor
        .unsqueeze(0)
        .to(DEVICE)
    )

    return input_tensor

# ============================================================
# PREDICT RETINAL IMAGE
# ============================================================

def predict_image(image):

    """
    Predict diabetic retinopathy class.

    Parameters:
    ----------
    image : PIL.Image

    Returns:
    -------
    result : dict
    """

    # Preprocess image
    input_tensor = preprocess_image(image)

    # Disable gradients
    with torch.no_grad():

        # Forward pass
        outputs = model(input_tensor)

        # Convert logits to probabilities
        probabilities = torch.softmax(
            outputs,
            dim=1
        )

        # Get top 2 predictions
        top_probs, top_classes = torch.topk(

            probabilities,

            k=2
        )

    # ========================================================
    # EXTRACT TOP PREDICTION
    # ========================================================

    predicted_class = (
        top_classes[0][0].item()
    )

    second_class = (
        top_classes[0][1].item()
    )

    confidence = (
        top_probs[0][0].item() * 100
    )

    second_confidence = (
        top_probs[0][1].item() * 100
    )

    # ========================================================
    # CONFIDENCE STATUS
    # ========================================================

    if confidence < CONFIDENCE_THRESHOLD:

        confidence_status = (
            "Low Confidence Prediction"
        )

    else:

        confidence_status = (
            "Prediction Confidence Acceptable"
        )

    # ========================================================
    # RETURN RESULTS
    # ========================================================

    result = {

        "prediction": (
            CLASS_NAMES[predicted_class]
        ),

        "confidence": (
            round(confidence, 2)
        ),

        "second_prediction": (
            CLASS_NAMES[second_class]
        ),

        "second_confidence": (
            round(second_confidence, 2)
        ),

        "risk_level": (
            RISK_LEVELS[predicted_class]
        ),

        "recommendation": (
            RECOMMENDATIONS[predicted_class]
        ),

        "confidence_status": (
            confidence_status
        ),

        "predicted_class_index": (
            predicted_class
        )
    }

    return result

# ============================================================
# END OF FILE
# ============================================================