# Stock Prediction
#### A stock price prediction algorithm can help us predict future stock prices. In this way, we can reap significant benefits as an individual or corporation. This is a hard task to accomplish as there are many confounding factors that may influence a stock's performance. Here, we examine the ability of an LSTM network in predicting stock prices.
* The data for this project was pulled using yfinance on Python which utilizes free APIs provided by Yahoo Finance
_____
### LSTM Network
#### LSTM (Long Short Term Memory) networks are a special kind of recurrent neural networks (RNNs). RNNs are networks with loops in them, allowing information to persist, forming 'memory'. LSTM networks take this a step further, and can learn long-term dependencies, making them particularly useful in working with time-series data such as stock data.

#### Data from Yahoo Finance was used for this project, taking stock close price data to train the model, and using it to predict future data. Opening the experiments.ipynb notebook, any ticker that is followed by Yahoo Finance can be entered and this model will return raw data for the stock in question, visualization of historical stock close price, as well as process and run this close price through an LSTM network. 95% of the data will be used as training data, and this model will predict on 5% of test data (roughly 2 months of predictions). A visualization of the model's accuracy as well as a tabulated form of the predictions and test data will also be returned with this model.
