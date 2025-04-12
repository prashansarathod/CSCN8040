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

### A. `datawrang.ipynb` – Data Wrangling
- Cleans and merges datasets
- Simulates household-level features
- Calculates `Subsidy Priority Score`

### B. `unit4.ipynb` – Statistical Testing
- Validates PM₂.₅ as a pollution proxy
- Performs:
  - Pearson correlation (ρ = 0.9998)
  - Hypothesis testing vs. EPA standards

### C. `unit5.ipynb` – Model Training
- Builds a `RandomForestRegressor`
- Predicts subsidy priority scores
- Outputs model performance and plots

---

## ⚙️ Setup and Installation

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

## 🖥️ Optional: Run the Interactive Dashboard

To launch the Streamlit-based UI:

```bash
streamlit run ui.py
```

- Select your county and input values
- Get real-time subsidy score predictions
- Includes model confidence and policy advice
