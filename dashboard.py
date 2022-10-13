# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:30:44 2022

@author: shubhu
"""

import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Finance Dashbord')

tickers='AAPL','TSLA','MSFT','BTC-USD'

dropdown=st.multiselect('Pick your asserts',tickers)

start=st.date_input('start',value=pd.to_datetime('2020-01-01'))
end=st.date_input('end',value=pd.to_datetime('today'))

def relativeret(df):
    rel=df.pct_change()
    cum=(1+rel).cumprod()-1
    cumret=cum.fillna(0)
    return cumret
    
if len(dropdown) >0:
    #df=yf.download(dropdown,start,end)['Adj Close']
    df=relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)
    
