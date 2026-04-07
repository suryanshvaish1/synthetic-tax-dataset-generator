from reportlab.pdfgen import canvas
import random


# 🔥 TAX LOGIC (INTEGRATED HERE)
def calculate_tax(income):
    ti = income["taxable_income"]

    if ti <= 11000:
        tax = ti * 0.10
    elif ti <= 44725:
        tax = 1100 + (ti - 11000) * 0.12
    elif ti <= 95375:
        tax = 5147 + (ti - 44725) * 0.22
    else:
        tax = 16290 + (ti - 95375) * 0.24

    credits = 2500
    total_tax = max(0, tax - credits)

    payments = random.randint(5000, 10000)

    return {
        "tax": round(tax, 2),
        "credits": credits,
        "total_tax": round(total_tax, 2),
        "payments": payments,
        "refund": max(0, payments - total_tax),
        "amount_owed": max(0, total_tax - payments),
    }


# 🔥 UPDATED SUMMARY FUNCTION
def create_summary(path, profile, income):

    # -------- USE PRE-CALCULATED VALUES --------
    total_income = income["total_income"]
    agi = income["agi"]
    standard_deduction = income["standard_deduction"]
    taxable_income = income["taxable_income"]

    # 🔥 USE REAL TAX LOGIC
    tax_data = calculate_tax(income)

    tax = tax_data["tax"]
    credits = tax_data["credits"]
    total_tax = tax_data["total_tax"]
    payments = tax_data["payments"]
    refund = tax_data["refund"]
    amount_owed = tax_data["amount_owed"]

    effective_rate = (total_tax / total_income) if total_income else 0

    # -------- PDF --------
    c = canvas.Canvas(path)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, 780, "EXECUTIVE SUMMARY")

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
    c.drawString(120, 640, f"Total Income (Line 9): ${round(total_income,2)}")
    c.drawString(120, 620, f"Adjusted Gross Income (Line 11): ${round(agi,2)}")
    c.drawString(120, 600, f"Standard Deduction (Line 12): ${standard_deduction}")
    c.drawString(120, 580, f"Taxable Income (Line 15): ${round(taxable_income,2)}")

    c.drawString(120, 560, f"Tax Before Credits (Line 16): ${round(tax,2)}")
    c.drawString(120, 540, f"Credits (Line 19): ${credits}")
    c.drawString(120, 520, f"Total Tax (Line 24): ${round(total_tax,2)}")

    c.drawString(120, 500, f"Total Payments (Line 33): ${round(payments,2)}")

    # Refund / Due
    if refund > 0:
        c.drawString(120, 480, f"Refund (Line 34): ${round(refund,2)}")
    else:
        c.drawString(120, 480, f"Amount Owed (Line 37): ${round(amount_owed,2)}")

    c.drawString(120, 460, f"Effective Tax Rate: {round(effective_rate*100,2)}%")

    # -------- STATE SUMMARY --------
    c.setFont("Helvetica-Bold", 13)
    c.drawString(100, 420, "State Summary")

    state_tax = total_income * 0.05
    state_payment = state_tax * 0.9
    state_balance = state_payment - state_tax

    c.setFont("Helvetica", 12)
    c.drawString(120, 400, f"State Taxable Income: ${round(total_income,2)}")
    c.drawString(120, 380, f"State Tax: ${round(state_tax,2)}")
    c.drawString(120, 360, f"State Payments: ${round(state_payment,2)}")

    if state_balance > 0:
        c.drawString(120, 340, f"Refund: ${round(state_balance,2)}")
    else:
        c.drawString(120, 340, f"Amount Due: ${round(abs(state_balance),2)}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(100, 300, "Note: Synthetic dataset aligned with IRS Form 1040 structure.")

    c.save()