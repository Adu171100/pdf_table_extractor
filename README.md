
# PDF SKU Extractor

This project extracts SKU information from PDFs with product price lists and outputs structured JqaSON.

## Features
- Extracts tabular data from PDFs.
- Parses SKUs with fields: `ID`, `description`, `price`, and `attributes`.

## Prerequisites
- Python 3.6 
- Libraries:
  - `pdfplumber`
  - `json`




##Alternate Approach:
- Use pdf2image library to converts PDF pages to images.
- Use pytesseract to performs OCR (Optical Character Recognition) on images to extract text.
- Use OpenAI's LLM  to analyze text and extract structured data in JSON format. (Don't have the access to OpenAI's paid version)
- Alternatively used Hugging Face's GPT-like pipeline but the accuracy was very low.
