import base64
from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from src.component.get_data import Get_Data

from statsmodels.tsa.seasonal import seasonal_decompose,STL


class Seasonality():

    def deseasonal_plot(index:pd.Series,df:pd.Series,decomposition_result:List,model:str):
        plt.figure(figsize=(10,3))
        plt.plot(index,df, color = 'blue', linewidth=1, label = 'nifty 50')
        if model == 'additive':
            decomposed_nifty = df - decomposition_result.seasonal
        else:
            decomposed_nifty = df / decomposition_result.seasonal

        
        plt.plot(index,decomposed_nifty, color = 'red', linewidth ='1', label = 'decomposed_nifty_50')
        plt.tight_layout()
        plt.legend(loc = 'best')
        
        # Save the plot to a BytesIO object
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        base64_image = base64.b64encode(img_buffer.read()).decode('utf-8')
        plt.close()  # Close the plot to free memory
        return f"data:image/png;base64,{base64_image}"
        # return "working"




    def classical_decompose(model:str,period:int):
        data_fetcher = Get_Data()
        nifty = data_fetcher.get_data()
        c_d = seasonal_decompose(nifty['Close'],model=model,period=period)

        return Seasonality.deseasonal_plot(nifty.index,nifty['Close'],c_d,model)
    

    def stl_decompose(seasonal:int,period:int):
        data_fetcher = Get_Data()
        nifty = data_fetcher.get_data()
        stl_d = STL(nifty['Close'],seasonal = seasonal, period = period)
        stl_d_result = stl_d.fit()
        return Seasonality.deseasonal_plot(nifty.index,nifty['Close'],stl_d_result,model ='additive')
    
    
    



