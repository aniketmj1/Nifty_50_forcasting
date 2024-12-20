from src.component.get_data import Get_Data
import pandas as pd
from src.component.data_pre_pro import Data_Preprocessing
from src.time_series_components.seasonality import Seasonality


url = 'https://raw.githubusercontent.com/aniketmj1/NSE_Data/refs/heads/main/NIFTY%2050.csv'
nifty = Get_Data.get_data(url)
print(nifty.head(2))
print(nifty.shape)
Data_Preprocessing.data_Preprocessing(nifty)
# print(nifty.shape)

print(Seasonality.classical_decompose(nifty,'additive',365))