# -*- coding: utf-8 -*-

import streamlit as st

st.cache(suppress_st_warning=True)
def app():
    st.title('Homepage')

    st.subheader('Problem statement')

    st.write('According to recent statistics, there were 580,466 people experiencing homelessness in America in 2020. Most were individuals (70%), and the rest were people living in families with children. They live in every state and territory of the United States, and they reflected the diversity of our country. This is a big societal issue that many city councils and local governments are trying to solve.')
    st.image("pages/pitBars.png", caption="image source: https://endhomelessness.org/homelessness-in-america/homelessness-statistics/state-of-homelessness-2021/", use_column_width=True)
    
    st.write('The project will be made open-source and the results obtained can help create a systematic response for organizations working in this domain, that can address immediate needs, quickly connect people to housing, and provide services to ensure long-term stability.') 
    st.subheader('Here you can browse the sidebar for using various tools such as')
    
    st.write("")
    st.write("")
    
    st.markdown('## 1. Health Domain')
    st.image("pages/covid.jpg", caption="image source: https://www.texasattorneygeneral.gov/", use_column_width=True)
    st.write("In the health domain, we have built a model for predicting which counties are most at risk of having more child abuse cases based on census population and overall under 18 homeless population for that county. Additionally, we also built a visualization for covid cases for each county giving a reference for which county has more cases and fatalities relative to each other.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.markdown('## 2. Income and Employment')
    st.image("pages/outreach.jpg", caption="image source: https://goldentriangledc.com/what-we-do/homeless-outreach/", use_column_width=True)
    st.write("In this domain, we have created visualzations which give an idea of the poverty index in Texas per County and the needs met by social outreach teams for different categories of homelessness over the year 2018 and 2019 in the City of Austin.")
    #st.write('Depening on the tracker terms selected, sentiment graph for live tweets is displayed. Additionally, user can view historical sentiment tweets for the year 2021')
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.markdown('## 3. Housing and Development')
    st.image("pages/housing.jpg", caption="image source: https://www.archdaily.com/963912/we-already-have-viable-models-for-quality-affordable-housing", use_column_width=True)
    st.write('For housing, a forecasting model was built which can be used as a guide on when and where to concentrate efforts to meet the needs of those who cannot afford housing. Visualizations related to returns to homeless and the demograph which constitutes it, housing inventory control database and historical representation in prison can also be found for in the sidebar.')
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    
    st.markdown('## Acknowledgements')
    st.write('Thanks to Omdena and Omdena Texas Chapter for providing the oppurtunity and guidance to successfully complete the project.')