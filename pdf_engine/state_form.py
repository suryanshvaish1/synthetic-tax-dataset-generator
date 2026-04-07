from reportlab.platypus import Table, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.platypus import TableStyle


def generate_state_form(path, data, state):
    doc = SimpleDocTemplate(path)

    table_data = [
        [f"{state} STATE TAX RETURN", ""],
        ["Name", data["name"]],
        ["SSN", data["ssn"]],
        ["Total Income", data["total_income"]],
        ["Taxable Income", data["taxable_income"]],
        ["State Tax (approx)", int(data["tax"] * 0.5)]
    ]

    table = Table(table_data)

    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey)
    ]))

    doc.build([table])