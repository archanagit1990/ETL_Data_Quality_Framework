# ETL Data Engineering & Data Quality Automation Framework

A basic end-to-end ETL and Data Quality automation project built using **Python, Pandas, PostgreSQL and Pytest**.

The project demonstrates how raw data is extracted, transformed, validated, loaded into a target database, and then automatically tested for data quality and reconciliation.

## 🔄 Project Flow

```text
CSV Source
    ↓
Extract
    ↓
Transform & Validate
    ↓
Valid / Rejected Records
    ↓
PostgreSQL
    ↓
Pytest Data Quality Tests
    ↓
HTML Test Report
    ↓
GitHub Actions CI/CD
🏗️ Project Structure
ETL_Data_Quality_Framework/
│
├── data/
│   └── raw/
│       └── sales_data.csv
│
├── src/
│   ├── database.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── run_pipeline.py
│
├── tests/
│   ├── conftest.py
│   ├── test_source_quality.py
│   ├── test_transformations.py
│   ├── test_target_quality.py
│   └── test_reconciliation.py
│
├── reports/
├── .github/workflows/
│   └── etl-quality.yml
├── pytest.ini
├── requirements.txt
└── README.md
🧪 Data Quality Validations

The Pytest framework validates:

Source data availability and schema
Mandatory fields and null checks
Duplicate records
Business rules such as valid quantity
Transformation calculations
Target data quality
Source-to-target reconciliation
Reconciliation Rule
Source Records = Valid Target Records + Rejected Records

Invalid records are retained separately with a rejection_reason for basic traceability.

⚙️ Tech Stack

Python | Pandas | SQL | PostgreSQL | Pytest | Git | GitHub Actions

▶️ Run Locally

Activate the virtual environment:

.venv\Scripts\activate

Run the ETL pipeline:

python src/run_pipeline.py

Run the complete test suite:

pytest

Generate the HTML test report:

pytest --html=reports/etl_test_report.html --self-contained-html
🚀 CI/CD

GitHub Actions automatically:

Sets up Python and PostgreSQL
Runs the ETL pipeline
Executes the Pytest Data Quality suite
Generates the HTML test report
Uploads the report as an artifact
🎯 Key Learning

This project demonstrates the integration of Data Engineering and Data Quality Engineering by combining ETL processing with automated validation and CI/CD.

Extract → Transform → Load → Validate → Report
