from email import header
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def graph_raw_cyton_data(cyton_data: pd.DataFrame):    
    num_cols = len(cyton_data.columns) 
    for i in range(num_cols):
        # for each plot, let's title it the header that it comes from
        plt.title(cyton_data.columns[i])
        plt.plot(cyton_data.iloc[:, i])
        plt.show()




