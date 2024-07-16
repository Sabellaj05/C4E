import fitz
import pandas as pd
import argparse

def pdf_to_excel(input_pdf, output_excel):
    doc = fitz.open(input_pdf)
    data = []
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        data.append(text)

    with pd.ExcelWriter(output_excel) as writer:
        for i, page_text in enumerate(data):
            df = pd.DataFrame(page_text.splitlines(), columns=[f'Page {i+1}'])
            df.to_excel(writer, sheet_name=f'Sheet{i+1}', index=False)

def main(args) -> None:
    pdf_to_excel(args.in_path, args.out_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("in_path", help="Input PDF")
    parser.add_argument("out_path", help="Output Excel")
    args = parser.parse_args()
    main(args)