import datetime
from datetime import datetime as dt
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from csv import writer
sns.set()

df = pd.read_csv('ol49.csv')
df['new_date']=pd.to_datetime(df['DATE'])
df['tgl'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])


option = st.selectbox('Parameter untuk dilihat data dan grafiknya', ('pH', 'DO', 'NH4', 'NO3'))



def chart(ylabel, xlabel, yvalues, xvalues, title=''):
    #create new graph
    
    fig = plt.figure(figsize = (10,7))
    plt.plot(xvalues, yvalues)
    plt.title(title, fontsize = 20, fontweight = 'bold')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return fig

#empty chart
c1, c2 = st.columns(2)
with c1:
    if 'space_initial' not in st.session_state:
        st.session_state.space_initial = st.empty()
with c2:
    if 'space_initial_2' not in st.session_state:
        st.session_state.space_initial_2 = st.empty()
        
#chart parameter
pH = chart('pH', 'Date', df[-24:]['pH'], df[-24:]['tgl'], title= 'Grafik pH')
DO = chart('DO', 'Date', df[-24:]['DO'], df[-24:]['tgl'], title= 'Grafik DO')
suhu = chart('Suhu', 'Date', df[-24:]['TEMP'], df[-24:]['tgl'], title= 'Grafik Suhu')
NH = chart('NH', 'Date', df[-24:]['NH4'], df[-24:]['tgl'], title= 'Grafik NH')
NO = chart('NO3', 'Date', df[-24:]['NO3'], df[-24:]['tgl'], title= 'Grafik NO')

#dataframe parameter
data_pH = df[-24:][['tgl', 'pH']]
data_DO = df[-24:][['tgl', 'DO']]
data_NH = df[-24:][['tgl', 'NH4']]
data_NO = df[-24:][['tgl', 'NO3']]
data_T0 = df[-24:][['tgl', 'TEMP']]

#chart column
    
if option == 'pH':
    st.session_state.space_initial.write(pH)
    st.session_state.space_initial_2.write(data_pH)
elif option == 'DO':
    st.session_state.space_initial.write(DO)
    st.session_state.space_initial_2.write(data_DO)
elif option == 'NH4':
    st.session_state.space_initial.write(NH)
    st.session_state.space_initial_2.write(data_NH)
elif option == 'NO3':
    st.session_state.space_initial.write(NO)
    st.session_state.space_initial_2.write(data_NO)