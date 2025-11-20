# NAV Data Extraction – Shell Script

This repository contains a shell script that downloads and extracts **Scheme Name** and **Net Asset Value (NAV)** from AMFI India's official NAV dataset:

🔗 Source: `https://portal.amfiindia.com/spages/NAVAll.txt`

The script automatically detects whether the data uses `|` or `;` as the delimiter, making it robust even if AMFI changes the format.

---

## 📌 What the Script Does

The script performs the following steps:

1. Downloads the NAV file using `curl`
2. Detects the delimiter (`|` or `;`)
3. Removes comment and empty lines
4. Extracts:
   - **Column 4 → Scheme Name**
   - **Column 5 → Asset Value (NAV)**
5. Saves the cleaned output into a **TSV file** named `nav_data.tsv`

---

## 🛠️ Requirements

Compatible with:

- Linux
- macOS
- Windows Subsystem for Linux (WSL)

Required tools (commonly pre-installed):

- `curl`
- `awk`
- `sed`
- `grep`

---

## ▶️ How to Run the Script

Make the script executable:

```bash
chmod +x extract_nav.sh
