import streamlit as st
from multipage import MultiPage
from pages import stream, stream_1

app = MultiPage()

st.title("Data Visualization Application")
app.add_page("Income Poverty in Texas", stream_1.app)
app.add_page("COVID Data Texas", stream.app)

app.run()