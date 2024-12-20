import pandas as pd


class Data_Preprocessing():
    def data_Preprocessing(df:pd.DataFrame):
        df.drop(df[df['Close'] == 0].index, inplace=True)
# Columns 
# 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'
        df['Date'] = pd.to_datetime(df['Date'])
        df.index = df['Date']
