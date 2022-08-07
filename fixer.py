from email import header
import pandas as pd

datapath = 'shubhJul-17-2022.csv'


data = pd.read_csv(datapath)

full_list = []
import numpy as np
#print(type(data.iloc[0, 0]))
y = (data.iloc[0, 0])

x = np.array(y.split())
print(x)
print(len(x))

for i in range(23):
    #print(len(data.iloc[i, 0]))
    all_times = []

    cell = data.iloc[i, 0]
    delimitered_cell_list = np.array(cell.split())
    print(len(delimitered_cell_list))
    for elem in delimitered_cell_list:
        all_times.append(elem)


    full_list.append(all_times)

full_list = np.array(full_list).T

import numpy as np
# emg_data = np.array(full_list[1:4]).T
import csv
header_data = ['Package Num Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', 'EXG Channel', "Accel", "Accel", "Accel", "Other", "Other", "Other", "Other", "Other", "Other", "Other", "Analog", "Analog", "Analog", "Timestamp", "Marker"]
with open("july-17-cleaned-shubh-data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(header_data)
    writer.writerows(full_list)


# Plot the graphs
import matplotlib.pyplot as plt

fig, ax = plt.subplots(23)
for i in range(23):
    ax[i].plot(full_list[:,i])
plt.show()




