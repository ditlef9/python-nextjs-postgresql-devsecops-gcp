import reportlab
from reportlab.pdfgen import canvas


def x_save_pdf(c: reportlab.pdfgen.canvas.Canvas):

    # Save the PDF
    print("b_create_tmp() · Saving PDF")
    c.save()


