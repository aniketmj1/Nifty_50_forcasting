import base64
import pandas as pd
import matplotlib.pylab as plt
from src.component.get_data import Get_Data
from io import BytesIO

class Plots():
    @staticmethod
    def nifty_plot():
        # nifty = Get_Data.get_data()
        data_fetcher = Get_Data()
        nifty = data_fetcher.get_data()
        plt.figure(figsize=(15,5))

        plt.plot(nifty.index,nifty['Close'], color = 'red' , linewidth = 1)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Nifty 50 ')

        # Saving the plot
        img_buffer = BytesIO()
        plt.savefig(img_buffer,format='png')
        img_buffer.seek(0)
        base64_imgage = base64.b64encode(img_buffer.read()).decode('utf-8')
        plt.close()

        return f"data:image/png;base64,{base64_imgage}"
