import streamlit as st
from multipage import MultiPage
from pages import stream, stream_1, mets_reach_by_outreaach, prison_data, Return_to_homelessness

app = MultiPage()

st.title("Data Visualization Application")
app.add_page("Income Poverty in Texas", stream_1.app)
app.add_page("COVID Data in Texas", stream.app)
app.add_page("Needs Met By Outreach Teams", mets_reach_by_outreaach.app)
app.add_page("Prison Data in Texas", prison_data.app)
app.add_page("Return to Homelessness Rates", Return_to_homelessness.app)

app.run()