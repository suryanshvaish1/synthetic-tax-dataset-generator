import random

def generate_income(level):
    # Base income (Level 1 - Easy)
    data = {
        "w2": random.randint(30000, 120000),
        "interest": random.randint(0, 2000),
        "dividend": random.randint(0, 1500)
    }

    # Level 2 - Medium complexity
    if level in ["medium", "complex"]:
        data["business"] = random.randint(5000, 40000)          # 1099-NEC
        data["retirement"] = random.randint(0, 20000)           # 1099-R
        data["unemployment"] = random.randint(0, 10000)

    # Level 3 - Complex
    if level == "complex":
        data["capital_gain"] = random.randint(-2000, 8000)      # 1099-B
        data["rental"] = random.randint(2000, 15000)            # Schedule E
        data["k1_income"] = random.randint(1000, 5000)          # K-1
        data["foreign_income"] = random.randint(0, 10000)
        data["mortgage_interest"] = random.randint(1000, 5000)  # 1098

    return data