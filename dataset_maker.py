import pandas as pd
import numpy as np
def make_dataset():
    dates = np.arange('2026-01-01', '2027-01-01', dtype='datetime64[D]')
    l =  len(dates)
    positions = np.random.choice(['SL', 'TP1', 'TP2', 'TP3', 'TP4', 'TP5', 'TP6', 'TP7', 'TP8', 'TP9', 'TP10', 'TP11', 'TP12', 'TP13', 'TP14', 'TP15', 'TP16', 'TP17', 'TP18', 'TP19', 'TP20'], size=l, p=[0.3, 0.1, 0.3, 0.1, 0.029227,0.024321,0.021098,0.018765,0.016543,0.014987,0.013210,0.011876,0.010345,0.009123,0.007890,0.006543,0.005432,0.004321,0.003210,0.002109,0.001000])
    strategies = np.random.choice(['A','B','C','D','E','F','G','H'], size=l)
    data = {
        'date': dates
        ,'position': positions
        ,'strategy': strategies
    }
    (pd.DataFrame(data)).to_csv(r'my_dataset2.csv', index=False, encoding='utf-8-sig')
