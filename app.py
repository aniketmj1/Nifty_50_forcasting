from flask import Flask,render_template
from src.time_series_components.seasonality import Seasonality
from src.component.get_data import Get_Data
from src.plots.plots import Plots
from src.time_series_components.stationarity_test import Stationarity_Test


app = Flask(__name__)

# url = 'https://raw.githubusercontent.com/aniketmj1/NSE_Data/refs/heads/main/NIFTY%2050.csv'
# nifty = Get_Data.get_data()

@app.route("/")
def home():
    img = Plots.nifty_plot()
    adf_test = Stationarity_Test.adf_test()
    kpss_test = Stationarity_Test.kpss_test()
    classical_decompostion = Seasonality.classical_decompose('additive',365)
    classical_decompostion_multi = Seasonality.classical_decompose('multiplicative',365)
    stl_decompostion = Seasonality.stl_decompose(365,365)
    return render_template('index.html',show = img,adf = adf_test,kpss = kpss_test,
                            classical_decompostion=classical_decompostion,
                            classical_decompostion_multi =classical_decompostion_multi,
                            stl_decompostion = stl_decompostion)
    






if __name__ == '__main__':  
   app.run(debug=True)