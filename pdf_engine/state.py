from reportlab.pdfgen import canvas

def create_state(path, income):
    tax = income["w2"] * 0.05

    c = canvas.Canvas(path)
    c.drawString(100, 750, "State Tax")
    c.drawString(100, 720, f"Tax: {tax}")
    c.save()