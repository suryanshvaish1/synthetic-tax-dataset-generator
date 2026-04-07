def build_schedule_c():
    from reportlab.platypus import Table
    from reportlab.lib import colors
    from reportlab.platypus import TableStyle

    data = [
        ["Schedule C", "Profit or Loss from Business"],
        ["Business Name", "Johnson Creative Studios"],
        ["Income", "80000"],
        ["Expenses", "37300"],
        ["Net Profit", "42700"]
    ]

    table = Table(data)

    table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black)
    ]))

    return [table]