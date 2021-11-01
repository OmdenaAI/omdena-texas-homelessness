import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os

# Define app for streamlit to grab onto
def app():
    
    # Create styling for page
    st.title("Return to Homelessness Rates in Texas")
    st.markdown(" The dashboard will help anyone to get to know \
        more about the given datasets and it's output")
    st.sidebar.title("Select Visual Charts")
    st.sidebar.markdown("Select a Chart/Plot from the list:")
    
    # Dropdown Menus, saved to referenced variables
    chart_visual = st.sidebar.selectbox("Select Charts/Plot Type",
                                        ("Bar Chart", "Scatter Plot", "Violin Graph"))
    
    selected_status = st.sidebar.selectbox("Select a Category",
                                           options= ['demographic_category',
                                           'specific_demographic', 'so_es_th_sh_ph'])
    # Read in data to dataframe
    # Save to data
    filepath = os.path.join(Path(__file__).parents[1],
                            'data/return_to_homelessness.csv')
    data = pd.read_csv(filepath)
    if chart_visual == "Bar Chart":
        fig = px.bar(data, x=selected_status,y='rate',
                     hover_name='specific_demographic',
                     hover_data= ['demographic_category','specific_demographic'],
                     color_continuous_scale='greens', height=800, width=800)
        st.plotly_chart(fig)
    if chart_visual == "Scatter Plot":
        fig = px.scatter(data, x= selected_status, y='rate',
                         color='fiscal_year',hover_name='specific_demographic',
                         hover_data=['fiscal_year_end','demographic_category'],
                         width=800, height=1200, color_continuous_scale='greens')
        st.plotly_chart(fig)
    if chart_visual == "Violin Graph":
        fig = fig=px.violin(data, y='rate', color='fiscal_year', 
                            points='all', hover_name='demographic_category',
                            hover_data=['specific_demographic'])
        st.plotly_chart(fig)