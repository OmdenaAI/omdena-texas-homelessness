import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
import os

def app():

    st.title("Income Poverty Statistics in Texas by County")
    st.markdown(" The dashboard will help anyone to get to know \
        more about the given datasets and it's output")
    st.sidebar.title("Select Visual Charts")
    st.sidebar.markdown("Select a Chart/Plot from the list:")

    filepath = os.path.join(Path(__file__).parents[1], 
                             'data/texas_income_poverty_stats.csv')
    data = pd.read_csv(filepath)

    chart_visual = st.sidebar.selectbox("Select Charts/Plot Type", 
                                        ("Line Chart", "Bar Chart", "Scatter Plot"))

    st.sidebar.checkbox("Show Analysis by Category", True, key=1)
    selected_status = st.sidebar.selectbox("Select a Category",
                                           options = ['Total Personal Income', 'Median Household Income',
                                                      'Average Annual Pay',
                                                      'Percentage of Population in Poverty',
                                                      'Percentage of Population Under 18 in Poverty'])

    fig = go.Figure()

    if chart_visual == "Line Chart":
        if selected_status == "Total Personal Income":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.total_personal_income,
                                     name = 'Total Personal Income by County in Texas',
                                     mode= 'lines'))
        if selected_status == "Median Household Income":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.median_household_income,
                                     name = 'Median Household Income by County in Texas',
                                     mode = 'lines'))
        if selected_status == "Average Annual Pay":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.average_annual_pay,
                                     name = 'Average Annual Income by County in Texas',
                                     mode = 'lines'))
        if selected_status == "Percentage of Population in Poverty":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.percentage_of_population_in_poverty,
                                     name = 'Percentage of the Population Living in Poverty by County in Texas',
                                     mode = 'lines'))
        if selected_status == "Percentage of Population Under 18 in Poverty":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.percentage_of_population_under_18_in_poverty,
                                     name = 'Percentage of Population Under 18 Living in Poverty by County in Texas',
                                     mode = 'lines'))

    if chart_visual == "Bar Chart":
        if selected_status == "Total Personal Income":
            fig.add_trace(go.Bar(x = data.county,
                                 y = data.total_personal_income,
                                 name = 'Total Personal Income by County in Texas'))
        if selected_status == "Median Household Income":
            fig.add_trace(go.Bar(x = data.county,
                                 y = data.median_household_income,
                                 name = 'Median Household Income by County in Texas'))
        if selected_status == "Average Annual Pay":
            fig.add_trace(go.Bar(x = data.county,
                                 y = data.average_annual_pay,
                                 name = 'Average Annual Income by County in Texas'))
        if selected_status == "Percentage of Population in Poverty":
            fig.add_trace(go.Bar(x = data.county,
                                 y = data.percentage_of_population_in_poverty,
                                 name = 'Percentage of the Population Living in Poverty by County in Texas'))
        if selected_status == "Percentage of Population Under 18 in Poverty":
            fig.add_trace(go.Bar(x = data.county,
                                 y = data.percentage_of_population_under_18_in_poverty,
                                 name = 'Percentage of Population Under 18 Living in Poverty by County in Texas'))

    if chart_visual == "Scatter Plot":
        if selected_status == "Total Personal Income":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.total_personal_income,
                                     name = 'Total Personal Income by County in Texas',
                                     mode = 'markers'))
        if selected_status == "Median Household Income":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.median_household_income,
                                     name = 'Median Household Income by County in Texas',
                                     mode = 'markers'))
        if selected_status == "Average Annual Pay":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.average_annual_pay,
                                     name = 'Average Annual Income by County in Texas',
                                     mode = 'markers'))
        if selected_status == "Percentage of Population in Poverty":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.percentage_of_population_in_poverty,
                                     name = 'Percentage of the Population Living in Poverty by County in Texas',
                                     mode = 'markers'))
        if selected_status == "Percentage of Population Under 18 in Poverty":
            fig.add_trace(go.Scatter(x = data.county,
                                     y = data.percentage_of_population_under_18_in_poverty,
                                     name = 'Percentage of Population Under 18 Living in Poverty by County in Texas',
                                     mode = 'markers'))

    st.plotly_chart(fig, use_container_width=True)