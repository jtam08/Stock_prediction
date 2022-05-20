#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from pandas_datareader.data import DataReader
import yfinance as yf
from datetime import datetime
from pathlib import Path


# In[7]:


def data_pull(data):
    filepath = Path('data/raw_data.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df = DataReader(data, data_source='yahoo', start='2012-01-01', end=datetime.now())
    df.to_csv(filepath)
    return df


# In[ ]:




