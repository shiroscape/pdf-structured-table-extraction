
from table_pdf_extraction import PDFTableExtractor

# Specify the path to your PDF file
file_path = 'pdf_data/test_pdf_file.pdf'

# Instantiate the class with the file path
pdf_extractor = PDFTableExtractor(file_path)  

# Extract the cleaned tables
final_table = pdf_extractor.extract_tables()

# Print the final cleaned table
for row in final_table:
    print(row)

# Extract specific columns (like ref code, quantity, and unit cost)
columns = pdf_extractor.extract_columns()

# Print the extracted columns
print('Ref Code List:', columns['ref_code_list'])
print('Qty List:', columns['qty_list'])
print('Unit Cost List:', columns['unit_cost'])