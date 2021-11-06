import streamlit as st
from multipage import MultiPage
from pages import (texas_covid, income_poverty, needs_met,
                   prison_data, return_to_homelessness, 
                   homelessness_forecast,HIC_FINAL_REPORT, homepage)
from pages.CPI_homeless.main import predict
app = MultiPage()

st.sidebar.image("logo.png", use_column_width=True)
st.title("Combating Homelessness in Texas")
app.add_page("Home", homepage.app)
app.add_page("Income Poverty in Texas", income_poverty.app)
app.add_page("COVID Data in Texas", texas_covid.app)
app.add_page("Needs Met By Outreach Teams", needs_met.app)
app.add_page("Prison Data in Texas", prison_data.app)
app.add_page("Return to Homelessness Rates", return_to_homelessness.app)
app.add_page("Texas Homelessness forecasts", homelessness_forecast.app)
app.add_page("HIC_FINAL_REPORT", HIC_FINAL_REPORT.app)
app.add_page("County based Child abuse likelihood prediction", predict)
app.run()
