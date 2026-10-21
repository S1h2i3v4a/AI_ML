import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

src_ppt = r'C:/Users/Shivam Keshari/.gemini/antigravity/brain/8ef3ef34-7b4d-453e-b498-75b3644d3aa7/.user_uploaded/media_1792515573274_65da0e82.pptx'
dst_ppt = r'c:\Users\Shivam Keshari\OneDrive\Desktop\AI-ML\SmartCredit\smartCredit.pptx'
dfd_img = r'c:\Users\Shivam Keshari\OneDrive\Desktop\AI-ML\SmartCredit\assets\dfd_smartcredit.png'

prs = pptx.Presentation(src_ppt)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 1: Title Slide
# ══════════════════════════════════════════════════════════════════════════════
s1 = prs.slides[0]
for shape in s1.shapes:
    if shape.has_text_frame and 'Summer Training' in shape.text:
        tf = shape.text_frame
        # Clear and rebuild paragraphs to maintain formatting
        for p in tf.paragraphs:
            if 'AI-Driven Student' in p.text:
                p.text = '"SmartCredit: AI-Powered Loan Default Prediction & Risk Scoring System"'
            elif 'RISHI PANDEY' in p.text:
                p.text = '       NAME – SHIVAM KESHARI'

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 2: Table of Content (Keep exact layout)
# ══════════════════════════════════════════════════════════════════════════════
# Slide 2 is already standard table of content:
# Introduction, Objectives, Technology Used, Data Flow Diagram, Features & Dashboard, Future Work, Conclusion, References

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 3: Introduction & Problem Statement
# ══════════════════════════════════════════════════════════════════════════════
s3 = prs.slides[2]
for shape in s3.shapes:
    if shape.has_text_frame and 'EduPredict' in shape.text:
        tf = shape.text_frame
        tf.clear()
        
        p1 = tf.paragraphs[0]
        p1.text = "SmartCredit is a machine-learning-based application designed to predict borrower loan default and credit risk."
        p1.font.size = Pt(14)
        
        p2 = tf.add_paragraph()
        p2.text = "It analyzes financial, demographic, and behavioral factors including income, credit score, DTI ratio, and assets."
        p2.font.size = Pt(14)
        
        p3 = tf.add_paragraph()
        p3.text = "It helps banks and financial institutions identify high-risk applicants early and minimize Non-Performing Assets (NPAs)."
        p3.font.size = Pt(14)
        
        p4 = tf.add_paragraph()
        p4.text = "The system provides real-time default probability, granular risk tiers (Low/Medium/High), and recommended safe loan limits."
        p4.font.size = Pt(14)
        
        p_head = tf.add_paragraph()
        p_head.text = "Problem Statement"
        p_head.font.size = Pt(18)
        p_head.font.bold = True
        p_head.font.color.rgb = RGBColor(16, 44, 87)
        
        p5 = tf.add_paragraph()
        p5.text = "In banking and NBFCs, manual credit underwriting is slow, labor-intensive, and prone to human subjectivity. Unsound loan sanctions directly lead to increased loan defaults and non-performing assets (NPAs), jeopardizing institutional liquidity."
        p5.font.size = Pt(13)
        
        p6 = tf.add_paragraph()
        p6.text = "The proposed SmartCredit – AI-Powered Loan Default Prediction & Risk Scoring System leverages machine learning to automate underwriting, evaluate default probability accurately, and assign transparent risk categories. It empowers lenders to make rapid, objective, and risk-adjusted credit decisions."
        p6.font.size = Pt(13)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 4: Objectives
# ══════════════════════════════════════════════════════════════════════════════
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
            p.space_after = Pt(14)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 5: Technology Used (Table update)
# ══════════════════════════════════════════════════════════════════════════════
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

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 6: Data Flow Diagram (DFD)
# ══════════════════════════════════════════════════════════════════════════════
s6 = prs.slides[5]
# Find the large DFD image and replace it with our SmartCredit DFD
for shape in s6.shapes:
    if hasattr(shape, 'image') and shape.width > Inches(8):
        # This is the old horizontal DFD (shape 5)
        # We replace it by deleting old shape or updating its image
        left, top, width, height = shape.left, shape.top, shape.width, shape.height
        # In python-pptx we can remove and add a new picture at same position
        sp = shape._element
        sp.getparent().remove(sp)
        s6.shapes.add_picture(dfd_img, left, top, width, height)
        break

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 7: Future Scope
# ══════════════════════════════════════════════════════════════════════════════
s7 = prs.slides[6]
for shape in s7.shapes:
    if shape.has_text_frame and 'Improve prediction' in shape.text:
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

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 8: Conclusion
# ══════════════════════════════════════════════════════════════════════════════
s8 = prs.slides[7]
for shape in s8.shapes:
    if shape.has_text_frame and 'EduPredict' in shape.text:
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

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 9: References
# ══════════════════════════════════════════════════════════════════════════════
s9 = prs.slides[8]
for shape in s9.shapes:
    if shape.has_text_frame and 'Student Performance' in shape.text:
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

# Save the updated presentation
prs.save(dst_ppt)
print("Updated presentation saved successfully to:", dst_ppt)
