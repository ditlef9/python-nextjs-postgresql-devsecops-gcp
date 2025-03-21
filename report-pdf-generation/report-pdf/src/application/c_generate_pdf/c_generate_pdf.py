from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def c_generate_pdf(pdf_file_full_path: str, datetime_ymdhms_saying: str):
    """
    Generates a PDF with a front page containing a title, subtitle, and date.

    :param pdf_file_full_path: Full path where the PDF will be saved.
    :return: ReportLab canvas object.
    """

    # Create a PDF canvas
    c = canvas.Canvas(pdf_file_full_path, pagesize=A4)
    width, height = A4  # Get page dimensions

    # Set title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, height - 150, "Asset Security Report")

    # Set subtitle
    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2, height - 200, "Generated Vulnerability Report")

    # Set date
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 250, f"{datetime_ymdhms_saying}")

    # Add a line separator
    c.line(100, height - 270, width - 100, height - 270)

    # Show the front page - new page command
    c.showPage()

    return c
