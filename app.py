# ============================================================
# RETANIASCAN-AI GRADIO APPLICATION
# ============================================================

"""
Main deployment interface for RetaniaScan-AI.

Features:
---------
1. Retinal image upload
2. AI diabetic retinopathy detection
3. Confidence scoring
4. GradCAM explainability
5. Medical recommendation system
6. Downloadable PDF medical reports
"""

# ============================================================
# IMPORTS
# ============================================================

import gradio as gr

# ============================================================
# IMPORT MAIN ANALYSIS PIPELINE
# ============================================================

from app.main import analyze_retina

# ============================================================
# IMPORT CONFIGURATION
# ============================================================

from app.config import (

    APP_TITLE,

    APP_DESCRIPTION
)

# ============================================================
# ANALYSIS FUNCTION
# ============================================================

def run_analysis(image):

    """
    Run complete retinal analysis.

    Parameters:
    ----------
    image : PIL.Image

    Returns:
    -------
    report : str

    heatmap : PIL.Image

    pdf_report : str
    """

    # ========================================================
    # VALIDATE IMAGE
    # ========================================================

    if image is None:

        return (

            "Please upload a retinal image.",

            None,

            None
        )

    # ========================================================
    # RUN COMPLETE AI ANALYSIS
    # ========================================================

    report, heatmap, pdf_path = (

        analyze_retina(image)
    )

    return (

        report,

        heatmap,

        pdf_path
    )

# ============================================================
# GRADIO INTERFACE
# ============================================================

with gr.Blocks(

    theme=gr.themes.Soft(),

    title=APP_TITLE
) as demo:

    # ========================================================
    # HEADER SECTION
    # ========================================================

    gr.Markdown(

        f"""
# 👁️ {APP_TITLE}

### {APP_DESCRIPTION}

AI-powered diabetic retinopathy analysis system
using EfficientNetB2 + GradCAM explainability.

---

### Features

✅ DR Severity Classification  
✅ Confidence Scoring  
✅ Risk Assessment  
✅ GradCAM Explainability  
✅ Medical Recommendations  
✅ Downloadable PDF Reports

---
"""
    )

    # ========================================================
    # MAIN LAYOUT
    # ========================================================

    with gr.Row():

        # ====================================================
        # LEFT PANEL
        # ====================================================

        with gr.Column(scale=1):

            input_image = gr.Image(

                type="pil",

                label="Upload Retinal Fundus Image"
            )

            analyze_button = gr.Button(

                "🔍 Analyze Retina",

                variant="primary",

                size="lg"
            )

            gr.Markdown(

                """
### Example Usage

Upload:
- Fundus retinal image
- JPG / PNG format
- Clear retinal scan

The AI system will analyze
the retinal structures and
generate a detailed report.
"""
            )

        # ====================================================
        # RIGHT PANEL
        # ====================================================

        with gr.Column(scale=2):

            output_report = gr.Textbox(

                label="Medical Analysis Report",

                lines=22
            )

            output_heatmap = gr.Image(

                label="GradCAM Explainability Heatmap"
            )

            output_pdf = gr.File(

                label="Download PDF Medical Report"
            )

    # ========================================================
    # ANALYSIS BUTTON ACTION
    # ========================================================

    analyze_button.click(

        fn=run_analysis,

        inputs=input_image,

        outputs=[

            output_report,

            output_heatmap,

            output_pdf
        ]
    )

    # ========================================================
    # FOOTER
    # ========================================================

    gr.Markdown(

        """
---
## ⚠ Disclaimer

RetaniaScan-AI is designed for:

- Educational purposes
- Research demonstrations
- AI-assisted retinal analysis

This system is NOT a substitute
for professional medical diagnosis.

Please consult a qualified ophthalmologist
for clinical evaluation and treatment.

---
"""
    )

# ============================================================
# LAUNCH APPLICATION
# ============================================================

if __name__ == "__main__":

    demo.launch(

        share=True
    )

# ============================================================
# END OF FILE
# ============================================================