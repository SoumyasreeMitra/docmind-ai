from utils.pdf_loader import load_pdf

docs = load_pdf("data/Activation Functions.pdf")

print("Total pages:", len(docs))

print("\nFirst page content:\n")
print(docs[0].page_content[:1000])