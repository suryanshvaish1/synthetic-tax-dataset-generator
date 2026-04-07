from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.lib import colors


def generate_w2(path, data):
    doc = SimpleDocTemplate(path)

    table_data = [
        ["Form W-2", "Wage and Tax Statement"],
        ["Employee", data["name"]],
        ["SSN", data["ssn"]],
        ["Wages", data["wages"]],
        ["Federal Tax Withheld", data["tax_withheld"]]
    ]

    table = Table(table_data)

    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey)
    ]))

    doc.build([table])


def generate_1099_int(path, data):
    doc = SimpleDocTemplate(path)

    table_data = [
        ["Form 1099-INT", "Interest Income"],
        ["Recipient", data["name"]],
        ["Interest", data["interest"]]
    ]

    table = Table(table_data)

    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ]))

    doc.build([table])


def generate_1099_div(path, data):
    doc = SimpleDocTemplate(path)

    table_data = [
        ["Form 1099-DIV", "Dividends"],
        ["Recipient", data["name"]],
        ["Dividends", data["dividends"]]
    ]

    table = Table(table_data)

    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ]))

    doc.build([table])