from reportlab.pdfgen import canvas

def create_schedule_c(path, income):
    c = canvas.Canvas(path)

    business = income.get("business", 0)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(150, 780, "Schedule C - Business Income")

    c.drawString(100, 720, f"Business Income: ${business}")
    c.drawString(100, 700, f"Expenses: ${round(business * 0.3, 2)}")
    c.drawString(100, 680, f"Net Profit: ${round(business * 0.7, 2)}")

    c.save()