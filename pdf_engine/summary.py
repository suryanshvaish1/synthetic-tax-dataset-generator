from reportlab.pdfgen import canvas

def create_summary(path, profile, income):
    # -------- CALCULATIONS --------
    total_income = sum(income.values())

    # Basic deductions (simulated)
    standard_deduction = 13850
    taxable_income = max(0, total_income - standard_deduction)

    # Simple tax calculation
    tax = taxable_income * 0.1

    # Simulated payments (withholding etc.)
    payments = total_income * 0.08

    # Refund or amount due
    refund_or_due = payments - tax

    # Effective tax rate
    effective_rate = (tax / total_income) if total_income else 0

    # -------- PDF --------
    c = canvas.Canvas(path)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, 780, "EXECUTIVE SUMMARY")

    # Divider
    c.line(80, 770, 500, 770)

    c.setFont("Helvetica", 12)

    # -------- PERSONAL INFO --------
    c.drawString(100, 740, f"Name: {profile['name']}")
    c.drawString(100, 720, f"State: {profile['state']}")
    c.drawString(100, 700, f"Filing Status: {profile['filing_status']}")

    # -------- FEDERAL SUMMARY --------
    c.setFont("Helvetica-Bold", 13)
    c.drawString(100, 660, "Federal Summary")

    c.setFont("Helvetica", 12)
    c.drawString(120, 640, f"Total Income (AGI): ${round(total_income,2)}")
    c.drawString(120, 620, f"Standard Deduction: ${standard_deduction}")
    c.drawString(120, 600, f"Taxable Income: ${round(taxable_income,2)}")
    c.drawString(120, 580, f"Total Tax: ${round(tax,2)}")
    c.drawString(120, 560, f"Total Payments: ${round(payments,2)}")

    # Refund / Due
    status = "Refund" if refund_or_due > 0 else "Amount Due"
    c.drawString(120, 540, f"{status}: ${round(abs(refund_or_due),2)}")

    c.drawString(120, 520, f"Effective Tax Rate: {round(effective_rate*100,2)}%")

    # -------- STATE SUMMARY --------
    c.setFont("Helvetica-Bold", 13)
    c.drawString(100, 480, "State Summary")

    state_tax = total_income * 0.05

    c.setFont("Helvetica", 12)
    c.drawString(120, 460, f"State Taxable Income: ${round(total_income,2)}")
    c.drawString(120, 440, f"State Tax: ${round(state_tax,2)}")
    c.drawString(120, 420, f"State Payments: ${round(state_tax * 0.9,2)}")

    state_balance = (state_tax * 0.9) - state_tax
    state_status = "Refund" if state_balance > 0 else "Amount Due"

    c.drawString(120, 400, f"{state_status}: ${round(abs(state_balance),2)}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(100, 360, "Note: This is a synthetic dataset generated for testing purposes.")

    c.save()