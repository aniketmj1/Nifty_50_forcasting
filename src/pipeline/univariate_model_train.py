import joblib
from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import os




class Univariate_Model_Train():

    def arima_model(train_data:pd.Series):

        model = ARIMA(train_data,trend=None,order=(7,1,7))
        arima = model.fit()

        # save_path = os.path.join('src', "saved_model")

        # joblib.dump(arima,save_path)
        save_dir = "src/saved_model"
        os.makedirs(save_dir, exist_ok=True)  # Ensure directory exists
        save_path = os.path.join(save_dir, "arima_model.joblib")

        # Save the model
        joblib.dump(arima, save_path)
        print('Model Dumped')

