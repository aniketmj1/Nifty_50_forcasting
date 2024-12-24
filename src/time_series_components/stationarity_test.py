from statsmodels.tsa.stattools import adfuller,kpss
import pandas as pd
from src.component.get_data import Get_Data


class Stationarity_Test():
    def adf_test():
        data_fetcher = Get_Data()
        nifty = data_fetcher.get_data()
        adf = adfuller(nifty['Close'],autolag='AIC')
        adf_result = pd.Series(adf[0:4],index=["Test Statistic",
            "p-value",
            "#Lags Used",
            "Number of Observations Used"])
        
        for key,value in adf[4].items():
            adf_result["Critical Value (%s)" % key] = value
        
        return adf_result
    


    def kpss_test():
        data_fetcher = Get_Data()
        nifty = data_fetcher.get_data()
        kpsstest = kpss(nifty['Close'], regression="c", nlags="auto")
        kpss_result = pd.Series(kpsstest[0:3],index=["Test Statistic", "p-value", "Lags Used"])
        
        for key,value in kpsstest[3].items():
            kpss_result["Critical Value (%s)" % key] = value
        
        return kpss_result
