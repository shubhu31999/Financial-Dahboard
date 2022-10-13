# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:07:10 2022

@author: shubhu
"""

import pandas as pd
import streamlit as st

data=pd.read_csv("C:\\Users\\shubhu\\Documents\\Streamlit app test\\financial_dash.csv")
df=pd.DataFrame(data)
df=df.set_index('symbol')

dropdown1=st.selectbox('Choose the sector',df.sector.unique())
dropdown2=st.selectbox('Choose the parametre',df.columns[df.columns!='sector'])

values=df[df.sector==dropdown1][[dropdown2]]

st.bar_chart(values)

