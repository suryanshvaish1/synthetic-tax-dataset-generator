from reportlab.pdfgen import canvas

def create_8949(path, income):
    c = canvas.Canvas(path)

    gain = income.get("capital_gain", 0)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(150, 780, "Form 8949")

    c.drawString(100, 720, f"Transaction Gain/Loss: ${gain}")

    c.save()