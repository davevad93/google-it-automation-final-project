#!/usr/bin/env python3

# Import the required modules
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Define the generate_report function
def generate_report(attachment, title, paragraph):
    """Generates a PDF report with the given title and paragraph."""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)
    # Build the PDF document
    report.build([report_title, empty_line, report_info])
    