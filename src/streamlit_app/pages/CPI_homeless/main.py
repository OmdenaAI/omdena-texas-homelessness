# -*- coding: utf-8 -*-


import pickle
import pandas as pd
import numpy as np
import joblib

import streamlit as st

def model(X):
    scaler= joblib.load('pages\CPI_homeless\models\scaler.save')
    mfile = open('pages/CPI_homeless/models/finalized_model.sav', 'rb')     
    rf = pickle.load(mfile)
    X_norm= scaler.transform(X)
    y= rf.predict(X_norm)
    if y==1:
        st.header("Risk level: 1 (Homeless under 18 populations least likely to experience child abuse)")
    elif y==2:
        st.header("Risk level: 2 (Less number of reports of child abuse)")
    elif y==3:
        st.header("Risk level: 3 (Controllable number of reports of child abuse)")
    elif y==4:
        st.header("Risk level: 4 (High number of reports of child abuse)")
    else:
        st.header("Risk level: 5 (Alarming number of reports of child abuse)")
    
    

    
    

def preprocess(df):
    #Counties part of Texas Balance of State
    Bos= "Anderson, Culberson, Hidalgo, Mason, Scurry, Andrews, Dallam, Hockley, Matagorda, Shackelford, Angelina, Dawson, Hood, Maverick, Shelby, Aransas, De Witt, Hopkins, McCulloch, Sherman, Armstrong, Deaf Smith, Houston, McMullen, Smith, Atascosa, Delta, Howard, Medina, Somervell, Austin, Denton, Hudspeth, Menard, Starr, Bailey, Dickens, Hunt, Midland, Sterling, Bandera, Dimmit, Hutchinson, Mills, Stonewall, Bastrop, Donley, Irion, Mitchell, Sutton, Bee, Duval, Jackson, Moore, Swisher, Bell, Eastland, Jasper, Morris, Taylor, Blanco, Ector, Jeff Davis, Motley, Terrell, Borden, Edwards, Jefferson, Nacogdoches, Terry, Bowie, Ellis, Jim Hogg, Navarro, Titus, Brazoria, Erath, Jim Wells, Newton, Tom Green, Brewster, Fannin, Johnson, Nolan, Trinity, Briscoe, Fayette, Jones, Nueces, Tyler, Brooks, Fisher, Karnes, Ochiltree, Upshur, Brown, Floyd, Kaufman, Oldham, Upton, Burnet, Franklin, Kendall, Orange, Uvalde, Caldwell, Frio, Kenedy, Panola, Val Verde, Calhoun, Gaines, Kent, Parmer, Van Zandt, Callahan, Galveston, Kerr, Pecos, Victoria, Cameron, Garza, Kimble, Polk, Walker, Camp, Gillespie, King, Potter, Waller, Carson, Glasscock, Kinney, Presidio, Ward, Cass, Goliad, Kleberg, Rains, Washington, Castro, Gonzales, Knox, Randall, Webb, Chambers, Gray, La Salle, Reagan, Wharton, Cherokee, Grayson, Lamar, Real, Wheeler, Cochran, Gregg, Lamb, Red River, Willacy, Coke, Guadalupe, Lampasas, Reeves, Williamson, Coleman, Hale, Lavaca, Refugio, Wilson, Collingsworth, Hall, Lee, Roberts, Winkler, Colorado, Hamilton, Liberty, Rockwall, Wood, Comal, Hansford, Lipscomb, Runnels, Yoakum, Comanche, Hardin, Live Oak, Rusk, Zapata, Concho, Harrison, Llano, Sabine, Zavala, Cooke, Hartley, Loving, San Augustine, Coryell, Haskell, Lubbock, San Jacinto, Crane, Hays, Lynn, San Patricio, Crockett, Hemphill, Marion, San Saba, Crosby, Henderson, Martin, Schleicher"
    Bos= Bos.split(',')
    Bos= [c.strip() for c in Bos]
    #Duplicate Counties present in other CoCs
    rem= ['Washington', 'Potter', 'Randall']
    for i in rem:
        Bos.remove(i)
    am= ['Potter', 'Randall'] #amarillo Coc
    tra= ['Travis'] #Travis CoC
    br= ['Leon', 'Brazos', 'Grimes', 'Washington', 'Burleson', 'Madison', 'Robertson', 'Milam'] #Bryan/college COC
    da= ['Collin', 'Dallas'] #Dallas CoC
    el= ['El Paso'] #El Paso CoC
    ta= ['Parker', 'Tarrant'] #Tarrant CoC
    ha= ['Harris', 'Fort Bend', 'Montgomery'] #Harris CoC
    bex= ['Bexar'] #Bexar CoC
    mc= ['McLennan', 'Limestone', 'Bosque', 'Hill', 'Falls', 'Freestone'] #Mclennan Coc
    #Wichita Falls COc
    wi= ['Childress', 'Foard', 'Baylor', 'Clay', 'Montague', 'Hardeman', 'Wilbarger', 'Wise', 'Cottle', 'Throckmorton', 'Young', 'Jack', 'Archer', 'Stephens', 'Palo Pinto', 'Wichita']

    for c,i in enumerate(df.area_name):
        if any(i in s for s in Bos):
            df.at[c, 'coc']= 'Texas Balance of State CoC'
        elif any(i in s for s in wi):
            df.at[c, 'coc']= 'Wichita Falls/Wise, Palo Pinto, Wichita, Archer Counties CoC'
        elif any(i in s for s in am):
            df.at[c, 'coc']= 'Amarillo CoC'
        elif any(i in s for s in br):
            df.at[c, 'coc']= 'Bryan, College Station/Brazos Valley CoC'
        elif any(i in s for s in da):
            df.at[c, 'coc']= 'Dallas City & County, Irving CoC'
        elif any(i in s for s in el):
            df.at[c, 'coc']= 'El Paso City & County CoC'
        elif any(i in s for s in ta):
            df.at[c, 'coc']= 'Fort Worth, Arlington/Tarrant County CoC'
        elif any(i in s for s in ha):
            df.at[c, 'coc']= 'Houston, Pasadena, Conroe/Harris, Ft. Bend, Montgomery, Counties CoC'
        elif any(i in s for s in bex):
            df.at[c, 'coc']= 'San Antonio/Bexar County CoC'
        elif any(i in s for s in mc):
            df.at[c, 'coc']= 'Waco/McLennan County CoC'
        elif any(i in s for s in tra):
            df.at[c, 'coc']= 'Austin/Travis County CoC'
    return df



