"""
generate_presentation_suite.py
Generates both SmartCredit.pptx and SmartCredit.pdf matching the United Group
presentation format, layouts, logos, and structure.
"""

import sys

# Ensure UTF-8 output on Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    pass

import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from PIL import Image

BASE_DIR = r"c:\Users\Shivam Keshari\OneDrive\Desktop\AI-ML\SmartCredit"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
REPORTS_DIR = os.path.join(BASE_DIR, "reports", "figures")
SRC_PPT = r"C:\Users\Shivam Keshari\.gemini\antigravity\brain\8ef3ef34-7b4d-453e-b498-75b3644d3aa7\.user_uploaded\media_1792515573274_65da0e82.pptx"

LOGO_PATH = os.path.join(ASSETS_DIR, "united_logo.png")
DFD_PATH = os.path.join(ASSETS_DIR, "dfd_smartcredit.png")
ROC_PATH = os.path.join(REPORTS_DIR, "roc_curves.png")

OUTPUT_PPTX = os.path.join(BASE_DIR, "smartCredit.pptx")
OUTPUT_PDF = os.path.join(BASE_DIR, "smartCredit.pdf")

WORKSPACE_PPTX = r"c:\Users\Shivam Keshari\OneDrive\Desktop\AI-ML\smartCredit.pptx"
WORKSPACE_PDF = r"c:\Users\Shivam Keshari\OneDrive\Desktop\AI-ML\smartCredit.pdf"


