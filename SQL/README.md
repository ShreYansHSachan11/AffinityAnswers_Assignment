# Rfam SQL Assignment – Solutions

This repository contains SQL queries written for the Rfam public MySQL database, based on the provided schema and the assignment requirements.

## 📌 Database Connection (Public Rfam MySQL)

Use the following credentials to connect:

```
Host: mysql-rfam-public.ebi.ac.uk  
Port: 4497  
User: rfamro  
Password: (none)  
Database: Rfam
```

CLI connection example:

```bash
mysql --user=rfamro --host=mysql-rfam-public.ebi.ac.uk --port=4497 --database=Rfam
```

---

## 📁 Repository Contents

### `/sql/answers.sql`
Contains complete SQL answers for:
1. Tiger species count + Sumatran tiger `ncbi_id`
2. Joinable columns across the Rfam schema
3. Longest DNA sequence among all rice species
4. Paginated query for families with DNA sequence length > 1,000,000

### `/sql/schema_notes.md`
A short explanation of how each table is related and which columns connect them.

---

## 🧠 Notes

- Queries follow best practices: readable, modular, no hard-coding (beyond biological names required).
- Compatible with MySQL 5.7+ and the public Rfam server.
- All results can be tested directly on the remote database.

---

## 📜 Author

Prepared as part of an SQL/database aptitude test.
