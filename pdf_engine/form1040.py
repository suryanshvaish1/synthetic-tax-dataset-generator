from reportlab.pdfgen import canvas

def create_1040(path, profile, income):
    total_income = income["w2"] + income["interest"] + income["dividend"]
    standard_deduction = 13850
    taxable_income = max(0, total_income - standard_deduction)
    tax = taxable_income * 0.1

    c = canvas.Canvas(path)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, 750, "FORM 1040 - U.S. Individual Income Tax Return")

    c.line(80, 740, 500, 740)

    # Personal Info
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Name: {profile['name']}")

    # Income Section
    c.drawString(100, 660, "Income Details:")
    c.drawString(120, 640, f"Wages: ${income['w2']}")
    c.drawString(120, 620, f"Interest: ${income['interest']}")
    c.drawString(120, 600, f"Dividends: ${income['dividend']}")

    # Calculation
    c.drawString(100, 560, f"Total Income: ${total_income}")
    c.drawString(100, 540, f"Standard Deduction: ${standard_deduction}")
    c.drawString(100, 520, f"Taxable Income: ${taxable_income}")
    c.drawString(100, 500, f"Tax Liability: ${round(tax, 2)}")

    c.save()