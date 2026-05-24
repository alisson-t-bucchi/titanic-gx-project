# 🚢 Titanic Data Quality Pipeline  
### 📊 Great Expectations + MySQL + Power BI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Great_Expectations-Data_Quality-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql" />
  <img src="https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge&logo=powerbi" />
</p>

---

# 📖 Overview

This project demonstrates a complete **End-to-End Data Quality Pipeline** using:

- 🐍 Python
- ✅ Great Expectations (GX)
- 🛢️ MySQL
- 📊 Power BI

The pipeline validates Titanic dataset records, stores validation results in MySQL, and visualizes data quality metrics in Power BI dashboards.

---

# 🏗️ Pipeline Architecture

```text
📄 train.csv
        ↓
✅ Great Expectations Validation
        ↓
📋 Validation Results
        ↓
🛢️ MySQL Database
        ↓
📊 Power BI Dashboard
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | ETL and validation scripts |
| ✅ Great Expectations | Data quality validation |
| 🐼 Pandas | Data manipulation |
| 🔗 SQLAlchemy | MySQL connection |
| 🛢️ PyMySQL | MySQL driver |
| 🧰 MySQL Workbench | Database management |
| 📊 Power BI | Dashboard and visualization |

---

# 📁 Project Structure

```text
titanic-gx-project/
│
├── 📂 data/
│   └── 📄 train.csv
│
├── 📂 scripts/
│   ├── ⚙️ setup_gx.py
│   ├── 🧪 create_expectations.py
│   ├── ✅ validate_data.py
│   └── 🛢️ load_mysql.py
│
├── 📂 great_expectations/
│
├── 📄 requirements.txt
│
└── 📄 README.md
```

---

# 🚀 Step 1 — Create Virtual Environment

## 🏗️ Create environment

```powershell
python -m venv .venv
```

---

## ⚡ Activate environment

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

# 📦 Step 2 — Install Dependencies

```powershell
pip install -r requirements.txt
```

Or manually:

```powershell
pip install great_expectations pandas sqlalchemy pymysql
```

---

# ✅ Step 3 — Initialize Great Expectations

```powershell
python scripts/setup_gx.py
```

This creates the GX project structure.

---

# 🧪 Step 4 — Create Expectations

Run:

```powershell
python scripts/create_expectations.py
```

This creates the validation suite containing:

- 🚫 Null validations
- 🔢 Numeric range validations
- 🏷️ Allowed categorical values
- 📈 Statistical validations
- 📊 Quantile validations
- 🔍 Unique value validations

---

# 🔎 Step 5 — Validate Dataset

Run:

```powershell
python scripts/validate_data.py
```

Example output:

```text
expect_column_values_to_be_between: False
expect_column_values_to_be_in_set: False
expect_table_row_count_to_be_between: True
```

---

# 🧠 Great Expectations Rules

## 🚫 Non-null validation

```python
gx.expectations.ExpectColumnValuesToNotBeNull(
    column="PassengerId"
)
```

---

## 🔢 Numeric range validation

```python
gx.expectations.ExpectColumnValuesToBeBetween(
    column="Age",
    min_value=0,
    max_value=100
)
```

---

## 🏷️ Allowed categorical values

```python
gx.expectations.ExpectColumnValuesToBeInSet(
    column="Sex",
    value_set=["male", "female"]
)
```

---

## 📈 Mean validation

```python
gx.expectations.ExpectColumnMeanToBeBetween(
    column="Fare",
    min_value=20,
    max_value=40
)
```

---

## 📉 Median validation

```python
gx.expectations.ExpectColumnMedianToBeBetween(
    column="Fare",
    min_value=10,
    max_value=30
)
```

---

## 📊 Quantile validation

```python
gx.expectations.ExpectColumnQuantileValuesToBeBetween(
    column="Fare",
    quantile_ranges={
        "quantiles": [0.25, 0.5, 0.75],
        "value_ranges": [
            [0, 20],
            [10, 30],
            [20, 50]
        ]
    }
)
```

---

## 🔍 Unique value count validation

```python
gx.expectations.ExpectColumnUniqueValueCountToBeBetween(
    column="Survived",
    min_value=2,
    max_value=2
)
```

---

# 📝 Step 6 — Generate Data Docs

Inside `validate_data.py`:

```python
context.build_data_docs()
context.open_data_docs()
```

The generated report includes:

- ✅ Passed validations
- ❌ Failed validations
- 📊 Dataset statistics
- 🕒 Validation history

If invalid data exists, GX highlights failures in:

- 🔴 Red
- 🟡 Yellow

---

# 🛢️ Step 7 — Create MySQL Database

Open MySQL Workbench and run:

```sql
CREATE DATABASE titanic_quality;
```

---

# 📥 Step 8 — Load Titanic Dataset into MySQL

Run:

```powershell
python scripts/load_mysql.py
```

Example script:

```python
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/train.csv")

