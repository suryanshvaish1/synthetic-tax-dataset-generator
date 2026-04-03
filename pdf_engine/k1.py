from reportlab.pdfgen import canvas

def create_k1(path, income):
    c = canvas.Canvas(path)

    k1 = income.get("k1_income", 3000)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(180, 780, "Schedule K-1")

    c.drawString(100, 720, f"Partnership Income: ${k1}")

    c.save()