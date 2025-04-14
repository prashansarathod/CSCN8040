# CSCN8040

All the required libraries are provided inside jupyter notebook

Link to datasets:

1. [EPA dataset](https://www.epa.gov/outdoor-air-quality-data/download-daily-data)
2. [For data wrangling](https://www.eia.gov/consumption/residential/data/2020/#fueluses)
3. [Low-income Energy Affordability Data Tool](https://lead.openei.org/)

# 🧪 Clean Heating Subsidy Allocation – PM₂.₅ Analysis & AI Modeling

This project uses AI and statistical techniques to identify high-priority regions for clean heating subsidies based on PM₂.₅ levels, wood fuel usage, and income brackets. The work is structured into three main notebooks and an optional Streamlit dashboard.

## 📁 Repository Structure

- `datawrang.ipynb` – Data wrangling and feature engineering
- `unit4.ipynb` – Statistical validation and hypothesis testing
- `unit5.ipynb` – Model building and visualization
- `ui.py` – Streamlit dashboard (optional)
- `requirements.txt` – Python package dependencies
---
Make sure you have **Python 3.9+** installed.


# 1. Clone the repository
```bash
git clone https://github.com/prashansarathod/CSCN8040.git
cd CSCN8040
```
# 2. (Optional) Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate        # Windows
```
# 3. Install dependencies
```bash
pip install -r requirements.txt
```


---
# 🔄 Execution Order & Notebook Purpose

This project includes four core files: three Jupyter notebooks and one Streamlit dashboard. Below is the required execution order and purpose of each component.

---

## 1️⃣ merged_data.ipynb – Data Preparation & Feature Engineering
- **Purpose:** Creates the full modeling dataset
- **Loads:**
  - `pm25_combined.csv`: Aggregated PM2.5 values (e.g., from AL/CA)
- **Simulates:**
  - `Wood_Usage_%` per county
  - `Avg_Income_Bracket` per county
- **Engineers:**
  - `Subsidy_Priority_Score` using PM2.5, income, wood usage
- **Saves:**
  - `./data/merged_subsidy_priority_data.csv`
- ✅ **Optional** since already created by the ipynb and uploaded "merged_subsidy_priority_data.csv"  inside `data/`

---

## 2️⃣ unit5.ipynb – Model Training & Evaluation
- **Purpose:** Builds and evaluates the Random Forest model
- **Loads:**
  - `./data/merged_subsidy_priority_data.csv`
- **Performs:**
  - Random Forest Regression
  - Calculates R², MAE, MSE
  - Feature importance chart
  - Confidence estimation using std. dev. across trees
- ✅ **Run after Step 1**

---

## 3️⃣ ui.py – Streamlit Dashboard
- **Purpose:** User interface for live predictions and policy suggestions
- **Runs a retrained Random Forest** based on user input
- **No pre-saved model needed** – training happens instantly from CSV
- **To run:**
```bash
streamlit run ui.py
```

- Select your county and input values
- Get real-time subsidy score predictions
- Includes model confidence and policy advice
---






