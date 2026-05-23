# ============================================================
# RETANIASCAN-AI MAIN APPLICATION ENGINE
# ============================================================

"""
This file connects:

1. AI inference engine
2. GradCAM explainability engine
3. PDF report generation
4. Medical analysis pipeline

This acts as the central orchestrator
for the complete RetaniaScan-AI system.
"""

# ============================================================
# IMPORTS
# ============================================================

from PIL import Image

# ============================================================
# IMPORT INFERENCE ENGINE
# ============================================================

from app.inference import (

    predict_image
)

# ============================================================
# IMPORT GRADCAM ENGINE
# ============================================================

from app.gradcam import (

    generate_gradcam
)

# ============================================================
# IMPORT PDF REPORT GENERATOR
# ============================================================

from app.report_generator import (

    generate_pdf_report
)

# ============================================================
# RUN COMPLETE RETINAL ANALYSIS
# ============================================================

def analyze_retina(image):

    """
    Complete retinal image analysis pipeline.

    Parameters:
    ----------
    image : PIL.Image

    Returns:
    -------
    result_text : str

    heatmap_image : PIL.Image

    pdf_path : str
    """

    # ========================================================
    # SAVE INPUT RETINA IMAGE
    # ========================================================

    retina_image_path = (
        "outputs/heatmaps/latest_input.png"
    )

    image.save(retina_image_path)

    # ========================================================
    # RUN AI PREDICTION
    # ========================================================

    prediction_result = predict_image(image)

    # ========================================================
    # EXTRACT RESULTS
    # ========================================================

    prediction = (
        prediction_result["prediction"]
    )

    confidence = (
        prediction_result["confidence"]
    )

    second_prediction = (
        prediction_result[
            "second_prediction"
        ]
    )

    second_confidence = (
        prediction_result[
            "second_confidence"
        ]
    )

    risk_level = (
        prediction_result["risk_level"]
    )

    recommendation = (
        prediction_result[
            "recommendation"
        ]
    )

    confidence_status = (
        prediction_result[
            "confidence_status"
        ]
    )

    predicted_class_index = (
        prediction_result[
            "predicted_class_index"
        ]
    )

    # ========================================================
    # GENERATE GRADCAM HEATMAP
    # ========================================================

    overlay_image, heatmap_path = (

        generate_gradcam(

            image,

            predicted_class_index
        )
    )

    # ========================================================
    # GENERATE PDF REPORT
    # ========================================================

    pdf_path = generate_pdf_report(

        prediction_result,

        retina_image_path,

        heatmap_path
    )

    # ========================================================
    # CREATE MEDICAL REPORT TEXT
    # ========================================================

    result_text = f"""

============================================================
RETANIASCAN-AI MEDICAL ANALYSIS REPORT
============================================================

Prediction:
{prediction}

Confidence:
{confidence:.2f}%

Second Likely Class:
{second_prediction} ({second_confidence:.2f}%)

Risk Level:
{risk_level}

Confidence Status:
{confidence_status}

Medical Recommendation:
{recommendation}

============================================================
DISCLAIMER
============================================================

This AI system is designed for educational
and research purposes only.

Please consult a qualified ophthalmologist
for professional medical diagnosis.

============================================================
"""

    # ========================================================
    # CONVERT HEATMAP TO PIL IMAGE
    # ========================================================

    heatmap_image = Image.fromarray(
        overlay_image
    )

    print(
        "Retinal Analysis Completed Successfully!"
    )

    # ========================================================
    # RETURN RESULTS
    # ========================================================

    return (

        result_text,

        heatmap_image,

        pdf_path
    )

# ============================================================
# END OF FILE
# ============================================================