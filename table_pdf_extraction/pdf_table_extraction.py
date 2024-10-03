# table_pdf_extraction/pdf_table_extraction.py

import pdfplumber

class PDFTableExtractor:
    def __init__(self, file_path):  # Fixed constructor
        self.file_path = file_path
        self.tables = []
        self.merged_table = []
        self.final_table = []

    def clean_text(self, text):
        """Helper function to clean text data."""
        return text.strip() if text else ''

    # merge_tables meant for pdf broken table pages
    def merge_tables(self, tables):
        merged_table = []
        previous_row = None

        for table in tables:
            for row in table:
                if not any(row):  # Skip empty rows
                    continue
                
                # Check if the row is a continuation of the previous row
                if previous_row and not any(previous_row):
                    merged_row = previous_row[:]
                    for i, cell in enumerate(row):
                        if cell:  
                            merged_row[i] = cell
                    merged_table.append(merged_row)
                    previous_row = None  # Reset previous_row after merging
                else:
                    if all(cell == '' for cell in row):
                        previous_row = row  # Mark this row for potential merging
                    else:
                        merged_table.append(row)
        self.merged_table = merged_table
        return merged_table

    def identify_and_clean_concatenated_rows(self):
        """Identify rows that are likely concatenated and clean the first cell."""
        cleaned_table = []
        for row in self.merged_table:
            cleaned_table.append(row)
        self.final_table = cleaned_table
        return cleaned_table

    def remove_unwanted_rows(self):
        """If needed, remove unwanted rows, like deleting the first row."""

        '''Sample tables output:
        
        ['No.', 'Vendor Ref', 'Our Ref', 'Description', 'UOM', 'QTY', 'Unit Price', 'Value']
        ['1', '1234567', 'ITEM1', 'TESTING 123456 DESCRIPTION', '6/bx', '2', '100.00', '100.00']
        ['2', '2345678', 'ITEM2', 'TESTING 234567 DESCRIPTION', '10/bx', '1', '200.10', '200.10']
        ['', '', '', '', '', 'Total Excl GST 300.00\nAdd GST @ 9% 27.00\nTotal Invoice 327.00', '', '']
        ['Vendor Ref', '1234567', '2345678', '']
        ['QTY', '2', '1', 'Total Excl GST 300.00\nAdd GST @ 9% 27.00\nTotal Invoice 327.00']
        ['Unit Price', '100.00', '200.10', '']
        ['', '', '', '', '', 'Total Excl GST 300.00\nAdd GST @ 9% 27.00\nTotal Invoice 327.00', '', '']

        rows of interest:

        ['1', '1234567', 'ITEM1', 'TESTING 123456 DESCRIPTION', '6/bx', '2', '100.00', '100.00']
        ['2', '2345678', 'ITEM2', 'TESTING 234567 DESCRIPTION', '10/bx', '1', '200.10', '200.10']
        
        '''

        self.final_table = self.final_table[1:3]
        return self.final_table

    def extract_tables(self):
        """Extract and process tables from the PDF."""
        with pdfplumber.open(self.file_path) as pdf:
            for pageNum, pdfPage in enumerate(pdf.pages, start=1):
                page_tables = pdfPage.extract_tables()
                for pageTableNum, table in enumerate(page_tables):
                    clean_table = [[self.clean_text(cell) for cell in row] for row in table if any(row)]
                    self.tables.append(clean_table)

        # Merge broken tables
        self.merge_tables(self.tables)

        # Identify and clean rows with concatenated data
        self.identify_and_clean_concatenated_rows()

        # Remove unwanted rows
        self.remove_unwanted_rows()

        return self.final_table

    def extract_columns(self):
        """Extract specific columns from the table."""
        ref_code_list = []
        qty_list = []
        unit_cost = []

        for row in self.final_table:
            ref_code_list.append(row[1])
            qty_list.append(row[5])
            unit_cost.append(row[6])

        return {
            'ref_code_list': ref_code_list,
            'qty_list': qty_list,
            'unit_cost': unit_cost
        }