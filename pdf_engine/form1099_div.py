from reportlab.pdfgen import canvas

def create_1099_div(path, income):
    c = canvas.Canvas(path)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "FORM 1099-DIV")

    c.setFont("Helvetica", 12)
    c.drawString(100, 710, "Recipient: Synthetic User")
    c.drawString(100, 680, f"Dividend Income: ${income['dividend']}")
    c.drawString(100, 650, "Payer: ABC Investments")

    c.line(100, 740, 400, 740)

    c.save()