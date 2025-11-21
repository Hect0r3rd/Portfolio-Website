from PyPDF2 import PdfReader

reader = PdfReader("resume.pdf")
all_text = []
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        all_text.append(text)

out = "\n\n---PAGE_BREAK---\n\n".join(all_text)
with open("resume_text.txt", "w", encoding="utf-8") as f:
    f.write(out)
print("Wrote resume_text.txt")
