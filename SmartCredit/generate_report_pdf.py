"""
generate_report_pdf.py
Generates the complete 17-page SmartCredit Mini Project / Internship Report PDF
matching the exact design, formatting, line wraps, bolding, typography, and structure.
"""

import os
import sys

# Ensure UTF-8 output on Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    pass

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import simpleSplit

BASE_DIR = r"c:\Users\Shivam Keshari\OneDrive\Desktop\AI-ML\SmartCredit"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

EMBLEM_PATH = os.path.join(ASSETS_DIR, "united_emblem.png")
LOGO_PATH = os.path.join(ASSETS_DIR, "united_logo.png")
FLOWCHART_PATH = os.path.join(ASSETS_DIR, "flowchart_smartcredit.png")
UI_FIG1_PATH = os.path.join(ASSETS_DIR, "ui_fig_6_1.png")
UI_FIG2_PATH = os.path.join(ASSETS_DIR, "ui_fig_6_2.png")

OUTPUT_PDF = os.path.join(BASE_DIR, "SmartCredit_Project_Report.pdf")
WORKSPACE_PDF = r"c:\Users\Shivam Keshari\OneDrive\Desktop\AI-ML\SmartCredit_Project_Report.pdf"

W, H = A4  # 595.27 x 841.89 pt
LEFT_MARGIN = 72
RIGHT_MARGIN = W - 72
CONTENT_WIDTH = RIGHT_MARGIN - LEFT_MARGIN  # ~451 pt


def draw_bullet(c, x, y, radius=2):
    """Draw a clean filled circular bullet dot."""
    c.circle(x, y + 3.5, radius, fill=1, stroke=0)


def draw_para(c, text, x, y, font="Times-Roman", font_size=11, leading=15, width=CONTENT_WIDTH, align="left"):
    """Draw a paragraph with word wrapping."""
    c.setFont(font, font_size)
    lines = simpleSplit(text, font, font_size, width)
    for line in lines:
        if align == "center":
            c.drawCentredString(W / 2, y, line)
        elif align == "right":
            c.drawRightString(RIGHT_MARGIN, y, line)
        else:
            c.drawString(x, y, line)
        y -= leading
    return y


