
import connexion
import datetime
import logging

import sktime 
from sktime.forecasting.naive import NaiveForecaster
import pandas as pd

def naive_forecast():
    time_series = connexion.request.get_json();
    time_series = time_series['time_series']
    time_series = pd.Series(time_series)
    print(time_series)
    
    forecaster = NaiveForecaster(strategy="last")
    forecaster.fit(time_series)
    #TODO: Move to yaml spec
    fh= 6
    y_pred = forecaster.predict(fh)
    print(y_pred)
    return {"forecast": y_pred.values.tolist()}


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('naive_fc.yml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080)