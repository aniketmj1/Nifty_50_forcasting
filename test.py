from src.component.get_data import Get_Data
import pandas as pd
from src.component.data_pre_pro import Data_Preprocessing
from src.time_series_components.seasonality import Seasonality
from src.pipeline.univariate_model_train import Univariate_Model_Train
import joblib
from statsmodels.tsa.arima.model import ARIMA



url = 'https://raw.githubusercontent.com/aniketmj1/NSE_Data/refs/heads/main/NIFTY%2050.csv'
nifty = Get_Data.get_data(url)
print(nifty.tail(10))
print(nifty.shape)
Data_Preprocessing.data_Preprocessing(nifty)
# print(nifty.shape)

print(Seasonality.classical_decompose(nifty,'additive',365))
# Univariate_Model_Train.arima_model(nifty['Close'])
print(joblib.load("src/saved_model/arima_model.joblib").predict(start=nifty.index[-10], end=nifty.index[-1]))
# for i in nifty.index[-10]:
#     print(i)
#     i-=1