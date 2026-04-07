def build_schedule_se():
    from reportlab.platypus import Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet

    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("SCHEDULE SE - SELF EMPLOYMENT TAX", styles['Heading2']))
    content.append(Paragraph("SE Tax: 6034", styles['Normal']))
    content.append(Paragraph("Deduction: 3017", styles['Normal']))
    content.append(Spacer(1, 20))

    return content