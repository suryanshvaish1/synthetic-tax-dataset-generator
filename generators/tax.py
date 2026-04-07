import random

def calculate_tax(data):
    tax = int(data["taxable_income"] * 0.1)  # simple logic
    tax_withheld = random.randint(2000, 10000)
    child_tax_credit = random.choice([0, 1000, 2000, 2500])

    amount_owed = tax - tax_withheld

    return {
        "tax": tax,
        "tax_withheld": tax_withheld,
        "child_tax_credit": child_tax_credit,
        "amount_owed": amount_owed
    }