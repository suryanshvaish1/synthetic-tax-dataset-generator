from faker import Faker
fake = Faker()

def generate_profile():
    return {
        "name": fake.name(),
        "ssn": fake.ssn(),
        "address": fake.address()
    }