import os

from generators.profile import generate_profile
from generators.income import generate_income
from generators.input import save_input

from pdf_engine.w2 import create_w2
from pdf_engine.form1099_int import create_1099_int
from pdf_engine.form1099_div import create_1099_div
from pdf_engine.schedule_b import create_schedule_b
from pdf_engine.form1040 import create_1040
from pdf_engine.state import create_state
from pdf_engine.summary import create_summary


def generate_dataset(i):
    profile = generate_profile()
    income = generate_income()

    base = f"output/dataset_{i:03}"

    os.makedirs(base + "/documents", exist_ok=True)
    os.makedirs(base + "/federal", exist_ok=True)
    os.makedirs(base + "/state", exist_ok=True)

    save_input(f"{base}/input.json", profile, income)

    create_w2(f"{base}/documents/w2.pdf", profile, income)
    create_1099_int(f"{base}/documents/1099_int.pdf",profile, income)
    create_1099_div(f"{base}/documents/1099_div.pdf", income)

    create_1040(f"{base}/federal/form_1040.pdf", profile, income)
    create_schedule_b(f"{base}/federal/schedule_b.pdf", income)

    create_state(f"{base}/state/state_return.pdf", income)

    create_summary(f"{base}/summary.pdf", profile, income)


def run():
    for i in range(1, 41):
        print(f"Generating {i}")
        generate_dataset(i)

    print("✅ 40 datasets ready")


if __name__ == "__main__":
    run()