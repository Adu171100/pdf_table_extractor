#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:23:48 2025

@author: Adnan
"""

import pdfplumber
import json

def extract_tables_from_pdf(pdf_path): 
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_tables = page.extract_tables()
            if page_tables:
                tables.extend(page_tables)
    return tables


def parse_table_to_json(tables):
    sku_list = []
    for table in tables:
        for row in table:
            #print(f"Row: {row}")
            try:
                # Ensure the row has 4 fields
                if len(row) < 4:
                    #print(f"Skip incomplete rows: {row}")
                    continue
                
                # Extract columns 
                idh_no = row[0] if row[0] else None
                description = row[1] if len(row) > 1 else ""
                pack_size = row[2] if len(row) > 2 else ""
                price = row[3] if len(row) > 3 else ""

                # Skip rows with missing ID, price or description
                if not idh_no or idh_no.strip() == "" or not price or price.strip() == "" or not description or description.strip() == "":
                    #print("Skip rows with missing ID, price or description")
                    continue
                
                #Add sku info to a list         
                sku_list.append({
                    "ID": int(idh_no.strip()),
                    "title": "",
                    "description": description.strip(),
                    "price": float(price.strip().replace(",", "")) if price and price.strip().replace(",", "").isnumeric() else None,
                    "attributes": {"Pack Size": pack_size.strip()},
                })
                
            except Exception as e:
                #print(f"Error parsing row: {row}, Error: {e}")
                continue 
            
    return sku_list



if __name__ == "__main__":
    # PDF path
    pdf_path = 'LOCTITE-Price-List_Effective-01.07.2022_Gokul-Traders (1).pdf'

    # Extract tables from the PDF
    tables = extract_tables_from_pdf(pdf_path)
    #print(f"Extracted tables: {tables}")  

    # Parse tables into JSON
    sku_data = parse_table_to_json(tables)

    # Print the final SKU Info
    print("SKU Info:")
    print(json.dumps(sku_data, indent=4))
