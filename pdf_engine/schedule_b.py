from reportlab.pdfgen import canvas

def create_schedule_b(path, income):
    c = canvas.Canvas(path)
    c.drawString(100, 750, "Schedule B")
    c.drawString(100, 720, f"Interest: {income['interest']}")
    c.drawString(100, 700, f"Dividend: {income['dividend']}")
    c.save()