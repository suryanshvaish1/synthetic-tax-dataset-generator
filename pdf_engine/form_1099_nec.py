from reportlab.pdfgen import canvas

def create_1099_nec(path, income):
    c = canvas.Canvas(path)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(180, 780, "FORM 1099-NEC")

    c.drawString(100, 720, f"Non-Employee Income: ${income.get('business', 0)}")

    c.save()