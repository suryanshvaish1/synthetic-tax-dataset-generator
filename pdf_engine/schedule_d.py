from reportlab.pdfgen import canvas

def create_schedule_d(path, income):
    c = canvas.Canvas(path)

    gain = income.get("capital_gain", 0)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(150, 780, "Schedule D - Capital Gains")

    c.drawString(100, 720, f"Capital Gain/Loss: ${gain}")

    c.save()