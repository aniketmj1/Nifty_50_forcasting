from statsmodels.tsa.stattools import adfuller,kpss
import pandas as pd


class Stationarity_Test():
    def adf_test(df:pd.DataFrame):
        adf = adfuller(df['Close'],autolag='AIC')
        adf_result = pd.Series(adf[0:4],index=["Test Statistic",
            "p-value",
            "#Lags Used",
            "Number of Observations Used"])
        
        for key,value in adf[4].items():
            adf_result["Critical Value (%s)" % key] = value
        
        return adf_result
    


    def kpss_test(df:pd.DataFrame):
        kpsstest = kpss(df['Close'], regression="c", nlags="auto")
        kpss_result = pd.Series(kpsstest[0:3],index=["Test Statistic", "p-value", "Lags Used"])
        
        for key,value in kpsstest[3].items():
            kpss_result["Critical Value (%s)" % key] = value
        
        return kpss_result
