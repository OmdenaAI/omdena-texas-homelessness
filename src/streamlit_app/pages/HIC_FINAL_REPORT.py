import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt
import os

def app():

    st.title("HIC FINAL REPORT")
    st.markdown(" Visualizations of all the Project Type")
    st.sidebar.title("Select Visual Charts")
    st.sidebar.markdown("Select a Chart/Plot from the list:")

    filepath = os.path.join(Path(__file__).parents[1], 
                             'data/HIC_FINAL_REPORT.csv')
    data = pd.read_csv(filepath)
    data['Difference'] = data['Year_2017'] - data['Year_2016']

    chart_visual = st.sidebar.selectbox("Select Charts/Plot Type", 
                                        ("Line Chart", "Bar Chart", "Scatter Plot", "HeatMap"))

    st.sidebar.checkbox("Show Analysis by Category", True, key=1)
    selected_status = st.sidebar.selectbox("Select a Category",
                                           options = ['Year_2016', 'Year_2017',
                                                      'Difference',])

    
    fig = go.Figure()
    if chart_visual == "HeatMap":
        st.markdown("## Heatmap")
        fig,ax = plt.subplots()
        sns.heatmap(data.corr(),ax =ax,cmap="Blues")
        st.write(fig)

    if chart_visual == "Line Chart":
        if selected_status == "Year_2016":
            st.markdown("This graph helps to represent the report pf all the Project Type in the year 2016")
            fig.add_trace(go.Scatter(x = data.Project_Type,
                                     y = data.Year_2016,
                                     name = 'Project Type data in the year 2016',
                                     mode= 'lines'))
        if selected_status == "Year_2017":
            st.markdown("This graph helps to represent the report pf all the Project Type in the year 2016")
            fig.add_trace(go.Scatter(x = data.Project_Type,
                                     y = data.Year_2017,
                                     name = 'Project Type data in the year 2017',
                                     mode= 'lines'))
        if selected_status == "Difference":
            st.markdown("This graph helps to represent the report pf all the Project Type in the year 2016")
            fig.add_trace(go.Scatter(x = data.Project_Type,
                                     y = data.Difference,
                                     name = 'Project Type data as per difference',
                                     mode= 'lines'))


    if chart_visual == "Bar Chart":
        if selected_status == "Year_2016":
            st.markdown("This graph helps to represent the report pf all the Project Type in the year 2016")
            fig = px.bar(data, x = 'Project_Type', y = 'Year_2016',
                         title = 'Project Type data in the year 2016',
                         width = 800, height= 800)

        if selected_status == "Year_2017":
            st.markdown("This graph helps to represent the report pf all the Project Type in the year 2016")
            fig = px.bar(data, x = 'Project_Type', y = 'Year_2017',
                         title = 'Project Type data in the year 2017',
                         width = 800, height= 800)
        if selected_status == "Difference":
            st.markdown("This graph helps to represent the report pf all the Project Type in the year 2016")
            fig = px.bar(data, x = 'Project_Type', y = 'Difference',
                         title = 'Project Type data as per Difference in the Years',
                         width = 800, height= 800)

    if chart_visual == "Scatter Plot":
        if selected_status == "Year_2016":
            st.markdown("This graph helps to represent the report pf all the Project Type in the year 2016")
            fig = px.scatter(data, x = 'Project_Type', y = 'Year_2016',
                         title = 'Project Type data in the year 2016',
                         width = 800, height= 800)

        if selected_status == "Year_2017":
            st.markdown("This graph helps to represent the report pf all the Project Type in the year 2016")
            fig = px.scatter(data, x = 'Project_Type', y = 'Year_2017',
                         title = 'Project Type data in the year 2017',
                         width = 800, height= 800)
        if selected_status == "Difference":
            st.markdown("This graph helps to represent the report pf all the Project Type in the year 2016")
            fig = px.scatter(data, x = 'Project_Type', y = 'Difference',
                         title = 'Project Type data as per Difference in the Years',
                         width = 800, height= 800)

    st.plotly_chart(fig, use_container_width=True)