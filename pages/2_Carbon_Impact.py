import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Carbon Impact",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Renewable Energy Carbon Impact")

st.markdown("""
This page summarizes the estimated CO₂ emissions avoided through solar and wind electricity generation in Germany.
""")

# Load data
summary = pd.read_csv("data/dashboard/dashboard_summary_metrics.csv")
annual_carbon = pd.read_csv("data/dashboard/annual_carbon_impact.csv")
seasonal_carbon = pd.read_csv("data/dashboard/seasonal_carbon_impact.csv")
monthly_carbon = pd.read_csv("data/dashboard/monthly_carbon_impact.csv")

# KPI cards
total_co2 = summary.loc[
    summary["Metric"] == "Total CO₂ Avoided (tonnes)",
    "Value"
].values[0]

solar_total = annual_carbon["solar_co2_avoided_tonnes"].sum()
wind_total = annual_carbon["wind_co2_avoided_tonnes"].sum()
total_renewable = annual_carbon["total_co2_avoided_tonnes"].sum()

solar_pct = (solar_total / total_renewable) * 100
wind_pct = (wind_total / total_renewable) * 100

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total CO₂ Avoided",
    f"{total_co2 / 1_000_000:.1f}M tonnes"
)

col2.metric(
    "Solar Contribution",
    f"{solar_pct:.1f}%"
)

col3.metric(
    "Wind Contribution",
    f"{wind_pct:.1f}%"
)

st.divider()

# Annual carbon impact
st.subheader("Annual Renewable CO₂ Avoided")

fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    annual_carbon["year"].astype(str),
    annual_carbon["solar_co2_avoided_tonnes"],
    label="Solar"
)

ax.bar(
    annual_carbon["year"].astype(str),
    annual_carbon["wind_co2_avoided_tonnes"],
    bottom=annual_carbon["solar_co2_avoided_tonnes"],
    label="Wind"
)

ax.set_ylabel("CO₂ Avoided (tonnes)")
ax.set_title("Annual CO₂ Avoided by Solar and Wind Generation")
ax.legend()

st.pyplot(fig)

st.caption("Note: 2020 covers January to September only.")

st.divider()

# Seasonal carbon impact
st.subheader("Seasonal Carbon Impact")

fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    seasonal_carbon["season"],
    seasonal_carbon["solar_co2_avoided_tonnes"],
    label="Solar"
)

ax.bar(
    seasonal_carbon["season"],
    seasonal_carbon["wind_co2_avoided_tonnes"],
    bottom=seasonal_carbon["solar_co2_avoided_tonnes"],
    label="Wind"
)

ax.set_ylabel("CO₂ Avoided (tonnes)")
ax.set_title("Seasonal CO₂ Avoided by Solar and Wind Generation")
ax.legend()

st.pyplot(fig)

st.divider()

# Monthly trend
st.subheader("Monthly Renewable CO₂ Avoided")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    monthly_carbon["year_month"],
    monthly_carbon["total_co2_avoided_tonnes"]
)

ax.set_ylabel("CO₂ Avoided (tonnes)")
ax.set_xlabel("Month")
ax.set_title("Monthly Renewable CO₂ Avoided")
ax.tick_params(axis="x", rotation=45)

st.pyplot(fig)