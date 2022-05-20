#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas_datareader.data import DataReader
import yfinance as yf
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


def visualize_model(df, training_data_len, predictions):
    data = df.filter(['Close'])
    # Plot the data
    train = data[:training_data_len]
    valid = data[training_data_len:]
    valid['Predictions'] = predictions
    valid.to_csv('output/test_predictions/test_predictions.csv')
    # Visualize the data
    plt.figure(figsize=(32,12))
    plt.title('Model of Data')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.plot(train['Close'], linewidth=0.75)
    plt.plot(valid[['Close', 'Predictions']], linewidth=0.75)
    plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
    plt.savefig('output/figures/model_accuracy.png', bbox_inches='tight')
    plt.show()

