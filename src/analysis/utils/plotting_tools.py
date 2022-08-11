from email import header
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HEADERS = ['Package Num Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', "Accel", "Accel", "Accel", "Other", "Other", "Other", "Other", "Other", "Other", "Other", "Analog", "Analog", "Analog", "Timestamp", "Marker"]

def graph_raw_cyton_data(cyton_data: pd.DataFrame):    
    num_cols = len(cyton_data.columns) 
    print(num_cols)
    fig, ax = plt.subplots(num_cols)
    for i in range(num_cols):
        ax[i].plot(cyton_data.iloc[:, i])
    plt.show()




