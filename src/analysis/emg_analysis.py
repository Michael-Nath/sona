import pandas as pd
from utils.pull_brain_data import pull_brain_data

def main():
    emg_data = pull_brain_data()
    # print(emg_data.iloc[:, 0])
    pd.set_option('display.max_columns', None)
    print(emg_data["EXG Channel"].unique())
    # print(emg_data.drop_duplicates().head(5))


if __name__ == "__main__":
    main()