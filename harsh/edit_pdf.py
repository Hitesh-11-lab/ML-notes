import fitz  # PyMuPDF

old_roll = "160723748062"
new_roll = "160723748114"

doc = fitz.open("input.pdf")

for page in doc:
    areas = page.search_for(old_roll)

    for rect in areas:
        # 🔹 remove old roll number
        page.add_redact_annot(rect, fill=(1, 1, 1))
    
    page.apply_redactions()

    for rect in areas:
        # 🔹 insert new roll number (aligned properly)
        page.insert_text(
            (rect.x0, rect.y1 - 1.5),  # fine-tuned alignment
            new_roll,
            fontsize=rect.height * 0.85,
            color=(0, 0, 0)
        )

doc.save("output.pdf")

print("✅ Done! Check output.pdf")