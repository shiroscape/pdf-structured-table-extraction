## PDF Structured Table Extractor

This is a Python library that extracts and processes structured tables from PDF files using pdfplumber. It provides functionality for cleaning, merging, and extracting specific columns from table data. 

I have searched and used this extensively during my internship, dealing with medical purchase orders as a use case to automate and extract data. As most purchase orders PDFs are different in format and tables, this library aids as a template to extract basic data from pdf tables. From there, fine tuning can be done if necessary for extraction of data. The sample PDF is provided to help in the process. 

## Features

- Extract tables from PDFs.
- Clean and merge broken tables across PDF pages. (this is a check and may or may not work depending on the format of the PDF)
- Extract specific columns like reference codes, quantities, and unit prices.


## Limitations

- It cannot extract data from scanned copies of PDF.
- It cannot extract data if PDF's are protected and encrpyted.
- It cannot extract data from borderless and unstructured tables in PDF.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/shiroscape/pdf-table-extractor.git
cd pdf-table-extractor
pip install -r requirements.txt