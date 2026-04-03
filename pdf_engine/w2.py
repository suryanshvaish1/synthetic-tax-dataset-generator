from reportlab.pdfgen import canvas

def create_w2(path, profile, income):
    c = canvas.Canvas(path)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, 750, "FORM W-2")

    # Divider
    c.line(100, 740, 450, 740)

    # Employee Info
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Employee Name: {profile['name']}")
    c.drawString(100, 680, f"SSN: {profile['ssn']}")

    # Income Section
    c.drawString(100, 640, f"Wages: ${income['w2']}")
    c.drawString(100, 620, f"Federal Tax Withheld: ${round(income['w2'] * 0.1, 2)}")

    # Footer
    c.drawString(100, 580, "Employer: ABC Corporation")

    c.save()