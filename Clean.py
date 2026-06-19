from pypdf import PdfReader
import os
import re


# FOLDERS

pdf_folder = "data"
output_folder = "cleaned_data"

os.makedirs(output_folder, exist_ok=True)


# PROCESS EACH PDF

for pdf_file in os.listdir(pdf_folder):

    if pdf_file.endswith(".pdf"):

        pdf_path = os.path.join(pdf_folder, pdf_file)

        try:
            reader = PdfReader(pdf_path)
            text = ""

            
            # EXTRACT TEXT (ROBUST)
            
            for page in reader.pages:
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                except Exception:
                    # skip broken page
                    continue

            
            # CLEAN TEXT
            
            cleaned_text = re.sub(r'\s+', ' ', text).strip()

            # If PDF had no text
            if not cleaned_text:
                cleaned_text = "NO EXTRACTABLE TEXT FOUND"

            
            # SAVE OUTPUT
            
            output_path = os.path.join(
                output_folder,
                pdf_file.replace(".pdf", ".txt")
            )

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(cleaned_text)

            print(f"Processed: {pdf_file}")

        except Exception as e:
            print(f"Failed to process {pdf_file}: {e}")

print("Data Ingestion and Cleaning Completed")