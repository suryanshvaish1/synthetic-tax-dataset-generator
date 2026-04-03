from faker import Faker
import random

fake = Faker()

STATES = ["CA", "TX", "NY", "IL", "FL"]
LEVELS = ["easy", "medium", "complex"]

def generate_profile():
    return {
        "name": fake.name(),
        "ssn": fake.ssn(),
        "address": fake.address(),
        "state": random.choice(STATES),
        "filing_status": random.choice(["Single", "Married"]),
        "dependents": random.randint(0, 2),
        "level": random.choice(LEVELS)
    }