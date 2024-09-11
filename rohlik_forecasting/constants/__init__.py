import os
from datetime import datetime
from pathlib import Path

# Constants

CONFIG_FILE_PATH= Path("config/config.yaml")
PARAMS_FILE_PATH= Path("params.yaml")
SCHEMA_FILE_PATH= Path("schema.yaml")

PIPELINE_NAME :str = "rohlik_forecasting"
ARTIFACT_DIR :str = "artifacts"
COMPETITION_NAME :str = "rohlik-orders-forecasting-challenge"
PREPROCESSING_OBJECT_FILE_NAME :str = "preprocessing_object.pkl"
MODEL_FILE_NAME :str = "model.pkl"
TARGET_COLUMN :str = "orders"
TRAIN_FILE_NAME :str = "train.csv"
TEST_FILE_NAME :str = "test.csv"

# Data Ingestion

DATA_INGESTION_COLLECTION_NAME :str = "rohlik_forcast"
DATA_INGESSTION_DIR_NAME :str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR_NAME :str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO :float = 0.2
