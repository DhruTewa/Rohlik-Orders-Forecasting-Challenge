# Components##
import os
import zipfile
import kaggle
from rohlik_forecasting import logger 
#from rohlik_forecasting.utils.main_utils import get_size
from kaggle.api.kaggle_api_extended import KaggleApi
from rohlik_forecasting.entities.config_entity import DataIngestionConfig
from pathlib import Path

import shutil
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self) -> str:
        # Authenticate with Kaggle API
        api = KaggleApi()
        api.authenticate()
 
        try: 
            dataset_url = f"{self.config.kaggle_competition_name}"
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            api.competition_download_files(dataset_url, path=zip_download_dir)
            logger.logging.info(f"Downloaded dataset from kaggle to {zip_download_dir}")
            #logger.info(f"Downloaded dataset from kaggle to {self.config.root_dir}")
        
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        zip_file_path = os.path.join(self.config.local_data_file,'rohlik-orders-forecasting-challenge.zip')
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.logging.info(f"Extracted dataset to {unzip_path}")