def custom(data, homeless):
    data=preprocess(data)
    
    for c,i in enumerate(data.area_name):
        data.loc[c,'Number of white males':'Number of other races females']=data.loc[c,'Number of white males':'Number of other races females']/homeless
    data.drop(labels=['area_name'], inplace= True, axis=1)
    file = open('pages/CPI_homeless/models/target.pkl', 'rb')     
    smooth = pickle.load(file)
    data['coc_enc']=data['coc'].map(smooth)
    data.drop(labels=['coc'], inplace= True, axis=1)
    X_test= data.to_numpy()
    model(X_test)
    
    

def historical(county, Year):
    dfh= pd.read_csv('.\pages\CPI_homeless\{}.csv'.format(Year))
    values= dfh.loc[dfh['area_name'] == county ]
    values.reset_index(drop= True, inplace= True)
    inp= preprocess(values)
    inp.drop(labels=['area_name', 'Fiscal Year', 'count'], inplace= True, axis=1)
    file = open('pages/CPI_homeless/models/target.pkl', 'rb')     
    smooth = pickle.load(file)
    inp['coc_enc']=inp['coc'].map(smooth)
    inp.drop(labels=['coc'], inplace= True, axis=1)
    X_test= inp.to_numpy()
    model(X_test)
    
    
    
    



