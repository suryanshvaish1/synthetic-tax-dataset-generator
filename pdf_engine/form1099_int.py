from reportlab.pdfgen import canvas

def create_1099_int(path, profile, income):
    c = canvas.Canvas(path)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, 750, "FORM 1099-INT")

    # Divider line
    c.line(100, 740, 450, 740)

    # Recipient Info
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Recipient: {profile['name']}")
    c.drawString(100, 680, f"SSN: {profile['ssn']}")

    # Income Details
    c.drawString(100, 640, f"Interest Income: ${income['interest']}")
    c.drawString(100, 620, f"Federal Tax Withheld: ${round(income['interest'] * 0.1, 2)}")

    # Payer Info
    c.drawString(100, 580, "Payer: XYZ Bank Corporation")

    # Footer
    c.drawString(100, 540, "This is a synthetic tax document for testing.")

    c.save()