# ============================================================
# RETANIASCAN-AI CONFIGURATION FILE
# ============================================================

"""
This file contains all global configuration settings
used throughout the RetaniaScan-AI application.

Purpose:
---------
- Centralize important variables
- Avoid hardcoded values
- Make deployment easier
- Improve maintainability
"""

# ============================================================
# IMPORTS
# ============================================================

import torch

# ============================================================
# DEVICE CONFIGURATION
# ============================================================

# Automatically use GPU if available
DEVICE = torch.device(

    "cuda"

    if torch.cuda.is_available()

    else "cpu"
)

# ============================================================
# MODEL CONFIGURATION
# ============================================================

# Path to trained EfficientNetB2 model
MODEL_PATH = (
    "models/efficientnet/"
    "best_efficientnet_b2.pth"
)

# Number of diabetic retinopathy classes
NUM_CLASSES = 5

# Input image size used during training
IMAGE_SIZE = 300

# ============================================================
# CONFIDENCE SETTINGS
# ============================================================

# Minimum confidence threshold
# below which predictions are marked uncertain
CONFIDENCE_THRESHOLD = 65.0

# ============================================================
# CLASS LABELS
# ============================================================

CLASS_NAMES = {

    0: "No DR",

    1: "Mild DR",

    2: "Moderate DR",

    3: "Severe DR",

    4: "Proliferative DR"
}

# ============================================================
# RISK LEVELS
# ============================================================

RISK_LEVELS = {

    0: "Low Risk",

    1: "Mild Risk",

    2: "Moderate Risk",

    3: "High Risk",

    4: "Critical Risk"
}

# ============================================================
# MEDICAL RECOMMENDATIONS
# ============================================================

RECOMMENDATIONS = {

    0: (
        "Routine eye checkup recommended."
    ),

    1: (
        "Monitor condition and consult "
        "an eye specialist if symptoms increase."
    ),

    2: (
        "Clinical ophthalmology consultation "
        "recommended."
    ),

    3: (
        "Immediate specialist attention "
        "recommended."
    ),

    4: (
        "Urgent retinal treatment "
        "consultation required."
    )
}

# ============================================================
# OUTPUT DIRECTORIES
# ============================================================

# GradCAM output directory
HEATMAP_OUTPUT_DIR = (
    "outputs/heatmaps/"
)

# ============================================================
# APPLICATION SETTINGS
# ============================================================

APP_TITLE = "RetaniaScan-AI"

APP_DESCRIPTION = (
    "AI-Powered Diabetic Retinopathy "
    "Detection System"
)

# ============================================================
# END OF CONFIG FILE
# ============================================================