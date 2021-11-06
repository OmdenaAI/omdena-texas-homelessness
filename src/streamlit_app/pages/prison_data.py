# Removed unneccessary imports

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from pathlib import Path
import os

def app():
    filepath = os.path.join(Path(__file__).parents[1],
                            'data/prison_data.csv')
    df = pd.read_csv(filepath)
    st.title("Prison Data")
    st.markdown("Provides visualizations of Prisoner data by gender, from Texas, \
        spanning from 1978 - 2016.")
    st.sidebar.title("Select Visual Charts")
    st.sidebar.markdown("Select a Chart/Plot from the list:")
    chart_visual = st.sidebar.selectbox("Select Charts/Plot type", 
                                        ('Line Chart', 'Bar Chart', 'Bubble Chart', 'HeatMap'))
    st.sidebar.checkbox("Show Analysis by Gender", True, key = 1)
    selected_gender = st.sidebar.selectbox('Select Gender Type',
                                           options = ['male', 'female', 'total'])                 
    fig = go.Figure()
    gender = ['male' , 'female' , 'total']
    if chart_visual == "HeatMap":
        if selected_gender in gender:
            st.markdown("## Heatmap")
            fig,ax = plt.subplots()
            sns.heatmap(df.corr(),ax =ax,cmap="Blues")
            st.write(fig)
    if chart_visual == 'Line Chart':
        if selected_gender == 'male':
            fig.add_trace(go.Scatter(x = df.year, y = df.male , name = 'male' , mode = 'lines'))
        if selected_gender == 'female':
            fig.add_trace(go.Scatter(x = df.year , y = df.female , name = 'female' , mode = 'lines'))
        if selected_gender == 'total':
            fig.add_trace(go.Scatter(x = df.year , y = df.female , name = 'total' , mode = 'lines'))
        st.plotly_chart(fig, use_container_width=True)
    elif chart_visual == 'Bar Chart':
        if selected_gender == 'male':
            fig.add_trace(go.Bar(x = df.year , y = df.male , name = 'male'))
        if selected_gender == 'female':
            fig.add_trace(go.Bar(x = df.year , y = df.female , name = 'female'))
        if selected_gender == 'total':
            fig.add_trace(go.Bar(x = df.year , y = df.total , name = 'total'))
        st.plotly_chart(fig, use_container_width=True)
    elif chart_visual == 'Bubble Chart':
        if selected_gender == 'male':
            fig.add_trace(go.Scatter(x = df.year,
                                     y = df.male,
                                     mode = 'markers',
                                     name = 'male'))

        if selected_gender == 'female':
            fig.add_trace(go.Scatter(x = df.year,
                                     y = df.female,
                                     mode = 'markers',
                                     name = 'female'))

        if selected_gender == 'total':
            fig.add_trace(go.Scatter(x = df.year,
                                      y = df.total,
                                      mode = 'markers',
                                      name = 'total'))
        st.plotly_chart(fig, use_container_width=True)