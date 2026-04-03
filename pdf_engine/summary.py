from reportlab.pdfgen import canvas

def create_summary(path, profile, income):
    total_income = income["w2"] + income["interest"] + income["dividend"]
    tax = total_income * 0.1
    effective_rate = (tax / total_income) if total_income else 0

    c = canvas.Canvas(path)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "EXECUTIVE SUMMARY")

    c.line(100, 740, 450, 740)

    # User Info
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Name: {profile['name']}")

    # Summary
    c.drawString(100, 660, f"Total Income: ${total_income}")
    c.drawString(100, 640, f"Estimated Tax: ${round(tax, 2)}")
    c.drawString(100, 620, f"Effective Tax Rate: {round(effective_rate * 100, 2)}%")

    # Footer Note
    c.drawString(100, 580, "This is a synthetic dataset for testing purposes.")

    c.save()