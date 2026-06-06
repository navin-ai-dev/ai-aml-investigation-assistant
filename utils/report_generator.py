

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(content):

    pdf_name = "sar_report.pdf"

    doc = SimpleDocTemplate(pdf_name)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Suspicious Activity Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            content.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(elements)

    return pdf_name