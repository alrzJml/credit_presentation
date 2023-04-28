import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class MLCredit:

    def __init__(self, input_file='./german_credit_data 2.csv') -> None:
        self._file_path=input_file
        self._read_input()
        

    def _read_input(self):
        self._df = pd.read_csv(self._file_path, index_col=0)

    def describe(self):
        return self._df.describe()
    
    def get_data(self):
        return self._df
    
    def plot_dist(self, col):
        #See together in graphs accordings to Frequency and Count:
        df_good = self._df[self._df["Risk"] == 'good']
        df_bad = self._df[self._df["Risk"] == 'bad']

        fig, ax = plt.subplots(nrows=2, figsize=(12,8))
        plt.subplots_adjust(hspace = 0.4, top = 0.8)

        g1 = sns.distplot(df_good[f"{col}"], ax=ax[0], color="teal")
        g1 = sns.distplot(df_bad[f"{col}"], ax=ax[0], color='goldenrod')
        g1.set_title(f"{col} Distribuition", fontsize=15)
        g1.set_xlabel(f"{col}")
        g1.set_xlabel("Frequency")

        g2 = sns.countplot(x=f"{col}",data=self._df, palette="hls", ax=ax[1], hue = "Risk")
        g2.set_title(f"{col} Counting by Risk", fontsize=15)
        g2.set_xlabel(f"{col}")
        g2.set_xlabel("Count")
        plt.show()