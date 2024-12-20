import pandas as pd
from abc import ABC,abstractmethod


class Get_Data():
    def get_data(url:str):
        nifty = pd.read_csv(url)
        return nifty

