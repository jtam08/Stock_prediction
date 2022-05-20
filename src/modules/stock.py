#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
from pandas_datareader.data import DataReader
import yfinance as yf
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM


# In[6]:


def data_pull(ticker):
    filepath = Path('data/raw_data_{}.csv'.format(ticker))
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df = DataReader(ticker, data_source='yahoo', start='2012-01-01', end=datetime.now())
    df.to_csv(filepath)
    df=pd.read_csv(filepath)
    return df


# In[7]:


def visualize_raw(ticker, df):
    plt.figure(figsize=(16,6))
    plt.title('Close Price History for {}'.format(ticker))
    plt.plot(df['Close'], linewidth=0.75)
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.savefig('output/figures/Close_Price_History_{}.png'.format(ticker), bbox_inches='tight')
    plt.show()


# In[8]:


def preprocess(df): 
    data = df.filter(['Close'])
    dataset = data.values
    return dataset

