# ============================================================
# RETANIASCAN-AI GRADCAM ENGINE
# ============================================================

"""
This file handles:

1. GradCAM generation
2. Heatmap overlay creation
3. Explainability visualization
4. Heatmap saving
"""

# ============================================================
# IMPORTS
# ============================================================

import os
import numpy as np

from PIL import Image

import matplotlib.cm as cm

from pytorch_grad_cam import GradCAM

from pytorch_grad_cam.utils.image import (
    show_cam_on_image
)

# ============================================================
# IMPORT MODEL + CONFIG
# ============================================================

from app.inference import (

    model,

    preprocess_image
)

from app.config import (

    IMAGE_SIZE,

    HEATMAP_OUTPUT_DIR
)

# ============================================================
# CREATE OUTPUT DIRECTORY
# ============================================================

os.makedirs(

    HEATMAP_OUTPUT_DIR,

    exist_ok=True
)

# ============================================================
# TARGET LAYER FOR GRADCAM
# ============================================================

# Last convolutional feature layer
target_layer = model.features[-1]

# ============================================================
# GENERATE GRADCAM HEATMAP
# ============================================================

def generate_gradcam(

    image,

    predicted_class
):

    """
    Generate GradCAM heatmap.

    Parameters:
    ----------
    image : PIL.Image

    predicted_class : int

    Returns:
    -------
    overlay_image : numpy.ndarray

    heatmap_path : str
    """

    # ========================================================
    # PREPROCESS IMAGE
    # ========================================================

    input_tensor = preprocess_image(image)

    # ========================================================
    # CREATE GRADCAM OBJECT
    # ========================================================

    cam = GradCAM(

        model=model,

        target_layers=[target_layer]
    )

    # ========================================================
    # GENERATE HEATMAP
    # ========================================================

    grayscale_cam = cam(

        input_tensor=input_tensor
    )

    grayscale_cam = grayscale_cam[0]

    # ========================================================
    # RESIZE ORIGINAL IMAGE
    # ========================================================

    resized_image = image.resize(

        (IMAGE_SIZE, IMAGE_SIZE)
    )

    # Convert to numpy
    rgb_image = (
        np.array(resized_image)
        .astype(np.float32)
        / 255.0
    )

    # ========================================================
    # CREATE OVERLAY VISUALIZATION
    # ========================================================

    overlay_image = show_cam_on_image(

        rgb_image,

        grayscale_cam,

        use_rgb=True
    )

    # ========================================================
    # SAVE HEATMAP
    # ========================================================

    heatmap_path = os.path.join(

        HEATMAP_OUTPUT_DIR,

        "latest_gradcam.png"
    )

    # Convert to PIL image
    overlay_pil = Image.fromarray(
        overlay_image
    )

    # Save image
    overlay_pil.save(heatmap_path)

    print(
        "GradCAM Heatmap Generated Successfully!"
    )

    return overlay_image, heatmap_path

# ============================================================
# END OF FILE
# ============================================================