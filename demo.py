from rohlik_forecasting.logger import logging
from rohlik_forecasting.constants import COMPETITION_NAME
from rohlik_forecasting.configuration.kaggle_connection import KaggleAPIConnection

kaggleapi = KaggleAPIConnection()
logging.info(f'Kaggle API connection established')
kaggleapi.api.competition_download_files(COMPETITION_NAME)

logging.info(f'Competition files downloaded')