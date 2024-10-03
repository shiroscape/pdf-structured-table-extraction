from setuptools import setup, find_packages

setup(
    name='table_pdf_extraction',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pdfplumber',  
    ],
    description='A library for extracting and cleaning tables from PDFs',
    author='sheryl teo',
)