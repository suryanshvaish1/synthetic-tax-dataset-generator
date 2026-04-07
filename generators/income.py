import random

def generate_income():
    return {
        "wages": random.randint(30000, 100000),
        "interest": random.randint(100, 2000),
        "dividends": random.randint(500, 5000),
        "business_income": random.randint(10000, 60000)
    }


def calculate_income(income):
    total_income = (
        income["wages"]
        + income["interest"]
        + income["dividends"]
        + income["business_income"]
    )

    adjustments = random.randint(1000, 5000)
    agi = total_income - adjustments

    standard_deduction = 29200
    taxable_income = agi - standard_deduction

    return {
        **income,
        "total_income": total_income,
        "adjustments": adjustments,
        "agi": agi,
        "standard_deduction": standard_deduction,
        "taxable_income": taxable_income
    }