import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()
data = []


MAX_DATA_POINTS = 500  

def update(frame):
    global data

 
    stock = yf.Ticker("AAPL")
    price_data = stock.history(period="1d", interval="1m")['Close'].values[-50:]

    
    if len(price_data) > 0 and not np.isnan(price_data).any():
        price_data = np.array(price_data, dtype=np.float64)  
        price_data = [p + np.random.uniform(-0.1, 0.1) for p in price_data]
    else:
        price_data = [] 

  
    data.extend(price_data)

    if len(data) > MAX_DATA_POINTS:
        data = data[-MAX_DATA_POINTS:]

    
    ax.clear()
    ax.hist(data, bins=20, color='skyblue', edgecolor='black')  
    ax.set_title('Live Stock Price Histogram')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')


ani = animation.FuncAnimation(fig, update, interval=5000)  
plt.show()
