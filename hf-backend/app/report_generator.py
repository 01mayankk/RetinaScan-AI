# ============================================================
# RETANIASCAN-AI PDF REPORT GENERATOR
# ============================================================

"""
This file generates professional PDF reports
for retinal analysis results.
"""

# ============================================================
# IMPORTS
# ============================================================

import os
from datetime import datetime

from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    Image,

    Table,

    TableStyle
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import letter

# ============================================================
# OUTPUT DIRECTORY
# ============================================================

REPORT_OUTPUT_DIR = "outputs/reports"

os.makedirs(

    REPORT_OUTPUT_DIR,

    exist_ok=True
)

# ============================================================
# GENERATE PDF REPORT
# ============================================================

def generate_pdf_report(

    prediction_result,

    retina_image_path,

    heatmap_path
):

    """
    Generate medical PDF report.

    Parameters:
    ----------
    prediction_result : dict

    retina_image_path : str

    heatmap_path : str

    Returns:
    -------
    pdf_path : str
    """

    # ========================================================
    # TIMESTAMP
    # ========================================================

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    # ========================================================
    # PDF PATH
    # ========================================================

    pdf_path = os.path.join(

        REPORT_OUTPUT_DIR,

        f"RetaniaScan_Report_{timestamp}.pdf"
    )

    # ========================================================
    # CREATE PDF DOCUMENT
    # ========================================================

    doc = SimpleDocTemplate(

        pdf_path,

        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # ========================================================
    # TITLE
    # ========================================================

    title = Paragraph(

        "<b><font size=18>"
        "RetaniaScan-AI Medical Report"
        "</font></b>",

        styles["Title"]
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    # ========================================================
    # SUBTITLE
    # ========================================================

    subtitle = Paragraph(

        "AI-Powered Diabetic Retinopathy "
        "Analysis System",

        styles["Normal"]
    )

    elements.append(subtitle)

    elements.append(Spacer(1, 20))

    # ========================================================
    # REPORT TABLE
    # ========================================================

    table_data = [

        ["Prediction",
         prediction_result["prediction"]],

        ["Confidence",
         f"{prediction_result['confidence']}%"],

        ["Second Likely Class",
         (
            f"{prediction_result['second_prediction']} "
            f"({prediction_result['second_confidence']}%)"
         )],

        ["Risk Level",
         prediction_result["risk_level"]],

        ["Confidence Status",
         prediction_result["confidence_status"]],

        ["Recommendation",
         prediction_result["recommendation"]]
    ]

    table = Table(

        table_data,

        colWidths=[180, 300]
    )

    table.setStyle(

        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.lightblue
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, -1),
                colors.black
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, -1),
                "Helvetica"
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                8
            )
        ])
    )

    elements.append(table)

    elements.append(Spacer(1, 25))

    # ========================================================
    # ORIGINAL RETINA IMAGE
    # ========================================================

    retina_title = Paragraph(

        "<b>Uploaded Retina Image</b>",

        styles["Heading2"]
    )

    elements.append(retina_title)

    elements.append(Spacer(1, 10))

    retina_img = Image(

        retina_image_path,

        width=250,

        height=250
    )

    elements.append(retina_img)

    elements.append(Spacer(1, 25))

    # ========================================================
    # GRADCAM IMAGE
    # ========================================================

    heatmap_title = Paragraph(

        "<b>GradCAM Explainability Heatmap</b>",

        styles["Heading2"]
    )

    elements.append(heatmap_title)

    elements.append(Spacer(1, 10))

    heatmap_img = Image(

        heatmap_path,

        width=250,

        height=250
    )

    elements.append(heatmap_img)

    elements.append(Spacer(1, 25))

    # ========================================================
    # DISCLAIMER
    # ========================================================

    disclaimer = Paragraph(

        "<b>Disclaimer:</b><br/>"
        "This AI system is designed for "
        "educational and research purposes only. "
        "Please consult a qualified ophthalmologist "
        "for professional medical diagnosis.",

        styles["BodyText"]
    )

    elements.append(disclaimer)

    elements.append(Spacer(1, 20))

    # ========================================================
    # TIMESTAMP
    # ========================================================

    generated_time = Paragraph(

        f"Report Generated: {timestamp}",

        styles["Italic"]
    )

    elements.append(generated_time)

    # ========================================================
    # BUILD PDF
    # ========================================================

    doc.build(elements)

    print(
        "PDF Report Generated Successfully!"
    )

    return pdf_path

# ============================================================
# END OF FILE
# ============================================================