# Dataset Mapping

Project:
Germany National Energy Analytics Platform

Resolution:
Hourly

Period:
2015–2020

Objectives:

1. Electricity demand forecasting
2. Solar generation prediction
3. Carbon impact reporting

---

## Master Schema Mapping

| Master Column | Dataset Source | Raw Column |
|---------------|---------------|------------|
| datetime | | |
| load_MW | | |
| solar_generation_MW | | |
| wind_generation_MW | | |
| temperature_C | | |
| humidity_pct | | |
| cloud_cover_pct | | |
| wind_speed_ms | | |
| precipitation_mm | | |
| carbon_intensity_gCO2kWh | | |
| electricity_price_EURMWh | | |

| Master Column | Dataset Source | Raw Column |
|---------------|---------------|------------|
| datetime | OPSD | utc_timestamp |
| load_MW | OPSD | DE_load_actual_entsoe_transparency |
| solar_generation_MW | OPSD | DE_solar_generation_actual |
| wind_generation_MW | OPSD | DE_wind_generation_actual |
| temperature_C | OpenMeteo | |
| humidity_pct | OpenMeteo | |
| cloud_cover_pct | OpenMeteo | |
| wind_speed_ms | OpenMeteo | |
| precipitation_mm | OpenMeteo | |
| carbon_intensity_gCO2kWh | Carbon dataset | |
| electricity_price_EURMWh | OPSD | DE_LU_price_day_ahead |

| solar_capacity_MW | OPSD | DE_solar_capacity |
| wind_capacity_MW | OPSD | DE_wind_capacity |
| wind_offshore_generation_MW | OPSD | DE_wind_offshore_generation_actual |
| wind_onshore_generation_MW | OPSD | DE_wind_onshore_generation_actual |