import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
import sktime
from sktime.forecasting.naive import NaiveForecaster
from sktime.forecasting.base import ForecastingHorizon

import pandas as pd


def app_naive_forecast(body):  # noqa: E501
    """app_naive_forecast

    Sending time series which needs to be forecasted # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501time_series = connexion.request.get_json();
    """ time_series = time_series['time_series']
    time_series = pd.Series(time_series)

    forecaster = NaiveForecaster(strategy="last")
    forecaster.fit(time_series)
    #TODO: Move to yaml spec

    fh = ForecastingHorizon(list(range(1,7)), relative = False)
    y_pred = forecaster.predict(fh)
    print(y_pred)
    return {"forecast": y_pred.values.tolist()} """
    print(type(body))

    time_series = body.to_dict()
    time_series = time_series["time_series"]
    time_series = pd.Series(time_series)

    forecaster = NaiveForecaster(strategy="last")
    forecaster.fit(time_series)
    #TODO: Move to yaml spec

    fh = ForecastingHorizon(list(range(1,7)), is_relative = True)
    y_pred = forecaster.predict(fh)
    print(y_pred)
    return {"forecast": y_pred.values.tolist()}    
