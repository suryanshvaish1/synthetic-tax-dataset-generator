import random

def generate_income():
    return {
        "w2": random.randint(30000, 100000),
        "interest": random.randint(0, 2000),
        "dividend": random.randint(0, 1500)
    }