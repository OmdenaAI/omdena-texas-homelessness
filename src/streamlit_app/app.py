import streamlit as st
from multipage import MultiPage
from pages import (texas_covid, income_poverty, needs_met,
                   prison_data, return_to_homelessness, 
                   homelessness_forecast,HIC_FINAL_REPORT)

app = MultiPage()

st.title("Visualization of Homelessness in Texas")
app.add_page("Income Poverty in Texas", income_poverty.app)
app.add_page("COVID Data in Texas", texas_covid.app)
app.add_page("Needs Met By Outreach Teams", needs_met.app)
app.add_page("Prison Data in Texas", prison_data.app)
app.add_page("Return to Homelessness Rates", return_to_homelessness.app)
app.add_page("Texas Homelessness forecasts", homelessness_forecast.app)
app.add_page("HIC_FINAL_REPORT", HIC_FINAL_REPORT.app)
app.run()