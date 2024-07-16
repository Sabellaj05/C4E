import tabula
import pandas as pd
import argparse

def pdf_to_excel(in_path, out_path) -> None:
    # Read PDF file
    tables = tabula.read_pdf(in_path, pages='all')

    # Write each table to a separate sheet in the Excel file
    with pd.ExcelWriter(out_path) as writer:
        for i, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f'Sheet{i+1}')

def main(args) -> None:
    pdf_to_excel(args.in_path, args.out_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Pdf to EXcel", description="Convert PDF to Excel file")
    parser.add_argument("in_path", help="Input PDF File")
    parser.add_argument("out_path", help="Output Excel File")
    args = parser.parse_args()
    main(args)