# ══════════════════════════════════════════════════════════════════════════════
# PART 1: POWERPOINT (PPTX) GENERATION
# ══════════════════════════════════════════════════════════════════════════════
def build_pptx():
    prs = pptx.Presentation(SRC_PPT)

    # Slide 1: Title
    s1 = prs.slides[0]
    for shape in s1.shapes:
        if shape.has_text_frame and 'Summer Training' in shape.text:
            tf = shape.text_frame
            for p in tf.paragraphs:
                p.alignment = PP_ALIGN.CENTER
                if 'AI-Driven Student' in p.text:
                    p.text = '"SmartCredit: AI-Powered Loan Default Prediction & Risk Scoring System"'
                elif 'RISHI PANDEY' in p.text or 'SHIVAM KESHARI' in p.text:
                    p.text = 'NAME - SHIVAM KESHARI'
                elif '2302840100178' in p.text or 'ROLL NO.' in p.text:
                    p.text = 'ROLL NO. - (2302840100210)'
        elif shape.has_text_frame and 'Supervision' in shape.text:
            # Remove supervisor shape as requested
            shape.text_frame.clear()
        elif shape.has_text_frame and 'College' in shape.text:
            # Center college and session text
            shape.left = 0
            shape.width = prs.slide_width
            for p in shape.text_frame.paragraphs:
                p.alignment = PP_ALIGN.CENTER

    # Slide 3: Introduction
    s3 = prs.slides[2]
    for shape in s3.shapes:
        if shape.has_text_frame and 'EduPredict' in shape.text:
            tf = shape.text_frame
            tf.clear()
            
            p1 = tf.paragraphs[0]
            p1.text = "• SmartCredit is a machine-learning application designed to evaluate loan default risk and borrower creditworthiness."
            p1.font.size = Pt(13.5)
            p1.space_after = Pt(4)
            
            p2 = tf.add_paragraph()
            p2.text = "• It analyzes financial, demographic, and behavioral factors including income, credit score, DTI ratio, and assets."
            p2.font.size = Pt(13.5)
            p2.space_after = Pt(4)
            
            p3 = tf.add_paragraph()
            p3.text = "• It helps banks and NBFCs identify high-risk applicants early and minimize Non-Performing Assets (NPAs)."
            p3.font.size = Pt(13.5)
            p3.space_after = Pt(4)
            
            p4 = tf.add_paragraph()
            p4.text = "• The system provides real-time default probability, granular risk tiers (Low/Medium/High), and recommended safe loan limits."
            p4.font.size = Pt(13.5)
            p4.space_after = Pt(10)
            
            p_head = tf.add_paragraph()
            p_head.text = "Problem Statement"
            p_head.font.size = Pt(17)
            p_head.font.bold = True
            p_head.font.color.rgb = RGBColor(16, 44, 87)
            p_head.space_after = Pt(6)
            
            p5 = tf.add_paragraph()
            p5.text = "In banking and NBFCs, manual credit underwriting is slow, labor-intensive, and prone to human subjectivity. Unsound loan sanctions directly lead to increased loan defaults and non-performing assets (NPAs), jeopardizing institutional liquidity."
            p5.font.size = Pt(12.5)
            p5.space_after = Pt(4)
            
            p6 = tf.add_paragraph()
            p6.text = "The proposed SmartCredit – AI-Powered Loan Default Prediction & Risk Scoring System leverages machine learning to automate underwriting, evaluate default probability accurately, and assign transparent risk categories. It empowers lenders to make rapid, objective, and risk-adjusted credit decisions."
            p6.font.size = Pt(12.5)

    # Slide 4: Objectives
    s4 = prs.slides[3]
    for shape in s4.shapes:
        if shape.has_text_frame and 'student performance' in shape.text.lower():
            tf = shape.text_frame
            tf.clear()
            objs = [
                "To predict loan approval and default risk using trained machine learning classification models.",
                "To analyze critical financial determinants such as Debt-to-Income (DTI) ratio, CIBIL score, and savings.",
                "To identify high-risk applicants early and protect lenders against financial default losses (NPAs).",
                "To categorize applicants into actionable risk tiers (Low, Medium, High) with safe loan amount limits.",
                "To provide a user-friendly, interactive Streamlit web dashboard for real-time credit underwriting."
            ]
            for idx, obj in enumerate(objs):
                p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                p.text = obj
                p.font.size = Pt(15)
                p.space_after = Pt(16)

    # Slide 5: Technology Used
    s5 = prs.slides[4]
    for shape in s5.shapes:
        if shape.has_table:
            table = shape.table
            tech_data = [
                ("Technology", "Purpose"),
                ("Python", "Core programming language for ML pipeline and backend"),
                ("Streamlit", "Interactive multi-page web application & user interface"),
                ("Pandas", "Data ingestion, hygiene checking, and data preprocessing"),
                ("NumPy", "Vectorized numerical transformations and ratio computations"),
                ("Scikit-Learn", "Model training (Logistic, Tree, Random Forest) & metrics"),
                ("Machine Learning", "Credit risk classification & minimal cost-complexity pruning")
            ]
            for r_idx, (t, p) in enumerate(tech_data):
                table.cell(r_idx, 0).text = t
                table.cell(r_idx, 1).text = p
                for c_idx in [0, 1]:
                    cell = table.cell(r_idx, c_idx)
                    for paragraph in cell.text_frame.paragraphs:
                        paragraph.font.size = Pt(13)
                        if r_idx == 0:
                            paragraph.font.bold = True

    # Slide 6: Data Flow Diagram
    s6 = prs.slides[5]
    for shape in s6.shapes:
        if hasattr(shape, 'image') and shape.width > Inches(8):
            left, top, width, height = shape.left, shape.top, shape.width, shape.height
            sp = shape._element
            sp.getparent().remove(sp)
            s6.shapes.add_picture(DFD_PATH, left, top, width, height)
            break

    # Slide 7: Insert "Features & Dashboard" (clone layout or add slide)
    # Check if we already have 11 slides
    if len(prs.slides) == 10:
        # Insert a slide using Content layout (index 1)
        layout = prs.slide_layouts[1]
        s_feat = prs.slides.add_slide(layout)
        
        # Add title
        title_shape = s_feat.shapes.title
        title_shape.text = "Features & Dashboard"
        title_shape.text_frame.paragraphs[0].font.size = Pt(28)
        title_shape.text_frame.paragraphs[0].font.bold = True
        title_shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(16, 44, 87)
        
        # Add logo
        s_feat.shapes.add_picture(LOGO_PATH, Inches(0.4), Inches(0.3), Inches(2.3), Inches(0.7))
        
        # Add content text on left
        txBox = s_feat.shapes.add_textbox(Inches(0.6), Inches(1.5), Inches(6.5), Inches(5.0))
        tf = txBox.text_frame
        tf.word_wrap = True
        
        features = [
            ("Real-Time Credit Prediction:", " Instant evaluation of loan approval probability in under 1 second."),
            ("Granular Risk Tiers:", " Automated tagging into Low Risk (🟢), Medium Risk (🟡), and High Risk (🔴)."),
            ("Safe Loan Recommendation:", " Algorithmic calculation of maximum safe sanction amount based on DTI."),
            ("Interactive EDA Portal:", " Multi-tab distribution curves, CIBIL boxplots, and correlation heatmaps."),
            ("Model Benchmark Suite:", " Side-by-side performance ledger, confusion matrices, and ROC curves.")
        ]
        for idx, (title, desc) in enumerate(features):
            p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
            p.text = f"{title}{desc}"
            p.font.size = Pt(13)
            p.space_after = Pt(10)
            
        # Add ROC curve image on right
        if os.path.exists(ROC_PATH):
            s_feat.shapes.add_picture(ROC_PATH, Inches(7.3), Inches(1.8), Inches(4.8), Inches(3.8))

        # Reorder slides so Features & Dashboard is Slide 7 (index 6)
        # In python-pptx, move slide element in xml:
        slides_elem = prs.slides._sldIdLst
        feat_elem = slides_elem[-1]
        slides_elem.insert(6, feat_elem)

    # Slide 8 (original 7): Future Scope
    s_future = prs.slides[7]
    for shape in s_future.shapes:
        if shape.has_text_frame and ('Improve prediction' in shape.text or 'Future Scope' in shape.text):
            if 'Future Scope' not in shape.text:
                tf = shape.text_frame
                tf.clear()
                scopes = [
                    "Integrate alternative data sources such as utility payments, GST returns, and open banking APIs.",
                    "Incorporate Explainable AI (XAI) using SHAP and LIME for transparent credit denial justifications.",
                    "Implement automated PDF credit underwriting report generation with digital risk certificate.",
                    "Deploy the application onto cloud platforms (Streamlit Community Cloud / AWS ECS) for multi-branch access.",
                    "Enhance data security, encryption standards, and regulatory compliance (RBI / Fair Lending mandates)."
                ]
                for idx, sc in enumerate(scopes):
                    p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                    p.text = sc
                    p.font.size = Pt(15)
                    p.space_after = Pt(14)

    # Slide 9 (original 8): Conclusion
    s_conc = prs.slides[8]
    for shape in s_conc.shapes:
        if shape.has_text_frame and ('EduPredict' in shape.text or 'Conclusion' in shape.text):
            if 'Conclusion' not in shape.text:
                tf = shape.text_frame
                tf.clear()
                conclusions = [
                    "SmartCredit demonstrates the practical application of Machine Learning in FinTech credit risk evaluation.",
                    "It successfully integrates financial, demographic, and leverage metrics into a unified predictive model.",
                    "The Random Forest model achieved a 95.8% accuracy and 100% recall, minimizing costly False Negatives.",
                    "The interactive Streamlit dashboard provides transparent risk tiers, probability metrics, and safe limits.",
                    "The system acts as a reliable decision-support intelligence tool, accelerating institutional underwriting."
                ]
                for idx, c in enumerate(conclusions):
                    p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                    p.text = c
                    p.font.size = Pt(15)
                    p.space_after = Pt(14)

    # Slide 10 (original 9): References
    s_ref = prs.slides[9]
    for shape in s_ref.shapes:
        if shape.has_text_frame and ('Student Performance' in shape.text or 'References' in shape.text):
            if 'References' not in shape.text:
                tf = shape.text_frame
                tf.clear()
                refs = [
                    "Loan Approval Benchmark Dataset — Historical Retail Banking Credit Risk Records.",
                    "Scikit-Learn Documentation — Minimal Cost-Complexity Pruning & Random Forest (scikit-learn.org).",
                    "Streamlit Documentation — Multi-page Web Applications & Interactive Widgets (docs.streamlit.io).",
                    "Pandas & NumPy Documentation — Data Cleaning, Imputation & Vector Operations (pandas.pydata.org).",
                    "Leo Breiman, Jerome Friedman et al. — Classification and Regression Trees (CART Theory).",
                    "Reserve Bank of India (RBI) / Basel III Framework — Guidelines on Credit Risk & NPA Management."
                ]
                for idx, r in enumerate(refs):
                    p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
                    p.text = r
                    p.font.size = Pt(14)
                    p.space_after = Pt(12)

    prs.save(OUTPUT_PPTX)
    prs.save(WORKSPACE_PPTX)
    print(f"✅ PPTX saved to: {OUTPUT_PPTX} and {WORKSPACE_PPTX}")


