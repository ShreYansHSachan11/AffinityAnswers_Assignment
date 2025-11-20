# Technical Assignment – Solutions Overview

This repository contains the solutions for three questions involving Python web scraping, SQL database queries, and a Unix shell script.

---

## Question 1 – OLX Web Scraper (Python)

A Python script that scrapes **“Car Cover”** listings from OLX and prints the **title, description, and price** in a table format.

### How to run:
- Install dependencies:  
  `pip install -r requirements.txt`
- Run the script:  
  `python olx_scraper.py`

---

## Question 2 – SQL Queries (Rfam Database)

This folder contains SQL queries and written answers for:

- Counting tiger species and finding **Sumatran Tiger `ncbi_id`**
- Identifying columns used to connect tables
- Finding which rice species has the **longest DNA sequence**
- Pagination query for families with sequence length above **1,000,000**

All queries work on the **public Rfam MySQL database**.

---

## Question 3 – NAV Extraction Shell Script

A shell script that downloads the **AMFI NAV dataset**, auto-detects the delimiter, and extracts:

- Scheme Name  
- Asset Value

The script outputs a `nav_data.tsv` file.

### Run the script:
  `chmod +x extract_nav.sh
   ./extract_nav.sh `
  