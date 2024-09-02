from rohlik_forecasting.logger import logging
from rohlik_forecasting.exception import RohlikForecastException
import sys
try:
    a=1/"10"
except Exception as e:  
    raise RohlikForecastException(e,sys) from e