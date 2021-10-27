import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Spread of COVID-19 in Texas by County")
st.markdown("The dashboard will help anyone to get to know \
    more about the given datasets and it's output")
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select a Chart/Plot from the list:")

data = pd.read_csv('COVID_case_count_data.csv')

chart_visual = st.sidebar.selectbox("Select Charts/Plot type", 
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))

st.sidebar.checkbox("Show Analysis by Cases", True, key = 1)
selected_status = st.sidebar.selectbox('Select Case Type',
                                       options = ['confirmed_cases', 'probable_cases', 'fatalities'])

fig = go.Figure()

if chart_visual == 'Line Chart':
    if selected_status == 'confirmed_cases':
        fig.add_trace(go.Scatter(x = data.county, 
                                 y = data.confirmed_cases, 
                                 name = 'confirmed_cases', 
                                 mode = 'lines'))
    if selected_status == 'probable_cases':
        fig.add_trace(go.Scatter(x = data.county, 
                                 y = data.probable_cases, 
                                 name = 'probable_cases', 
                                 mode = 'lines'))
    if selected_status == 'fatalities':
        fig.add_trace(go.Scatter(x = data.county, 
                                 y = data.fatalities, 
                                 name = 'fatalities', 
                                 mode = 'lines'))

elif chart_visual == 'Bar Chart':
    if selected_status == 'confirmed_cases':
        fig.add_trace(go.Bar(x = data.county,
                             y = data.confirmed_cases, 
                             name = 'confirmed_cases'))
        
    if selected_status == 'probable_cases':
        fig.add_trace(go.Bar(x = data.county,
                             y = data.probable_cases, 
                             name = 'probable_cases'))
    
    if selected_status == 'fatalities':
        fig.add_trace(go.Bar(x = data.county,
                             y = data.fatalities, 
                             name = 'fatalities'))
elif chart_visual == 'Bubble Chart':
    if selected_status == 'confirmed_cases':
        fig.add_trace(go.Scatter(x = data.county,
                                 y = data.confirmed_cases,
                                 mode = 'markers',
                                 name = 'confirmed_cases'))
        
    if selected_status == 'probable_cases':
        fig.add_trace(go.Scatter(x = data.county,
                                 y = data.probable_cases,
                                 mode = 'markers',
                                 name = 'probable_cases'))
        
    if selected_status == 'fatalities':
        fig.add_trace(go.Scatter(x = data.county,
                                  y = data.fatalities,
                                  mode = 'markers',
                                  name = 'fatalities'))

st.plotly_chart(fig, use_container_width=True)