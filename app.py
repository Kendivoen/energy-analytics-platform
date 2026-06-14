import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Energy Analytics Platform",
    page_icon="⚡",
    layout="wide"
)

# Load dashboard summary metrics
summary = pd.read_csv(
    "data/dashboard/dashboard_summary_metrics.csv"
)

# Title
st.title("⚡ Energy Analytics Platform")

st.markdown("""
An end-to-end energy analytics project combining:

- Electricity Demand Forecasting
- Solar Generation Forecasting
- Wind Generation Forecasting
- Carbon Impact Assessment

using machine learning and sustainability analytics.
""")

# KPI Cards

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Demand Forecasting R²",
    "0.9953"
)

col2.metric(
    "Solar Forecasting R²",
    "0.9804"
)

col3.metric(
    "Wind Forecasting R²",
    "0.9902"
)

col4.metric(
    "CO₂ Avoided",
    "385.7M tonnes"
)

st.divider()

st.subheader("Project Workflow")

st.markdown("""
Data Collection → Data Cleaning → Exploratory Data Analysis →
Feature Engineering → Demand Forecasting →
Solar Forecasting → Wind Forecasting →
Carbon Impact Analysis → Model Evaluation → Dashboard Development
""")

st.divider()

st.subheader("Dashboard Navigation")

st.markdown("""
Use the sidebar to explore:

- **Forecasting**: Model performance and forecasting results
- **Carbon Impact**: Renewable energy sustainability metrics
- **Project Insights**: Key findings and lessons learned
""")