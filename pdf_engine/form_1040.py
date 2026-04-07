from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

def build_form_1040(data):
    content = []

    content.append(Paragraph("FORM 1040 - U.S. Individual Income Tax Return (2024)", styles['Title']))
    content.append(Spacer(1, 12))

    # Table Data
    table_data = [
        ["Field", "Value"],
        ["Name", f"{data['name']} & {data['spouse']}"],
        ["SSN", data['ssn']],
        ["Wages", data['wages']],
        ["Interest", data['interest']],
        ["Dividends", data['dividends']],
        ["Business Income", data['business_income']],
        ["Total Income", data['total_income']],
        ["AGI", data['agi']],
        ["Taxable Income", data['taxable_income']],
        ["Tax", data['tax']],
        ["Tax Withheld", data['tax_withheld']],
        ["Amount Owed", data['amount_owed']]
    ]

    table = Table(table_data, colWidths=[200, 200])

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    content.append(table)
    content.append(Spacer(1, 20))

    return content