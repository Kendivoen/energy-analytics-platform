import streamlit as st

st.set_page_config(
    page_title="Project Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Project Insights")

st.markdown("""
This page summarizes the main analytical lessons from the Energy Analytics Platform project.
""")

st.divider()

st.header("1. Feature Engineering Was Critical")

st.markdown("""
Across the forecasting workflows, feature engineering produced larger improvements than hyperparameter tuning.

- Demand forecasting improved after feature selection.
- Solar forecasting improved after adding richer temporal and weather-based features.
- Wind forecasting improved dramatically after introducing wind-specific lag features.
""")

st.header("2. Solar and Wind Behave Differently")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Solar Forecasting")
    st.markdown("""
    Solar generation was mainly driven by:
    
    - Hour of day
    - Seasonal patterns
    - Temperature
    - Humidity
    - Cloud cover
    """)

with col2:
    st.subheader("Wind Forecasting")
    st.markdown("""
    Wind generation was mainly driven by:
    
    - Previous-hour wind generation
    - Wind rolling averages
    - Wind speed
    - Seasonal patterns
    """)

st.header("3. Wind Delivered the Majority of Carbon Benefits")

st.markdown("""
Wind generation accounted for approximately **71.7%** of total avoided CO₂ emissions, while solar generation contributed approximately **28.3%**.

This highlights the major role of wind power in Germany's renewable electricity system.
""")

st.header("4. Solar and Wind Are Seasonally Complementary")

st.markdown("""
Solar generation contributes most strongly during spring and summer, while wind generation contributes more strongly during autumn and winter.

This complementarity supports year-round renewable electricity generation and strengthens the case for a diversified renewable energy portfolio.
""")

st.header("5. Project Outcome")

st.success("""
The project demonstrates a complete energy analytics workflow combining data engineering, machine learning, renewable generation forecasting, and carbon impact assessment.
""")