engine = create_engine(
    "mysql+pymysql://root:YOUR_PASSWORD@localhost/titanic_quality"
)

df.to_sql(
    "titanic_passengers",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Dataset loaded successfully.")
```

---

# 📋 Step 9 — Store Validation Results in MySQL

Inside `validate_data.py`, validation results are converted into a dataframe and stored in MySQL.

Example:

```python
results = []

for result in validation_result.results:
    results.append({
        "expectation": result.expectation_config.type,
        "success": result.success
    })

df_results = pd.DataFrame(results)

df_results.to_sql(
    "gx_validation_results",
    engine,
    if_exists="replace",
    index=False
)
```

---

# 🗄️ MySQL Tables

## 🚢 titanic_passengers

Stores Titanic dataset records.

---

## ✅ gx_validation_results

Stores validation results from Great Expectations.

---

# 📊 Step 10 — Connect Power BI to MySQL

## 📥 In Power BI

```text
Home → Get Data → MySQL Database
```

---

## ⚙️ Connection Settings

| Field | Value |
|---|---|
| 🖥️ Server | localhost |
| 🔌 Port | 3306 |
| 🛢️ Database | titanic_quality |

---

## 📂 Select Tables

Import:

- 🚢 `titanic_passengers`
- ✅ `gx_validation_results`

---

# 🧮 Power BI DAX Measures

## ✅ Success Count

```DAX
Successes =
COUNTROWS(
    FILTER(
        gx_validation_results,
        gx_validation_results[success] = TRUE()
    )
)
```

---

## ❌ Failure Count

```DAX
Failures =
COUNTROWS(
    FILTER(
        gx_validation_results,
        gx_validation_results[success] = FALSE()
    )
)
```

---

## 📈 Success Rate

```DAX
Success Rate =
DIVIDE(
    [Successes],
    COUNTROWS(gx_validation_results)
)
```

---

# 📊 Suggested Dashboard Visuals

## 🧾 KPI Cards

- Total validations
- Successes
- Failures
- Success rate

---

## 🥧 Pie Chart

Validation status distribution:

- ✅ Passed
- ❌ Failed

---

## 📊 Bar Chart

Validation failures by expectation type.

---

## 📋 Table

Detailed validation results.

---

# 🚨 Example Data Quality Failures

The pipeline detects issues such as:

| Problem | Detected |
|---|---|
| 🚫 Null values | ✅ Yes |
| 🔢 Invalid ages | ✅ Yes |
| 🏷️ Invalid gender values | ✅ Yes |
| 📈 Outliers | ✅ Yes |
| 📊 Statistical anomalies | ✅ Yes |

---

# ❌ Example Invalid Records

```csv
1,0,3,"Braund",male,9999
```

🔴 Invalid age detected.

---

```csv
3,1,3,"Heikkinen",unknown,1000
```

🔴 Invalid gender and age detected.

---

# ▶️ Running the Full Pipeline

## 🧪 1. Create expectations

```powershell
python scripts/create_expectations.py
```

---

## 🔎 2. Validate dataset

```powershell
python scripts/validate_data.py
```

---

## 🛢️ 3. Load dataset into MySQL

```powershell
python scripts/load_mysql.py
```

---

## 📊 4. Refresh Power BI dashboard

Open Power BI and refresh data.

---

# 🔮 Future Improvements

Possible extensions:

- 🌪️ Apache Airflow orchestration
- 🐳 Docker containers
- 🔄 CI/CD integration
- ⚡ Real-time validation
- ☁️ Azure Data Factory
- ❄️ Snowflake support
- 📬 Email alerts on failures
- 📡 Data observability monitoring

---

# 🔄 Example Pipeline Flow

```text
📄 CSV Dataset
        ↓
✅ Great Expectations
        ↓
📋 Validation Results
        ↓
🛢️ MySQL
        ↓
📊 Power BI Dashboard
```

---

# 👨‍💻 Author

### Alisson Teixeira Bucch

💡 Data Engineering • Data Quality • Analytics Engineering

---

# 📜 License

Apache-2.0