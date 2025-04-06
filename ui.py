import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# ---- Load real merged dataset ----
df = pd.read_csv("data/merged_subsidy_priority_data.csv")  # Ensure this file is in your working directory

# Train the real model
X = df[['Wood_Usage_%', 'Avg_Income_Bracket', 'Average_PM2.5_2020']]
y = df['Subsidy_Priority_Score']
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X, y)

# ---- Streamlit UI ----
st.set_page_config(page_title="CleanHeat AI - Subsidy Predictor", layout="centered")
st.title("🔍 AI-Powered Subsidy Priority Estimator")
st.write("Enter regional heating and air quality data to estimate subsidy priority.")

# Dropdowns for all inputs
county = st.selectbox("Select County:", df['County'].unique())
state = st.selectbox("Select State:", df[df['County'] == county]['State'].unique())

# Fetch values from the selected county
county_data = df[df['County'] == county].iloc[0]
wood_usage = st.selectbox("% of Homes Using Wood:", options=list(sorted(df['Wood_Usage_%'].unique())), index=list(sorted(df['Wood_Usage_%'].unique())).index(county_data['Wood_Usage_%']))
income_bracket = st.selectbox("Average Income Bracket:", options=list(sorted(df['Avg_Income_Bracket'].unique())), index=list(sorted(df['Avg_Income_Bracket'].unique())).index(county_data['Avg_Income_Bracket']))
pm25 = st.selectbox("Average PM2.5 Level (2020):", options=list(sorted(df['Average_PM2.5_2020'].unique())), index=list(sorted(df['Average_PM2.5_2020'].unique())).index(county_data['Average_PM2.5_2020']))

# Prediction with confidence estimate
X_input = np.array([[wood_usage, income_bracket, pm25]])
all_tree_preds = [tree.predict(X_input)[0] for tree in rf.estimators_]
pred_mean = np.mean(all_tree_preds)
pred_std = np.std(all_tree_preds)

# Confidence category
if pred_std < 50:
    confidence = "High"
elif pred_std < 150:
    confidence = "Moderate"
else:
    confidence = "Low"

# Display results
st.markdown("---")
st.subheader(f"📊 Predicted Subsidy Priority Score: **{pred_mean:.2f}**")
st.text(f"Model Confidence Level: {confidence} (±{pred_std:.2f})")

# Suggest policy action
if pred_mean > 1000:
    st.success("🔺 High Priority: Recommend immediate clean heating subsidy intervention.")
elif pred_mean > 600:
    st.warning("⚠️ Moderate Priority: Consider targeted outreach or pilot subsidy.")
else:
    st.info("✅ Low Priority: Minimal intervention needed at this time.")
