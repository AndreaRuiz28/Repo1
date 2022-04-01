import streamlit as st 
import pandas as pd
df = pd.read_csv ('https://raw.githubusercontent.com/napoles-uach/covid19mx/master/meteorite-landings.csv')
st.write(df)
st.map(df)
