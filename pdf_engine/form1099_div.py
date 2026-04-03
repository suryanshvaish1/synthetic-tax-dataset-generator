from reportlab.pdfgen import canvas

def create_1099_div(path, profile, income):
    c = canvas.Canvas(path)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(180, 780, "FORM 1099-DIV")

    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Recipient: {profile['name']}")
    c.drawString(100, 700, f"Dividend Income: ${income['dividend']}")
    c.drawString(100, 680, f"Tax Withheld: ${round(income['dividend'] * 0.1, 2)}")

    c.save()