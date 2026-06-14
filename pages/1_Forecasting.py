import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Forecasting Results",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Forecasting Model Performance")

st.markdown("""
This page compares the forecasting performance of models developed for:

- Electricity demand
- Solar generation
- Wind generation
""")

# Load data
demand_results = pd.read_csv("data/dashboard/demand_model_comparison.csv")
solar_results = pd.read_csv("data/dashboard/solar_model_comparison.csv")
wind_results = pd.read_csv("data/dashboard/wind_model_comparison.csv")

# Helper function
def show_results(title, results_df, selected_model):
    st.subheader(title)

    st.dataframe(
        results_df.style.format({
            "MAE": "{:.2f}",
            "RMSE": "{:.2f}",
            "R2": "{:.4f}"
        }),
        use_container_width=True
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(results_df["Model"], results_df["MAE"])
    ax.set_title(f"{title} - MAE Comparison")
    ax.set_ylabel("MAE")
    ax.tick_params(axis="x", rotation=25)

    st.pyplot(fig)

    st.success(f"Selected Model: {selected_model}")

# Tabs
tab1, tab2, tab3 = st.tabs([
    "Demand Forecasting",
    "Solar Forecasting",
    "Wind Forecasting"
])

with tab1:
    show_results(
        "Demand Forecasting",
        demand_results,
        "Reduced XGBoost"
    )

with tab2:
    show_results(
        "Solar Generation Forecasting",
        solar_results,
        "Enhanced XGBoost"
    )

with tab3:
    show_results(
        "Wind Generation Forecasting",
        wind_results,
        "Enhanced XGBoost"
    )