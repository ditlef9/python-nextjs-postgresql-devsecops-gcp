from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_with_image(pdf_filename, image_path):
    # Create a PDF file with letter-sized page
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Set up the coordinates for placing the image
    # x = 100, y = 500: The image will be placed at (100, 500) on the page.
    c.drawImage(image_path, 100, 500, width=400, height=300)

    # Optionally, you can add some text to the PDF
    c.setFont("Helvetica", 12)
    c.drawString(100, 480, "This is an image inserted into the PDF")

    # Save the PDF
    c.save()