# ══════════════════════════════════════════════════════════════════════════════
# PART 2: HIGH-DEFINITION PDF GENERATION (ReportLab)
# ══════════════════════════════════════════════════════════════════════════════
def build_pdf():
    # 16:9 widescreen canvas: 960 x 540 pt
    w, h = 960, 540
    c = canvas.Canvas(OUTPUT_PDF, pagesize=(w, h))

    navy = colors.HexColor('#102C57')
    crimson = colors.HexColor('#D93025')
    charcoal = colors.HexColor('#202124')
    gray_bg = colors.HexColor('#F8F9FA')
    border_color = colors.HexColor('#DADCE0')

    def draw_header(title_text):
        # United logo top right
        if os.path.exists(LOGO_PATH):
            c.drawImage(LOGO_PATH, 40, h - 55, width=150, height=42, preserveAspectRatio=True, mask='auto')
        # Title text
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(220, h - 45, title_text)
        # Red divider line
        c.setStrokeColor(crimson)
        c.setLineWidth(2.5)
        c.line(40, h - 68, w - 40, h - 68)

    # ── Slide 1: Title Slide ──────────────────────────────────────────────────
    # Logo top right
    if os.path.exists(LOGO_PATH):
        c.drawImage(LOGO_PATH, w - 240, h - 85, width=200, height=56, preserveAspectRatio=True, mask='auto')

    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(w / 2, h - 140, "Summer Training Project Presentation")
    c.setFont("Helvetica", 16)
    c.setFillColor(charcoal)
    c.drawCentredString(w / 2, h - 170, "on")

    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(w / 2, h - 215, '"SmartCredit: AI-Powered Loan Default Prediction & Risk Scoring System"')

    # Red accent line
    c.setStrokeColor(crimson)
    c.setLineWidth(3)
    c.line(w / 2 - 250, h - 235, w / 2 + 250, h - 235)

    # Student info (Centered)
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(w / 2, h - 300, "NAME - SHIVAM KESHARI")
    c.setFillColor(charcoal)
    c.setFont("Helvetica", 14)
    c.drawCentredString(w / 2, h - 325, "ROLL NO. - (2302840100210)")

    # Bottom footer
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(w / 2, 80, "College : United Institute of Technology")
    c.setFont("Helvetica", 12)
    c.setFillColor(charcoal)
    c.drawCentredString(w / 2, 60, "Session : 2026-2027")

    c.showPage()

    # ── Slide 2: Table of Content ─────────────────────────────────────────────
    draw_header("Table of Content")

    toc_items = [
        "1.  Introduction & Problem Statement",
        "2.  Objectives",
        "3.  Technology Used",
        "4.  Data Flow Diagram (DFD)",
        "5.  Features & Dashboard",
        "6.  Future Scope",
        "7.  Conclusion",
        "8.  References"
    ]

    c.setFillColor(charcoal)
    c.setFont("Helvetica-Bold", 15)
    for idx, item in enumerate(toc_items[:4]):
        # Card box
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(80, h - 140 - idx * 75, 360, 55, 6, fill=1, stroke=1)
        c.setFillColor(navy)
        c.drawString(100, h - 105 - idx * 75, item)

    for idx, item in enumerate(toc_items[4:]):
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(500, h - 140 - idx * 75, 360, 55, 6, fill=1, stroke=1)
        c.setFillColor(navy)
        c.drawString(520, h - 105 - idx * 75, item)

    c.showPage()

    # ── Slide 3: Introduction & Problem Statement ─────────────────────────────
    draw_header("Introduction")

    intro_bullets = [
        "SmartCredit is a machine-learning application designed to evaluate loan default risk and borrower creditworthiness.",
        "It analyzes financial, demographic, and behavioral factors including income, credit score, DTI ratio, and assets.",
        "It helps banks and NBFCs identify high-risk applicants early and minimize Non-Performing Assets (NPAs).",
        "The system provides real-time default probability, granular risk tiers (Low/Medium/High), and recommended safe loan limits."
    ]

    y = h - 95
    c.setFont("Helvetica", 12)
    c.setFillColor(charcoal)
    for b in intro_bullets:
        c.drawString(55, y, "•  " + b)
        y -= 22

    # Problem Statement Subheading
    y -= 10
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(navy)
    c.drawString(55, y, "Problem Statement")
    c.setStrokeColor(crimson)
    c.setLineWidth(1.5)
    c.line(55, y - 4, 195, y - 4)

    y -= 26
    c.setFont("Helvetica", 11.5)
    c.setFillColor(charcoal)
    ps1 = "In banking and NBFCs, manual credit underwriting is slow, labor-intensive, and prone to human subjectivity. Unsound loan sanctions directly lead to increased loan defaults and non-performing assets (NPAs), jeopardizing institutional liquidity."
    # Wrap text
    from reportlab.lib.utils import simpleSplit
    for line in simpleSplit(ps1, "Helvetica", 11.5, w - 110):
        c.drawString(55, y, line)
        y -= 18

    y -= 8
    ps2 = "The proposed SmartCredit – AI-Powered Loan Default Prediction & Risk Scoring System leverages machine learning to automate underwriting, evaluate default probability accurately, and assign transparent risk categories. It empowers lenders to make rapid, objective, and risk-adjusted credit decisions."
    for line in simpleSplit(ps2, "Helvetica", 11.5, w - 110):
        c.drawString(55, y, line)
        y -= 18

    c.showPage()

    # ── Slide 4: Objectives ───────────────────────────────────────────────────
    draw_header("Objectives")

    objs = [
        "To predict loan approval and default risk using trained machine learning classification models.",
        "To analyze critical financial determinants such as Debt-to-Income (DTI) ratio, CIBIL score, and savings.",
        "To identify high-risk applicants early and protect lenders against financial default losses (NPAs).",
        "To categorize applicants into actionable risk tiers (Low, Medium, High) with safe loan amount limits.",
        "To provide a user-friendly, interactive Streamlit web dashboard for real-time credit underwriting."
    ]

    y = h - 120
    for idx, obj in enumerate(objs):
        # Card background
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(55, y - 10, w - 110, 48, 6, fill=1, stroke=1)
        
        # Number badge
        c.setFillColor(navy)
        c.circle(85, y + 14, 14, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(85, y + 10, str(idx + 1))
        
        # Text
        c.setFillColor(charcoal)
        c.setFont("Helvetica", 12.5)
        c.drawString(115, y + 10, obj)
        y -= 70

    c.showPage()

    # ── Slide 5: Technology Used ──────────────────────────────────────────────
    draw_header("Technology Used")

    tech_table = [
        ("Technology", "Purpose"),
        ("Python", "Core programming language for ML pipeline and backend"),
        ("Streamlit", "Interactive multi-page web application & user interface"),
        ("Pandas", "Data ingestion, hygiene checking, and data preprocessing"),
        ("NumPy", "Vectorized numerical transformations and ratio computations"),
        ("Scikit-Learn", "Model training (Logistic, Tree, Random Forest) & metrics"),
        ("Machine Learning", "Credit risk classification & minimal cost-complexity pruning")
    ]

    y = h - 120
    col1_w = 220
    col2_w = 580
    row_h = 45

    for r_idx, (t, p) in enumerate(tech_table):
        if r_idx == 0:
            c.setFillColor(navy)
            c.rect(80, y, col1_w + col2_w, row_h, fill=1, stroke=0)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 13)
            c.drawString(100, y + 16, t)
            c.drawString(320, y + 16, p)
        else:
            bg = gray_bg if r_idx % 2 == 1 else colors.white
            c.setFillColor(bg)
            c.setStrokeColor(border_color)
            c.rect(80, y, col1_w + col2_w, row_h, fill=1, stroke=1)
            c.setFillColor(navy)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(100, y + 16, t)
            c.setFillColor(charcoal)
            c.setFont("Helvetica", 11.5)
            c.drawString(320, y + 16, p)
        y -= row_h

    c.showPage()

    # ── Slide 6: Data Flow Diagram ────────────────────────────────────────────
    draw_header("Data Flow Diagram")

    if os.path.exists(DFD_PATH):
        # Draw DFD centered
        c.drawImage(DFD_PATH, 50, 40, width=860, height=420, preserveAspectRatio=True)

    c.showPage()

    # ── Slide 7: Features & Dashboard ─────────────────────────────────────────
    draw_header("Features & Dashboard")

    features = [
        ("Real-Time Credit Prediction", "Instant evaluation of loan approval probability in under 1 second."),
        ("Granular Risk Tiers", "Automated tagging into Low Risk (🟢), Medium Risk (🟡), and High Risk (🔴)."),
        ("Safe Loan Recommendation", "Algorithmic calculation of maximum safe sanction amount based on DTI."),
        ("Interactive EDA Portal", "Multi-tab distribution curves, CIBIL boxplots, and correlation heatmaps."),
        ("Model Benchmark Suite", "Side-by-side performance ledger, confusion matrices, and ROC curves.")
    ]

    y = h - 110
    for idx, (title, desc) in enumerate(features):
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 12.5)
        c.drawString(55, y, f"•  {title}:")
        c.setFillColor(charcoal)
        c.setFont("Helvetica", 11.5)
        c.drawString(245, y, desc)
        y -= 38

    # Bottom ROC comparison chart
    if os.path.exists(ROC_PATH):
        c.drawImage(ROC_PATH, 480, 50, width=420, height=260, preserveAspectRatio=True)

    # Performance highlight card on left
    c.setFillColor(gray_bg)
    c.setStrokeColor(border_color)
    c.roundRect(55, 60, 390, 230, 8, fill=1, stroke=1)
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(75, 260, "🏆 Model Performance Highlights")
    c.setStrokeColor(crimson)
    c.line(75, 252, 280, 252)

    perf_items = [
        ("Random Forest Accuracy:", "95.79% (Best overall generalisation)"),
        ("Recall (Default Catch):", "100.00% (Zero missed defaults)"),
        ("ROC-AUC Score:", "0.9771 (Industry-grade discrimination)"),
        ("Decision Tree (Pruned):", "94.21% Accuracy (ccp_alpha tuned)"),
        ("Baseline Logistic:", "78.42% Accuracy")
    ]
    py = 225
    for k, v in perf_items:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(75, py, k)
        c.setFillColor(charcoal)
        c.setFont("Helvetica", 10)
        c.drawString(225, py, v)
        py -= 32

    c.showPage()

    # ── Slide 8: Future Scope ─────────────────────────────────────────────────
    draw_header("Future Scope")

    scopes = [
        "Integrate alternative data sources such as utility payments, GST returns, and open banking APIs.",
        "Incorporate Explainable AI (XAI) using SHAP and LIME for transparent credit denial justifications.",
        "Implement automated PDF credit underwriting report generation with digital risk certificate.",
        "Deploy the application onto cloud platforms (Streamlit Community Cloud / AWS ECS) for multi-branch access.",
        "Enhance data security, encryption standards, and regulatory compliance (RBI / Fair Lending mandates)."
    ]

    y = h - 120
    for idx, sc in enumerate(scopes):
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(55, y - 10, w - 110, 48, 6, fill=1, stroke=1)

        c.setFillColor(crimson)
        c.circle(85, y + 14, 14, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(85, y + 10, str(idx + 1))

        c.setFillColor(charcoal)
        c.setFont("Helvetica", 12.5)
        c.drawString(115, y + 10, sc)
        y -= 70

    c.showPage()

    # ── Slide 9: Conclusion ───────────────────────────────────────────────────
    draw_header("Conclusion")

    conclusions = [
        "SmartCredit demonstrates the practical application of Machine Learning in FinTech credit risk evaluation.",
        "It successfully integrates financial, demographic, and leverage metrics into a unified predictive model.",
        "The Random Forest model achieved a 95.8% accuracy and 100% recall, minimizing costly False Negatives.",
        "The interactive Streamlit dashboard provides transparent risk tiers, probability metrics, and safe limits.",
        "The system acts as a reliable decision-support intelligence tool, accelerating institutional underwriting."
    ]

    y = h - 120
    for idx, c_text in enumerate(conclusions):
        c.setFillColor(gray_bg)
        c.setStrokeColor(border_color)
        c.roundRect(55, y - 10, w - 110, 48, 6, fill=1, stroke=1)

        c.setFillColor(navy)
        c.circle(85, y + 14, 14, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(85, y + 10, str(idx + 1))

        c.setFillColor(charcoal)
        c.setFont("Helvetica", 12.5)
        c.drawString(115, y + 10, c_text)
        y -= 70

    c.showPage()

    # ── Slide 10: References ──────────────────────────────────────────────────
    draw_header("References")

    refs = [
        "Loan Approval Benchmark Dataset — Historical Retail Banking Credit Risk Records.",
        "Scikit-Learn Documentation — Minimal Cost-Complexity Pruning & Random Forest (scikit-learn.org).",
        "Streamlit Documentation — Multi-page Web Applications & Interactive Widgets (docs.streamlit.io).",
        "Pandas & NumPy Documentation — Data Cleaning, Imputation & Vector Operations (pandas.pydata.org).",
        "Leo Breiman, Jerome Friedman et al. — Classification and Regression Trees (CART Theory).",
        "Reserve Bank of India (RBI) / Basel III Framework — Guidelines on Credit Risk & NPA Management."
    ]

    y = h - 115
    for idx, r in enumerate(refs):
        c.setFillColor(navy)
        c.circle(75, y + 5, 5, fill=1, stroke=0)
        c.setFillColor(charcoal)
        c.setFont("Helvetica", 12.5)
        c.drawString(95, y, r)
        y -= 54

    c.showPage()

    # ── Slide 11: Thank You ───────────────────────────────────────────────────
    if os.path.exists(LOGO_PATH):
        c.drawImage(LOGO_PATH, w / 2 - 120, h - 160, width=240, height=67, preserveAspectRatio=True, mask='auto')

    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 38)
    c.drawCentredString(w / 2, h / 2 - 10, "Thank You")

    c.setStrokeColor(crimson)
    c.setLineWidth(3)
    c.line(w / 2 - 120, h / 2 - 25, w / 2 + 120, h / 2 - 25)

    c.setFillColor(charcoal)
    c.setFont("Helvetica", 14)
    c.drawCentredString(w / 2, h / 2 - 60, "Questions & Discussion")

    c.save()
    
    # Also save to workspace root
    import shutil
    shutil.copyfile(OUTPUT_PDF, WORKSPACE_PDF)
    print(f"✅ PDF saved to: {OUTPUT_PDF} and {WORKSPACE_PDF}")


if __name__ == "__main__":
    print("Building PowerPoint Presentation...")
    build_pptx()
    print("\nBuilding PDF Presentation...")
    build_pdf()
    print("\n🎉 All presentations successfully generated!")
