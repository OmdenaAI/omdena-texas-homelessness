import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
#from pathlib import Path

def app():
    df = pd.read_csv(r'C:\Users\Alex Lucchesi\OneDrive\Documents\GitHub\omdena-texas-homelessness\src\dashboards\app\data\needs_met_by_outreach_teams.csv')
    st.title("Needs met by Outreach Teams")
    st.markdown("The dashboard will help anyone to get to know \
        more about the given datasets and it's output")
    st.sidebar.title("Select Visual Charts")
    st.sidebar.markdown("Select a Chart/Plot from the list:")
    chart_visual = st.sidebar.selectbox("Select Charts/Plot type", 
                                        ('Line Chart', 'Bar Chart', 'HeatMap'))
    st.sidebar.checkbox("Show Analysis by Met Reach", True, key = 1)               
    fig = go.Figure()
    gender = ['fiscal_year','need_type','number_of_needs_met']
    if chart_visual == "HeatMap":
        st.markdown("## Heatmap")
        fig,ax = plt.subplots()
        sns.heatmap(df.corr(),ax =ax,cmap="Blues")
        st.write(fig)
    if chart_visual == 'Line Chart':
        fig.add_trace(go.Scatter(x = df.need_type, y = df.number_of_needs_met , name = 'number_of_needs_met' , mode = 'lines'))
    elif chart_visual == 'Bar Chart':
        fig.add_trace(go.Bar(x = df.need_type , y = df.number_of_needs_met , name = 'number_of_needs_met'))
    st.plotly_chart(fig, use_container_width=True)