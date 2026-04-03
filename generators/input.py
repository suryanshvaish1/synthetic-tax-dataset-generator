import json

def save_input(path, profile, income):
    data = {
        "profile": profile,
        "income": income
    }

    with open(path, "w") as f:
        json.dump(data, f, indent=4)