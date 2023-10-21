import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

# Generic function for optimal price
# define a function for finding the optimal price
def find_optimal_price(data, model, buying_price):
    start_price = data["PRICE"].min() - 1              # start price
    end_price = data["PRICE"].min() + 10               # end price
    
    # test dataframe
    test = pd.DataFrame(columns = ["PRICE", "QUANTITY"])  # choose required columns
    test['PRICE'] = np.arange(start_price, end_price, 0.01)
    test['QUANTITY'] = model.predict(test['PRICE'])         # make predictions
    test['PROFIT'] = (test["PRICE"] - buying_price) * test["QUANTITY"] # get profit of each price
    
    # Visualize the result
    plt.plot(test['PRICE'],test['QUANTITY'], linestyle = 'dotted') 
    plt.plot(test['PRICE'],test['PROFIT']) 
    plt.show()
    
    
    values_at_max_profit = test.loc[test['PROFIT'].idxmax()].to_frame().transpose()
    return values_at_max_profit