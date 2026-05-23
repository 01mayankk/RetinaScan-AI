# ============================================================
# RETANIASCAN-AI FASTAPI BACKEND
# ============================================================

"""
FastAPI backend server for RetaniaScan-AI.

Features:
---------
1. Retinal image upload
2. AI diabetic retinopathy prediction
3. GradCAM heatmap generation
4. PDF report generation
5. REST API endpoints
6. Frontend-ready JSON responses
"""

# ============================================================
# IMPORTS
# ============================================================

import io
import base64

from fastapi import (

    FastAPI,

    UploadFile,

    File
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

from PIL import Image

# ============================================================
# IMPORT ANALYSIS PIPELINE
# ============================================================

from app.main import analyze_retina

# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(

    title="RetaniaScan-AI Backend",

    version="1.0.0"
)

# ============================================================
# ENABLE CORS
# ============================================================

# Allows frontend applications
# like React / Vercel frontend
# to communicate with backend.

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=False,

    allow_methods=["*"],

    allow_headers=["*"],
)

# ============================================================
# ROOT ROUTE
# ============================================================

@app.get("/")

def home():

    """
    Health check endpoint.
    """

    return {

        "message":
            "RetaniaScan-AI Backend Running"
    }

# ============================================================
# ANALYZE RETINA ENDPOINT
# ============================================================

@app.post("/analyze")

async def analyze_image(

    file: UploadFile = File(...)
):

    """
    Analyze uploaded retinal image.

    Parameters:
    ----------
    file : UploadFile

    Returns:
    -------
    Structured JSON response
    """

    # ========================================================
    # READ IMAGE
    # ========================================================

    image_bytes = await file.read()

    image = Image.open(

        io.BytesIO(image_bytes)

    ).convert("RGB")

    # ========================================================
    # RUN COMPLETE AI ANALYSIS
    # ========================================================

    report, heatmap_image, pdf_path = (

        analyze_retina(image)
    )

    # ========================================================
    # CLEAN REPORT LINES
    # ========================================================

    lines = report.split("\n")

    cleaned_lines = [

        line.strip()

        for line in lines

        if line.strip()
    ]

    # ========================================================
    # PARSE REPORT VALUES
    # ========================================================

    prediction = cleaned_lines[
        cleaned_lines.index("Prediction:") + 1
    ]

    confidence = cleaned_lines[
        cleaned_lines.index("Confidence:") + 1
    ]

    second_prediction = cleaned_lines[
        cleaned_lines.index(
            "Second Likely Class:"
        ) + 1
    ]

    risk_level = cleaned_lines[
        cleaned_lines.index(
            "Risk Level:"
        ) + 1
    ]

    confidence_status = cleaned_lines[
        cleaned_lines.index(
            "Confidence Status:"
        ) + 1
    ]

    recommendation = cleaned_lines[
        cleaned_lines.index(
            "Medical Recommendation:"
        ) + 1
    ]

    # ========================================================
    # CONVERT HEATMAP IMAGE TO BASE64
    # ========================================================

    buffered = io.BytesIO()

    heatmap_image.save(

        buffered,

        format="PNG"
    )

    heatmap_base64 = base64.b64encode(

        buffered.getvalue()

    ).decode("utf-8")

    # ========================================================
    # RETURN STRUCTURED JSON RESPONSE
    # ========================================================

    return {

        "prediction":
            prediction,

        "confidence":
            confidence,

        "second_prediction":
            second_prediction,

        "risk_level":
            risk_level,

        "confidence_status":
            confidence_status,

        "recommendation":
            recommendation,

        "heatmap_base64":
            heatmap_base64,

        "pdf_report_path":
            pdf_path
    }

# ============================================================
# END OF FILE
# ============================================================