st.cache(suppress_st_warning=True)
def predict():
    state= ['Armstrong', 'Bailey', 'Briscoe', 'Carson', 'Castro', 'Childress', 'Cochran', 'Collingsworth', 'Crosby', 'Dallam', 'Deaf Smith', 'Dickens', 'Donley', 'Floyd', 'Garza', 'Gray', 'Hale', 'Hall', 'Hansford', 'Hartley', 'Hemphill', 'Hockley', 'Hutchinson', 'King', 'Lamb', 'Lipscomb', 'Lubbock', 'Lynn', 'Moore', 'Motley', 'Ochiltree', 'Oldham', 'Parmer', 'Potter', 'Randall', 'Sherman', 'Swisher', 'Terry', 'Wheeler', 'Yoakum', 'Archer', 'Baylor', 'Brown', 'Callahan', 'Clay', 'Coleman', 'Comanche', 'Cottle', 'Eastland', 'Fisher', 'Foard', 'Hardeman', 'Haskell', 'Jack', 'Jones', 'Kent', 'Knox', 'Mitchell', 'Montague', 'Nolan', 'Runnels', 'Scurry', 'Shackelford', 'Stephens', 'Stonewall', 'Taylor', 'Throckmorton', 'Wichita', 'Wilbarger', 'Young', 'Collin', 'Cooke', 'Dallas', 'Denton', 'Ellis', 'Erath', 'Fannin', 'Grayson', 'Hood', 'Hunt', 'Johnson', 'Kaufman', 'Navarro', 'Palo Pinto', 'Parker', 'Rockwall', 'Somervell', 'Tarrant', 'Wise', 'Anderson', 'Bowie', 'Camp', 'Cass', 'Cherokee', 'Delta', 'Franklin', 'Gregg', 'Harrison', 'Henderson', 'Hopkins', 'Lamar', 'Marion', 'Morris', 'Panola', 'Rains', 'Red River', 'Rusk', 'Smith', 'Titus', 'Upshur', 'Van Zandt', 'Wood', 'Angelina', 'Hardin', 'Houston', 'Jasper', 'Jefferson', 'Nacogdoches', 'Newton', 'Orange', 'Polk', 'Sabine', 'San Augustine', 'San Jacinto', 'Shelby', 'Trinity', 'Tyler', 'Austin', 'Brazoria', 'Chambers', 'Colorado', 'Fort Bend', 'Galveston', 'Harris', 'Liberty', 'Matagorda', 'Montgomery', 'Walker', 'Waller', 'Wharton', 'Bastrop', 'Bell', 'Blanco', 'Bosque', 'Brazos', 'Burleson', 'Burnet', 'Caldwell', 'Coryell', 'Falls', 'Fayette', 'Freestone', 'Grimes', 'Hamilton', 'Hays', 'Hill', 'Lampasas', 'Lee', 'Leon', 'Limestone', 'Llano', 'Madison', 'McLennan', 'Milam', 'Mills', 'Robertson', 'San Saba', 'Travis', 'Washington', 'Williamson', 'Atascosa', 'Bandera', 'Bexar', 'Calhoun', 'Comal', 'DeWitt', 'Dimmit', 'Edwards', 'Frio', 'Gillespie', 'Goliad', 'Gonzales', 'Guadalupe', 'Jackson', 'Karnes', 'Kendall', 'Kerr', 'Kinney', 'La Salle', 'Lavaca', 'Maverick', 'Medina', 'Real', 'Uvalde', 'Val Verde', 'Victoria', 'Wilson', 'Zavala', 'Andrews', 'Borden', 'Coke', 'Concho', 'Crane', 'Crockett', 'Dawson', 'Ector', 'Gaines', 'Glasscock', 'Howard', 'Irion', 'Kimble', 'Loving', 'Martin', 'Mason', 'McCulloch', 'Menard', 'Midland', 'Pecos', 'Reagan', 'Reeves', 'Schleicher', 'Sterling', 'Sutton', 'Terrell', 'Tom Green', 'Upton', 'Ward', 'Winkler', 'Brewster', 'Culberson', 'El Paso', 'Hudspeth', 'Jeff Davis', 'Presidio', 'Aransas', 'Bee', 'Brooks', 'Cameron', 'Duval', 'Hidalgo', 'Jim Hogg', 'Jim Wells', 'Kenedy', 'Kleberg', 'Live Oak', 'McMullen', 'Nueces', 'Refugio', 'San Patricio', 'Starr', 'Webb', 'Willacy', 'Zapata']
    st.title('Likelihood of Child Abuse in Homeless Population in Texas')
    st.write("")
    st.subheader("This application allows social services to see which counties in Texas are more likely to have higher cases of child abuse in its homeless population so that efforts can be focused so as to mitigate the likelihood to maximum")
    st.write("The data for the model is taken from multiple sources")
    st.write("1. [CPI child abuse dataset](https://data.texas.gov/dataset/CPI-3-8-Abuse-Neglect-Investigations-Alleged-and-C/v63e-6dss)")
    st.write("2. [Texas Census Projection Estimates](https://demographics.texas.gov/data/decennial/2020/)")
    st.write("3. [PIT count dataset](https://www.hudexchange.info/programs/hdx/pit-hic/)")
    
    st.header("**How to use**")
    st.subheader("From the dropdown in the sidebar, select whether to use historical data or new data. For historical data, select county to examine and fiscal year (from 2017 to 2020). For entering new data, enter census estimates for the county for <18 group followed by overall homeless population under 18.")
    st.write("For getting relevant data, you can visit link 2 and 3 above")
    
    option = st.sidebar.selectbox('Select type of input',('Historical Data', 'Input Custom Data'))
    
    if option== 'Historical Data':
        county= st.text_input("County name", "Dallas")
        Year= st.selectbox('Select Year for analysis', (2017, 2018, 2019, 2020))
        if county not in state:
            st.error('Please enter valid County Name')
        if st.button("Predict"):
            historical(county, Year)
        
    else:
        county= st.text_input("Enter County name", "Dallas")
        homeless= st.number_input('Overall Homeless population under 18',value=5)
        wml= st.sidebar.number_input('Number of white males',value=5)
        wfl= st.sidebar.number_input('Number of white females',value=5, key = "wf")
        bml= st.sidebar.number_input('Number of black males',value=5, key = "bm")
        bfl= st.sidebar.number_input('Number of black females',value=5, key = "bf")
        hml= st.sidebar.number_input('Number of hispanic males',value=5, key = "hm")
        hfl= st.sidebar.number_input('Number of hispanic females',value=5, key = "hf")
        aml= st.sidebar.number_input('Number of asian males',value=5, key = "am")
        afl= st.sidebar.number_input('Number of asian females',value=5, key = "af")
        oml= st.sidebar.number_input('Number of other races males',value=5, key = "om")
        ofl= st.sidebar.number_input('Number of other races females',value=5, key = "of")
        if county not in state:
            st.error('Please enter valid County Name')
        if st.button("Predict"):
            da= [county, wml, wfl, bml, bfl, hml, hfl, aml, afl, oml, ofl]
            df = pd.DataFrame([da] ,  columns =  ["area_name", "Number of white males", "Number of white females", "Number of black males", "Number of black females",
                                                                                                   "Number of hispanic males", "Number of hispanic females", "Number of asian males", "Number of asian females",
                                                                                                   "Number of other races males", "Number of other races females"])
            custom(df, homeless)
        
        