from reportlab.pdfgen import canvas

def create_1099_b(path, income):
    c = canvas.Canvas(path)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(180, 780, "FORM 1099-B")

    gain = income.get("capital_gain", 0)

    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Capital Gain/Loss: ${gain}")

    c.save()