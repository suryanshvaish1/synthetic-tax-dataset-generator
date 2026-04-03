import os
import json
import random

# Generators
from generators.profile import generate_profile
from generators.income import generate_income
from generators.input import save_input

# PDF Engines
from pdf_engine.w2 import create_w2
from pdf_engine.form1099_int import create_1099_int
from pdf_engine.form1099_div import create_1099_div
from pdf_engine.form1099_nec import create_1099_nec
from pdf_engine.form1099_b import create_1099_b
from pdf_engine.form1098 import create_1098
from pdf_engine.k1 import create_k1

from pdf_engine.schedule_b import create_schedule_b
from pdf_engine.schedule_c import create_schedule_c
from pdf_engine.schedule_d import create_schedule_d
from pdf_engine.schedule_e import create_schedule_e
from pdf_engine.form8949 import create_8949

from pdf_engine.form1040 import create_1040
from pdf_engine.state import create_state
from pdf_engine.summary import create_summary


# Years
YEARS = [2020, 2021, 2022, 2023, 2024, 2025]


def generate_dataset(i):
    # -------- PROFILE --------
    profile = generate_profile()
    level = profile["level"]

    # -------- YEAR --------
    year = random.choice(YEARS)

    # -------- INCOME --------
    income = generate_income(level)

    # -------- BASE PATH --------
    base = f"output/dataset_{i:03}"

    # -------- CREATE FOLDERS --------
    os.makedirs(base + "/documents", exist_ok=True)
    os.makedirs(base + "/federal", exist_ok=True)
    os.makedirs(base + "/state", exist_ok=True)

    # -------- METADATA --------
    metadata = {
        "year": year,
        "level": level,
        "state": profile["state"]
    }

    with open(f"{base}/metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

    # -------- INPUT --------
    save_input(f"{base}/input.json", profile, income)

    # ================= DOCUMENTS =================
    create_w2(f"{base}/documents/w2.pdf", profile, income)

    create_1099_int(f"{base}/documents/1099_int.pdf", profile, income)
    create_1099_div(f"{base}/documents/1099_div.pdf", profile, income)

    # Medium + Complex
    if level in ["medium", "complex"]:
        create_1099_nec(f"{base}/documents/1099_nec.pdf", income)

    # Complex only
    if level == "complex":
        create_1099_b(f"{base}/documents/1099_b.pdf", income)
        create_1098(f"{base}/documents/1098.pdf", income)
        create_k1(f"{base}/documents/k1.pdf", income)

    # ================= FEDERAL =================
    create_1040(f"{base}/federal/form_1040.pdf", profile, income)
    create_schedule_b(f"{base}/federal/schedule_b.pdf", income)

    if level in ["medium", "complex"]:
        create_schedule_c(f"{base}/federal/schedule_c.pdf", income)

    if level == "complex":
        create_schedule_d(f"{base}/federal/schedule_d.pdf", income)
        create_schedule_e(f"{base}/federal/schedule_e.pdf", income)
        create_8949(f"{base}/federal/form_8949.pdf", income)

    # ================= STATE =================
    create_state(f"{base}/state/state_return.pdf", income)

    # ================= SUMMARY =================
    create_summary(f"{base}/summary.pdf", profile, income)


def run():
    print("🚀 Generating datasets...\n")

    for i in range(1, 41):
        print(f"Generating dataset {i}...")
        generate_dataset(i)

    print("\n✅ All 40 datasets generated successfully!")


# ENTRY POINT
if __name__ == "__main__":
    run()