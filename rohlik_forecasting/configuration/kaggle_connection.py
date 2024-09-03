import os
import zipfile
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
from rohlik_forecasting.constants import COMPETITION_NAME
from rohlik_forecasting.logger import logging

class KaggleAPIConnection:
    def __init__(self, competition_name = COMPETITION_NAME) -> None:
        self.competition_name = competition_name
        self.api = KaggleApi()
        self.api.authenticate()
        logging.info(f'Kaggle API connection established')

    