import pandas as pd
from abc import ABC,abstractmethod
from src.component.data_pre_pro import Data_Preprocessing


class Get_Data():
    def __init__(self):
        self.nifty = None

    def data_processing(self):
        nifty_url = 'https://raw.githubusercontent.com/aniketmj1/NSE_Data/refs/heads/main/NIFTY%2050.csv'
        self.nifty = pd.read_csv(nifty_url)
        Data_Preprocessing.data_Preprocessing(self.nifty)
        

    def get_data(self):
        self.data_processing()
        
        return self.nifty

