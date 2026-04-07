import os
import json
import random
from reportlab.platypus import SimpleDocTemplate, PageBreak

# Generators
from generators.profile import generate_profile
from generators.income import generate_income, calculate_income
from generators.tax import calculate_tax

# PDF Builders
from pdf_engine.form_1040 import build_form_1040
from pdf_engine.schedule_c import build_schedule_c
from pdf_engine.schedule_se import build_schedule_se
from pdf_engine.documents import generate_w2, generate_1099_int, generate_1099_div
from pdf_engine.state_form import generate_state_form


def main():
    base_output = "output"

    if not os.path.exists(base_output):
        os.makedirs(base_output)

    # States list
    states = ["California", "Texas", "New York", "Illinois", "Florida"]

    for i in range(1, 51):
        dataset_id = f"dataset_{i:03d}"
        print(f"Generating {dataset_id}...")

        # =========================
        # 1. GENERATE DATA
        # =========================
        profile = generate_profile()
        income = generate_income()
        income_data = calculate_income(income)
        tax_data = calculate_tax(income_data)

        final_data = {**profile, **income_data, **tax_data}

        # Random state selection
        state = random.choice(states)

        # =========================
        # 2. CREATE FOLDER STRUCTURE
        # =========================
        dataset_folder = os.path.join(base_output, dataset_id)
        documents_folder = os.path.join(dataset_folder, "documents")
        federal_folder = os.path.join(dataset_folder, "federal")
        state_folder = os.path.join(dataset_folder, "state")

        os.makedirs(documents_folder, exist_ok=True)
        os.makedirs(federal_folder, exist_ok=True)
        os.makedirs(state_folder, exist_ok=True)

        # =========================
        # 3. SAVE INPUT JSON
        # =========================
        with open(os.path.join(dataset_folder, "input.json"), "w") as f:
            json.dump(final_data, f, indent=4)

        # =========================
        # 4. SAVE METADATA
        # =========================
        metadata = {
            "dataset_id": dataset_id,
            "state": state,
            "status": "generated"
        }

        with open(os.path.join(dataset_folder, "metadata.json"), "w") as f:
            json.dump(metadata, f, indent=4)

        # =========================
        # 5. GENERATE DOCUMENTS
        # =========================
        generate_w2(os.path.join(documents_folder, "w2.pdf"), final_data)
        generate_1099_int(os.path.join(documents_folder, "1099_int.pdf"), final_data)
        generate_1099_div(os.path.join(documents_folder, "1099_div.pdf"), final_data)

        # =========================
        # 6. GENERATE FEDERAL FORMS
        # =========================

        # Form 1040
        doc_1040 = SimpleDocTemplate(os.path.join(federal_folder, "form_1040.pdf"))
        doc_1040.build(build_form_1040(final_data))

        # Schedule C
        doc_sc = SimpleDocTemplate(os.path.join(federal_folder, "schedule_c.pdf"))
        doc_sc.build(build_schedule_c())

        # Schedule SE
        doc_se = SimpleDocTemplate(os.path.join(federal_folder, "schedule_se.pdf"))
        doc_se.build(build_schedule_se())

        # =========================
        # 7. GENERATE STATE FORM
        # =========================
        generate_state_form(
            os.path.join(state_folder, "state_return.pdf"),
            final_data,
            state
        )

        # =========================
        # 8. GENERATE SUMMARY PDF
        # =========================
        summary_path = os.path.join(dataset_folder, "summary.pdf")
        doc_summary = SimpleDocTemplate(summary_path)

        content = []
        content += build_form_1040(final_data)
        content.append(PageBreak())
        content += build_schedule_c()
        content.append(PageBreak())
        content += build_schedule_se()

        doc_summary.build(content)

    print("\n✅ ALL 50 DATASETS GENERATED SUCCESSFULLY!")


if __name__ == "__main__":
    main()