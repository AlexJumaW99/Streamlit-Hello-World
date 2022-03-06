import pandas as pd
import streamlit as st 

df = pd.read_csv('fandango_scrape.csv')

st.title('Fandango Data')
st.write('Movie review data')

sidebar = st.sidebar
df_display = sidebar.checkbox('Display raw data', value=True)

if df_display:
    st.write(df)