def build_report():
    c = canvas.Canvas(OUTPUT_PDF, pagesize=A4)

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 1: TITLE / COVER PAGE
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 90
    c.setFont("Times-Roman", 13)
    c.drawCentredString(W / 2, y, "A")
    y -= 25
    c.drawCentredString(W / 2, y, "Mini Project or Internship Report")
    
    y -= 55
    c.setFont("Times-Bold", 17)
    c.drawCentredString(W / 2, y, '"AI-Driven Loan Default Prediction and')
    y -= 24
    c.drawCentredString(W / 2, y, 'Risk Scoring System"')

    y -= 45
    c.setFont("Times-Roman", 11)
    c.drawCentredString(W / 2, y, "Submitted in partially fulfilment for the requirement for the award of the degree")
    y -= 16
    c.drawCentredString(W / 2, y, "of")
    
    y -= 28
    c.setFont("Times-Bold", 13)
    c.drawCentredString(W / 2, y, "Bachelor of Technology")
    y -= 18
    c.setFont("Times-Roman", 11)
    c.drawCentredString(W / 2, y, "in")
    y -= 20
    c.setFont("Times-Bold", 12)
    c.drawCentredString(W / 2, y, "Computer Science & Engineering")

    y -= 40
    c.setFont("Times-Roman", 12)
    c.drawCentredString(W / 2, y, "Submitted by")
    y -= 22
    c.setFont("Times-Bold", 13)
    c.drawCentredString(W / 2, y, "Name - SHIVAM KESHARI")
    y -= 18
    c.setFont("Times-Bold", 12)
    c.drawCentredString(W / 2, y, "(Uni. Roll No.- 2302840100210)")
    y -= 18
    c.setFont("Times-Bold", 11.5)
    c.drawCentredString(W / 2, y, "Branch Name : Computer Science and Engineering (CSE)")

    y -= 38
    c.setFont("Times-Roman", 11.5)
    c.drawCentredString(W / 2, y, "Under the Supervision of")
    y -= 16
    c.setFont("Times-Bold", 12)
    c.drawCentredString(W / 2, y, "IBM Mentor/Trainer")
    y -= 18
    c.setFont("Times-Bold", 12.5)
    c.drawCentredString(W / 2, y, "Svitlana Kramar")

    # United Emblem Logo
    y -= 60
    if os.path.exists(EMBLEM_PATH):
        c.drawImage(EMBLEM_PATH, (W - 85) / 2, y - 10, width=85, height=68, preserveAspectRatio=True, mask='auto')

    y -= 35
    c.setFont("Times-Roman", 12)
    c.drawCentredString(W / 2, y, "Department of Computer Science & Engineering")
    y -= 18
    c.setFont("Times-Bold", 13)
    c.drawCentredString(W / 2, y, "UNITED INSTITUTE OF TECHNOLOGY (284)")
    y -= 16
    c.setFont("Times-Roman", 10.5)
    c.drawCentredString(W / 2, y, "(Affiliated to Dr. A.P.J. Abdul Kalam Technical University, Lucknow)")

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 2: SESSION PAGE
    # ══════════════════════════════════════════════════════════════════════════
    c.setFont("Times-Bold", 15)
    c.drawCentredString(W / 2, H / 2, "Session-2026-2027")
    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 3: VISION & MISSION OF THE DEPARTMENT
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 90
    c.setFont("Times-Bold", 15)
    c.drawCentredString(W / 2, y, "Vision of the Department")
    c.setLineWidth(1)
    c.line(W / 2 - 95, y - 2, W / 2 + 95, y - 2)

    y -= 45
    vis_text = ("To be a center of excellence in the field of Computer Science and Engineering "
                "for producing talented engineers to ethically serve constantly changing needs of "
                "society and industry throughout their career and life.")
    y = draw_para(c, vis_text, LEFT_MARGIN, y, font="Times-Roman", font_size=11.5, leading=17)

    y -= 50
    c.setFont("Times-Bold", 15)
    c.drawCentredString(W / 2, y, "Mission of the Department")
    c.line(W / 2 - 100, y - 2, W / 2 + 100, y - 2)

    y -= 45
    missions = [
        ("M1. ", "Accomplish excellence with committed faculty by providing theoretical foundation and practical skills for solving complex engineering problems in the state-of-the-art trends in Computer science and allied disciplines."),
        ("M2. ", "To foster skills and competency, generating novel ideas, entrepreneurship and model creations focused towards deep knowledge, interpersonal skills and leadership."),
        ("M3. ", "To develop habitude of research among faculty and students in the area of Computer Science & Allied disciplines by providing the desired environment, for addressing the needs of industry and society."),
        ("M4. ", "To mould the students with ethical principles in thoughts, expression and deeds.")
    ]
    for tag, desc in missions:
        c.setFont("Times-Bold", 11.5)
        c.drawString(LEFT_MARGIN, y, tag)
        full_text = tag + desc
        y = draw_para(c, full_text, LEFT_MARGIN, y, font="Times-Roman", font_size=11.5, leading=16)
        y -= 14

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 4: INDEX (TABLE OF CONTENTS)
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 85
    c.setFont("Times-Bold", 20)
    c.drawCentredString(W / 2, y, "Index")

    y -= 40
    table_top = y
    row_heights = [32, 28, 28, 28, 28, 28, 28, 28, 28, 28]
    total_table_height = sum(row_heights)
    
    col_x = [LEFT_MARGIN, LEFT_MARGIN + 45, RIGHT_MARGIN - 70, RIGHT_MARGIN]

    # Draw Outer Border
    c.setStrokeColor(colors.black)
    c.setLineWidth(0.8)
    c.rect(col_x[0], table_top - total_table_height, CONTENT_WIDTH, total_table_height)

    # Vertical Lines
    for x in col_x[1:-1]:
        c.line(x, table_top, x, table_top - total_table_height)

    index_rows = [
        ("S.\nNo", "Topic", "Page No."),
        ("1", "Introduction", "1"),
        ("2", "Requirement", "2"),
        ("3", "Conceptual Background", "3 to 5"),
        ("4", "Implementation", "6"),
        ("4.1", "Coding", "6 to 9"),
        ("4.2", "Flow Chart", "10"),
        ("5", "User Interface", "11"),
        ("6", "Conclusion", "12"),
        ("", "References", "13")
    ]

    curr_y = table_top
    for r_idx, (sno, topic, pg) in enumerate(index_rows):
        rh = row_heights[r_idx]
        c.line(col_x[0], curr_y, col_x[-1], curr_y)
        
        # Text
        is_header = (r_idx == 0)
        c.setFont("Times-Bold" if is_header else "Times-Roman", 11 if not is_header else 11.5)
        
        # S.No
        if "\n" in sno:
            c.drawCentredString((col_x[0] + col_x[1]) / 2, curr_y - 12, "S.")
            c.drawCentredString((col_x[0] + col_x[1]) / 2, curr_y - 24, "No")
        else:
            c.drawCentredString((col_x[0] + col_x[1]) / 2, curr_y - rh / 2 - 4, sno)

        # Topic
        indent = 15 if "." in sno else 8
        c.drawString(col_x[1] + indent, curr_y - rh / 2 - 4, topic)

        # Page No
        c.drawString(col_x[2] + 10, curr_y - rh / 2 - 4, pg)

        curr_y -= rh

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 5: CHAPTER-1 INTRODUCTION & PROBLEM STATEMENT
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-1")
    y -= 18
    c.drawCentredString(W / 2, y, "Introduction")

    y -= 30
    intro_p1 = ("Financial stability and credit risk evaluation play an essential role in the development of "
                "individuals and banking institutions. Loan approval assessment is an important factor in evaluating "
                "borrower creditworthiness and identifying profiles where default risk is elevated. However, "
                "monitoring and screening every applicant can be challenging when credit underwriters must consider "
                "several financial and demographic indicators simultaneously.")
    y = draw_para(c, intro_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 8

    intro_p2 = ("Traditional approaches to loan underwriting mainly depend on examination of pay slips, manual "
                "record analysis, and credit officer observations. Although these approaches are useful, they may not "
                "always identify potential credit distress at an early stage. As a result, borrowers who present "
                "subtle default indicators may receive loans, or qualified applicants may experience substantial delays.")
    y = draw_para(c, intro_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 8

    intro_p3 = ("The AI-Driven Loan Default Prediction and Risk Scoring System, also known as SmartCredit, is a "
                "machine-learning-based project designed to support credit underwriting and risk assessment. It accepts "
                "relevant applicant financial information, processes the inputs, and generates a prediction using the "
                "machine-learning models implemented in the application.")
    y = draw_para(c, intro_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 8

    intro_p4 = ("The system aims to present the prediction in an understandable format and provide an early risk tier "
                "indication (Low, Medium, or High Risk) along with recommended safe loan limits. This can help users "
                "understand potential credit concerns and consider suitable actions for loan approval or risk mitigation.")
    y = draw_para(c, intro_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 8

    intro_p5 = ("The project uses Python and an interactive Streamlit application interface to demonstrate the practical "
                "application of artificial intelligence, data processing, and machine learning in the financial and banking "
                "sector.")
    y = draw_para(c, intro_p5, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 14

    c.setFont("Times-Bold", 13)
    c.drawCentredString(W / 2, y, "Problem Statement")
    y -= 20

    ps_p1 = ("Borrower creditworthiness is influenced by several factors, including annual income, co-applicant income, "
             "credit score, existing liabilities, collateral value, and debt-to-income (DTI) ratio. Analysing these factors "
             "manually can require considerable time and effort.")
    y = draw_para(c, ps_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 8

    ps_p2 = ("A major challenge is identifying applicants who may require additional credit scrutiny before loans are "
             "sanctioned. Without an organised analysis system, non-performing assets (NPAs) can escalate significantly, "
             "eroding institutional liquidity before default risks are noticed.")
    y = draw_para(c, ps_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 8

    ps_p3 = ("Therefore, there is a need for a system that can process relevant borrower performance data, generate predictions, "
             "and present risk-scoring information in a simple and understandable manner.")
    y = draw_para(c, ps_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 8

    ps_p4 = ("The proposed SmartCredit system addresses this problem by combining data processing and machine-learning "
             "techniques with an interactive user interface.")
    y = draw_para(c, ps_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 6: CHAPTER-2 REQUIREMENT
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-2")
    y -= 18
    c.drawCentredString(W / 2, y, "Requirement")

    y -= 30
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "2.1 Hardware Requirements")
    y -= 18

    c.setFont("Times-Roman", 10.5)
    c.drawString(LEFT_MARGIN, y, "The following hardware configuration is suitable for developing and running the project:")
    y -= 16

    hw_items = [
        "Computer or laptop.",
        "Processor: modern Intel or AMD processor.",
        "RAM: minimum 4 GB; 8 GB or more is recommended.",
        "Storage: sufficient free disk space for Python, project files, libraries, and model files.",
        "Keyboard and mouse or touchpad.",
        "Internet connection for installing libraries and accessing online documentation when required."
    ]
    for hw in hw_items:
        draw_bullet(c, LEFT_MARGIN + 15, y)
        c.drawString(LEFT_MARGIN + 25, y, hw)
        y -= 15

    y -= 4
    hw_note = ("The exact hardware requirements depend on the size of the dataset and the computational "
               "requirements of the selected machine-learning model.")
    y = draw_para(c, hw_note, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 16
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "2.2 Software Requirements")
    y -= 18

    c.setFont("Times-Roman", 10.5)
    c.drawString(LEFT_MARGIN, y, "The project uses a Python-based development environment. The relevant software components include:")
    y -= 16

    sw_items = [
        ("Python: ", "Python is the primary programming language used to implement the application's logic, data processing, and machine-learning workflow."),
        ("Streamlit: ", "Streamlit is used to develop the interactive user interface through which users can enter information and view the prediction results."),
        ("NumPy: ", "NumPy supports numerical calculations and array operations used in data processing."),
        ("Pandas: ", "Pandas provides data structures and data manipulation tools for data loading, cleaning, and preprocessing."),
        ("Scikit-learn: ", "Scikit-learn provides machine-learning utilities for model training, preprocessing, prediction, and evaluation, depending on the implementation."),
        ("Visual Studio Code: ", "Visual Studio Code provides an environment for writing, editing, and running Python code."),
        ("Web Browser: ", "A web browser is used to access the application's interface when it is running locally or through a deployment platform.")
    ]
    for tag, desc in sw_items:
        draw_bullet(c, LEFT_MARGIN + 15, y)
        c.setFont("Times-Bold", 10.5)
        c.drawString(LEFT_MARGIN + 25, y, tag)
        tag_w = c.stringWidth(tag, "Times-Bold", 10.5)
        
        full_line = desc
        lines = simpleSplit(full_line, "Times-Roman", 10.5, CONTENT_WIDTH - 25 - tag_w)
        c.setFont("Times-Roman", 10.5)
        c.drawString(LEFT_MARGIN + 25 + tag_w, y, lines[0])
        y -= 14
        for sub_line in lines[1:]:
            c.drawString(LEFT_MARGIN + 25, y, sub_line)
            y -= 14
        y -= 4

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 7: CHAPTER-3 CONCEPTUAL BACKGROUND (PART 1)
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-3")
    y -= 18
    c.drawCentredString(W / 2, y, "Conceptual Background")

    y -= 28
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.1 Artificial Intelligence")
    y -= 16

    ai_p1 = ("Artificial Intelligence (AI) is a field of computer science concerned with developing systems that can "
             "perform tasks commonly associated with human intelligence. These tasks may include recognising patterns, "
             "analysing information, solving problems, and making predictions.")
    y = draw_para(c, ai_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    ai_p2 = ("AI is used in many areas, including healthcare, banking, transportation, business analytics, and education. "
             "In the financial sector, AI can support credit scoring, fraud detection, portfolio risk management, and the "
             "identification of loan applicants who may benefit from structured terms.")
    y = draw_para(c, ai_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    ai_p3 = ("In this project, artificial intelligence provides the broader foundation for using computational techniques to "
             "analyse borrower performance and creditworthiness information.")
    y = draw_para(c, ai_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.2 Machine Learning")
    y -= 16

    ml_p1 = ("Machine Learning (ML) is a branch of artificial intelligence that enables computers to learn patterns from data "
             "and use those patterns to make predictions or decisions.")
    y = draw_para(c, ml_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    ml_p2 = ("Instead of manually defining every possible condition, a machine-learning model learns relationships from "
             "examples provided during training. The model can then apply those learned relationships to new input data.")
    y = draw_para(c, ml_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    ml_p3 = ("Machine-learning tasks are commonly divided into supervised learning, unsupervised learning, and reinforcement learning.")
    y = draw_para(c, ml_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    ml_p4 = ("Supervised learning uses labelled data containing input features and corresponding target values. Classification "
             "and regression are two common supervised-learning tasks.")
    y = draw_para(c, ml_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 4

    draw_bullet(c, LEFT_MARGIN + 15, y)
    c.drawString(LEFT_MARGIN + 25, y, "Classification predicts a category or class.")
    y -= 14
    draw_bullet(c, LEFT_MARGIN + 15, y)
    c.drawString(LEFT_MARGIN + 25, y, "Regression predicts a numerical value.")
    y -= 14

    ml_p5 = ("The appropriate task depends on the target variable selected for the borrower credit risk project.")
    y = draw_para(c, ml_p5, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    ml_p6 = ("Machine learning is useful for analysing banking datasets because multiple indicators may be related to loan default "
             "outcomes. However, a model's predictions depend on the quality and representativeness of the data used during training.")
    y = draw_para(c, ml_p6, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.3 Loan Default Prediction")
    y -= 16

    pred_p1 = ("Borrower-performance prediction involves estimating a loan applicant's credit risk outcome using relevant information "
               "available in a dataset.")
    y = draw_para(c, pred_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    pred_p2 = ("Depending on the project design, the input variables may include income, credit score, DTI ratio, savings, existing "
               "loans, or other financial indicators. The target variable represents an approval or default risk category.")
    y = draw_para(c, pred_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    c.drawString(LEFT_MARGIN, y, "A typical prediction process involves the following steps:")
    y -= 15
    c.drawString(LEFT_MARGIN + 15, y, "1.  Collect or load the relevant dataset.")
    y -= 14
    c.drawString(LEFT_MARGIN + 15, y, "2.  Inspect and prepare the data.")

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 8: CHAPTER-3 CONCEPTUAL BACKGROUND (PART 2)
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    steps = [
        "3.  Select the input features and target variable.",
        "4.  Train a suitable machine-learning model.",
        "5.  Evaluate the trained model.",
        "6.  Apply the model to new input information.",
        "7.  Display the prediction to the user."
    ]
    c.setFont("Times-Roman", 10.5)
    for s in steps:
        c.drawString(LEFT_MARGIN + 15, y, s)
        y -= 15

    y -= 6
    p_step_note = ("The exact variables and prediction target must correspond to the dataset and code used in SmartCredit.")
    y = draw_para(c, p_step_note, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    p_step_note2 = ("Borrower-performance prediction should be interpreted carefully. A predicted outcome is an estimate and "
                    "cannot guarantee a borrower's actual future repayment behavior.")
    y = draw_para(c, p_step_note2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.4 Early Warning System")
    y -= 16

    ew_p1 = ("An early warning system is designed to identify potential concerns before they develop into more serious problems. "
             "In financial environments, such a system can help highlight loan applicants who may require closer scrutiny.")
    y = draw_para(c, ew_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    ew_p2 = ("An early-warning system may use model predictions, predefined rules, or a combination of both. Depending on its "
             "implementation, it may assign categories such as low, medium, or high risk.")
    y = draw_para(c, ew_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    ew_p3 = ("The warning category should be interpreted according to the logic used in the application. If the system uses thresholds, "
             "those thresholds should be documented and evaluated rather than treated as universally correct.")
    y = draw_para(c, ew_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    ew_p4 = ("The primary purpose of an underwriting early-warning system is to support timely and constructive intervention. It "
             "should encourage further review and assistance rather than label an applicant permanently.")
    y = draw_para(c, ew_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.5 Data Collection and Data Preprocessing")
    y -= 16

    dp_p1 = ("Data preparation is an important stage in machine learning because raw data may contain missing values, inconsistent "
             "formats, duplicate records, or unsuitable data types.")
    y = draw_para(c, dp_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    dp_p2 = ("Data preprocessing converts the original dataset into a consistent structure suitable for model training and prediction.")
    y = draw_para(c, dp_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 8

    c.drawString(LEFT_MARGIN, y, "Common preprocessing operations include:")
    y -= 16

    ops = [
        ("Data inspection: ", "Understanding the number of records, column names, data types, and general structure of the dataset."),
        ("Handling missing values: ", "Identifying incomplete records and applying an appropriate imputation strategy (median/mode)."),
        ("Duplicate checking: ", "Identifying repeated records where duplicates could affect the analysis."),
        ("Feature selection: ", "Selecting the variables relevant to the prediction task."),
        ("Encoding: ", "Converting categorical values into numerical representations when required."),
        ("Feature scaling: ", "Transforming numerical features when the selected algorithm requires or benefits from scaling.")
    ]
    for tag, desc in ops:
        c.setFont("Times-Bold", 10.5)
        c.drawString(LEFT_MARGIN, y, tag)
        tw = c.stringWidth(tag, "Times-Bold", 10.5)
        c.setFont("Times-Roman", 10.5)
        lines = simpleSplit(desc, "Times-Roman", 10.5, CONTENT_WIDTH - tw)
        c.drawString(LEFT_MARGIN + tw, y, lines[0])
        y -= 14
        for sub_l in lines[1:]:
            c.drawString(LEFT_MARGIN, y, sub_l)
            y -= 14
        y -= 3

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 9: CHAPTER-3 CONCEPTUAL BACKGROUND (PART 3)
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    c.setFont("Times-Roman", 10.5)
    p_top = ("The preprocessing steps used during prediction must remain consistent with those used during model training. "
             "Otherwise, the model may receive inputs in an unexpected format and generate unreliable results or errors.")
    y = draw_para(c, p_top, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.6 Model Training and Evaluation")
    y -= 16

    mte_p1 = ("Model training is the process through which a machine-learning algorithm learns patterns from training data. "
              "After training, the model is evaluated to estimate how well it performs on data that was not used to fit the model.")
    y = draw_para(c, mte_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    mte_p2 = ("A common approach is to divide a dataset into training and testing subsets. The training subset is used to fit "
              "the model, while the testing subset is used to assess its performance.")
    y = draw_para(c, mte_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    mte_p3 = ("Evaluation metrics depend on the type of prediction task.")
    y = draw_para(c, mte_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    mte_p4 = ("For classification tasks, commonly used metrics include accuracy, precision, recall, F1-score, and a confusion matrix.")
    y = draw_para(c, mte_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    mte_p5 = ("For regression tasks, commonly used metrics include Mean Absolute Error (MAE), Mean Squared Error (MSE), "
              "and the coefficient of determination (R^2).")
    y = draw_para(c, mte_p5, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    mte_p6 = ("The appropriate metrics depend on the target variable and the consequences of incorrect predictions. In an early-warning application, "
              "recall is prioritized to minimize costly false negatives.")
    y = draw_para(c, mte_p6, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.7 Python Programming Language")
    y -= 16

    py_p1 = ("Python is a high-level programming language widely used in data analysis, automation, web development, and machine learning.")
    y = draw_para(c, py_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    py_p2 = ("Python has a readable syntax and a large ecosystem of libraries. These characteristics make it suitable for developing "
             "data-driven applications and machine-learning prototypes.")
    y = draw_para(c, py_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    py_p3 = ("In SmartCredit, Python is used for application logic and for connecting the user interface with the data-processing "
             "and prediction components.")
    y = draw_para(c, py_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    py_p4 = ("Its library ecosystem also makes it easier to organise the project into separate functions for input handling, "
             "preprocessing, prediction, and result presentation.")
    y = draw_para(c, py_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 14
    c.setFont("Times-Bold", 11.5)
    c.drawString(LEFT_MARGIN, y, "3.8 Streamlit Framework")
    y -= 16

    st_p1 = ("Streamlit is an open-source Python framework for developing interactive data applications.")
    y = draw_para(c, st_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    st_p2 = ("It allows developers to create application interfaces using Python code. Common interface elements include text fields, "
             "number inputs, selection controls, buttons, tables, and charts.")
    y = draw_para(c, st_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    st_p3 = ("Streamlit is useful for machine-learning projects because it can connect an existing Python model to an interface "
             "without requiring a separate front-end framework.")
    y = draw_para(c, st_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    st_p4 = ("In SmartCredit, Streamlit provides the interface through which the user interacts with the prediction system. "
             "It helps display input controls and prediction results in a convenient format.")
    y = draw_para(c, st_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 6

    st_p5 = ("The appearance and available features depend on the actual interface implemented in the project.")
    y = draw_para(c, st_p5, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 10: CHAPTER-4 IMPLEMENTATION (PART 1: CODING)
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter -4")
    y -= 18
    c.drawCentredString(W / 2, y, "Implementation")

    y -= 26
    code_p10 = [
        "from pathlib import Path",
        "import pickle",
        "import numpy as np",
        "import pandas as pd",
        "import streamlit as st",
        "",
        "# 1. Define Input Features",
        "FEATURE_COLUMNS = [",
        '    "Applicant_Income",',
        '    "Coapplicant_Income",',
        '    "Age",',
        '    "Dependents",',
        '    "Credit_Score",',
        '    "Existing_Loans",',
        '    "DTI_Ratio",',
        '    "Savings",',
        '    "Collateral_Value",',
        '    "Loan_Amount",',
        '    "Loan_Term",',
        '    "total_income",',
        '    "income_loan_ratio",',
        '    "high_dti",',
        '    "low_savings",',
        '    "high_loan_ratio",',
        "]",
        "",
        "CATEGORICAL_COLUMNS = [",
        '    "Employment_Status",',
        '    "Marital_Status",',
        '    "Loan_Purpose",',
        '    "Property_Area",',
        '    "Education_Level",',
        '    "Gender",',
        '    "Employer_Category",',
        "]",
        "",
        "# 2. Load Trained Model and Preprocessing Files",
        "@st.cache_resource",
        "def load_artifacts(model_dir_string):",
        "    model_dir = Path(model_dir_string)",
        "    filenames = {",
        '        "model": "best_model.joblib",',
        '        "feature_cols": "feature_columns.joblib",',
        '        "decision_tree": "decision_tree.pkl",'
    ]
    c.setFont("Courier", 9.5)
    for line in code_p10:
        c.drawString(LEFT_MARGIN, y, line)
        y -= 14

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 11: CHAPTER-4 IMPLEMENTATION (PART 2: CODING)
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    code_p11 = [
        '        "logistic": "logistic_regression.pkl",',
        "    }",
        "    artifacts = {}",
        "    for key, filename in filenames.items():",
        "        path = model_dir / filename",
        "        if not path.is_file():",
        '            return None, f"File not found: {path}"',
        "        try:",
        "            import joblib",
        "            artifacts[key] = joblib.load(path)",
        "        except Exception:",
        "            try:",
        '                with path.open("rb") as file:',
        "                    artifacts[key] = pickle.load(file)",
        "            except Exception as exc:",
        '                return None, f"Unable to load {filename}: {exc}"',
        '        if not hasattr(artifacts["model"], "predict"):',
        '            return None, "Invalid model file."',
        "    return artifacts, None",
        "",
        "# 3. Validate Borrower Input",
        "def validate_input(input_df):",
        "    if not isinstance(input_df, pd.DataFrame):",
        '        raise ValueError("Input must be a DataFrame.")',
        "    if input_df.empty:",
        '        raise ValueError("Enter applicant details.")',
        "    missing = [",
        "        col for col in FEATURE_COLUMNS",
        "        if col not in input_df.columns",
        "    ]",
        "    if missing:",
        '        raise ValueError(f"Missing features: {missing}")',
        "    numeric_ranges = {",
        '        "Applicant_Income": (1000, 500000),',
        '        "Credit_Score": (300, 900),',
        '        "Loan_Amount": (5000, 1000000),'
    ]
    c.setFont("Courier", 9.5)
    for line in code_p11:
        c.drawString(LEFT_MARGIN, y, line)
        y -= 14

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 12: CHAPTER-4 IMPLEMENTATION (PART 3: CODING)
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    code_p12 = [
        '        "DTI_Ratio": (0.0, 1.5),',
        '        "Savings": (0, 500000),',
        '        "Collateral_Value": (0, 2000000),',
        "    }",
        "    for column, (minimum, maximum) in numeric_ranges.items():",
        "        value = pd.to_numeric(",
        "            input_df.iloc[0][column],",
        '            errors="coerce",',
        "        )",
        "        if pd.isna(value) or not np.isfinite(value):",
        '            raise ValueError(f"Invalid value for {column}.")',
        "        if not minimum <= value <= maximum:",
        '            raise ValueError(f"Out-of-range value for {column}.")',
        "    for column in CATEGORICAL_COLUMNS:",
        "        if pd.isna(input_df.iloc[0][column]):",
        '            raise ValueError(f"Select {column}.")',
        "",
        "# 4. Encode Categorical Features",
        "    except (ValueError, TypeError, IndexError):",
        "        pass",
        "    return str(prediction)",
        "",
        "# 6. Determine Early-Warning Category",
        "def get_risk_level(prob):",
        "    prob = float(prob)",
        "    if prob < 0.30:",
        '        return "Low", "Approved with standard prime interest rate."',
        "    elif prob < 0.60:",
        '        return "Moderate", "Conditional approval; collateral review recommended."',
        "    elif prob >= 0.60:",
        '        return "High", "Declined; default probability exceeds threshold."',
        '    return "Review", "Discuss the result with a credit supervisor."',
        "",
        'elif page == "Predict Loan Risk":',
        '    with st.form("loan_form"):',
        '        income = st.number_input("Applicant Income", 1000.0, 500000.0, 25000.0)',
        '        cibil = st.number_input("Credit Score (CIBIL)", 300.0, 900.0, 720.0)'
    ]
    c.setFont("Courier", 9.5)
    for line in code_p12:
        c.drawString(LEFT_MARGIN, y, line)
        y -= 14

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 13: CHAPTER-4 IMPLEMENTATION (PART 4: CODING)
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    code_p13 = [
        '        coapplicant = st.number_input("Co-applicant Income", 0.0, 200000.0, 5000.0)',
        '        loan_amount = st.number_input("Loan Amount", 5000.0, 1000000.0, 150000.0)',
        '        loan_term = st.selectbox("Loan Term (Months)", [12, 24, 36, 48, 60, 72, 84])',
        '        existing_loans = st.number_input("Existing Active Loans", 0, 10, 1)',
        '        savings = st.number_input("Savings Cushion", 0.0, 500000.0, 15000.0)',
        '        collateral = st.number_input("Collateral Value", 0.0, 2000000.0, 75000.0)',
        "",
        '        employment = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Contract", "Unemployed"])',
        '        education = st.selectbox("Education Level", ["Graduate", "Not Graduate"])',
        '        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])',
        '        loan_purpose = st.selectbox("Loan Purpose", ["Personal", "Car", "Business", "Home", "Education"])',
        '        submitted = st.form_submit_button("Predict Loan Risk")',
        "",
        "    if submitted and artifacts is not None:",
        "        borrower_data = pd.DataFrame([{",
        '            "Applicant_Income": income,',
        '            "Coapplicant_Income": coapplicant,',
        '            "Credit_Score": cibil,',
        '            "Loan_Amount": loan_amount,',
        '            "Loan_Term": loan_term,',
        '            "Existing_Loans": existing_loans,',
        '            "Savings": savings,',
        '            "Collateral_Value": collateral,',
        '            "Employment_Status": employment,',
        '            "Education_Level": education,',
        '            "Property_Area": property_area,',
        '            "Loan_Purpose": loan_purpose,'
    ]
    c.setFont("Courier", 9.5)
    for line in code_p13:
        c.drawString(LEFT_MARGIN, y, line)
        y -= 14

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 14: FLOW CHART
    # ══════════════════════════════════════════════════════════════════════════
    if os.path.exists(FLOWCHART_PATH):
        # Draw vertical flowchart centered
        c.drawImage(FLOWCHART_PATH, (W - 380) / 2, 70, width=380, height=690, preserveAspectRatio=True)

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 15: CHAPTER-5 USER INTERFACES
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-5")
    y -= 18
    c.drawCentredString(W / 2, y, "User Interfaces")

    y -= 26
    c.setFont("Times-Roman", 10.5)
    ui_desc1 = ("The SmartCredit dashboard displays loan portfolio statistics, model accuracy benchmarks, "
                "early-warning risk indicators, and a borrower performance prediction form.")
    y = draw_para(c, ui_desc1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 10
    if os.path.exists(UI_FIG1_PATH):
        c.drawImage(UI_FIG1_PATH, (W - 380) / 2, y - 200, width=380, height=200, preserveAspectRatio=True)
        y -= 215

    c.setFont("Times-Bold", 11)
    c.drawCentredString(W / 2, y, "(Fig 5.1)")
    y -= 25

    ui_desc2 = ("The prediction interface accepts financial and demographic parameters and displays the "
                "predicted credit approval status, risk level tier, and suggested next underwriting steps.")
    y = draw_para(c, ui_desc2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    y -= 10
    if os.path.exists(UI_FIG2_PATH):
        c.drawImage(UI_FIG2_PATH, (W - 380) / 2, y - 200, width=380, height=200, preserveAspectRatio=True)
        y -= 215

    c.setFont("Times-Bold", 11)
    c.drawCentredString(W / 2, y, "(Fig 5.2)")

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 16: CHAPTER-6 CONCLUSION
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    c.setFont("Times-Bold", 14)
    c.drawCentredString(W / 2, y, "Chapter-6")
    y -= 18
    c.drawCentredString(W / 2, y, "Conclusion")

    y -= 28
    conc_p1 = ("The AI-Driven Loan Default Prediction and Risk Scoring System demonstrates the application of Python, "
               "data processing, and machine-learning techniques in the financial and retail banking sector.")
    y = draw_para(c, conc_p1, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 10

    conc_p2 = ("The project provides a workflow through which borrower credit information can be entered, processed, "
               "and passed to a trained classification model for prediction. The resulting output can be presented through "
               "an interactive interface, together with early-warning risk tiers and safe loan limit recommendations where "
               "supported by the implementation.")
    y = draw_para(c, conc_p2, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 10

    conc_p3 = ("The project illustrates how machine learning can contribute to credit risk analytics by helping users review "
               "borrower creditworthiness in an organised, objective manner. It also provides practical experience in developing "
               "a Python-based application and connecting a machine-learning workflow to an interactive user interface.")
    y = draw_para(c, conc_p3, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
    y -= 10

    conc_p4 = ("However, the usefulness of the system depends on the quality of the data, the suitability of the selected model, "
               "and the validity of its evaluation. The generated predictions should be interpreted as probabilistic estimates and "
               "should support rather than replace the sound professional judgement of credit underwriters and loan officers.")
    y = draw_para(c, conc_p4, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)

    c.showPage()

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 17: REFERENCES
    # ══════════════════════════════════════════════════════════════════════════
    y = H - 75
    c.setFont("Times-Bold", 15)
    c.drawCentredString(W / 2, y, "References")

    y -= 40
    c.setFont("Times-Roman", 10.5)

    refs = [
        '[1] Streamlit, "Streamlit Documentation." Available: https://docs.streamlit.io/',
        '[2] pandas Development Team, "pandas Documentation." Available: https://pandas.pydata.org/docs/',
        '[3] NumPy Developers, "NumPy Documentation." Available: https://numpy.org/doc/',
        '[4] scikit-learn Developers, "scikit-learn User Guide." Available: https://scikit-learn.org/stable/user_guide.html',
        '[5] Joblib Developers, "Joblib Documentation." Available: https://joblib.readthedocs.io/',
        '[6] Reserve Bank of India (RBI), "Master Direction - Non-Banking Financial Company Directions," 2016.',
        '[7] L. Breiman, "Random Forests," Machine Learning, vol. 45, no. 1, pp. 5-32, 2001.'
    ]

    for ref in refs:
        y = draw_para(c, ref, LEFT_MARGIN, y, font="Times-Roman", font_size=10.5, leading=14.5)
        y -= 12

    c.save()
    
    # Copy to workspace root
    import shutil
    shutil.copyfile(OUTPUT_PDF, WORKSPACE_PDF)
    print(f"PDF generated successfully at: {OUTPUT_PDF} and {WORKSPACE_PDF}")


if __name__ == "__main__":
    build_report()
