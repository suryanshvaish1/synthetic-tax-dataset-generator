from reportlab.pdfgen import canvas

def create_schedule_e(path, income):
    c = canvas.Canvas(path)

    rental = income.get("rental", 0)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(150, 780, "Schedule E - Rental Income")

    c.drawString(100, 720, f"Rental Income: ${rental}")

    c.save()