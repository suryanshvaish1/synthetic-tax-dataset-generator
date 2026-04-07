from reportlab.pdfgen import canvas

def create_1098(path, income):
    c = canvas.Canvas(path)

    mortgage = income.get("mortgage_interest", 2000)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(180, 780, "FORM 1098")

    c.drawString(100, 720, f"Mortgage Interest: ${mortgage}")

    c.save()