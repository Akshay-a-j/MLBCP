import os
from urllib import request
from pathlib import Path
from BreastCancerPred.entity.config_entity import DataIngestionConfig
import logging
from BreastCancerPred.utils.common import get_size
import zipfile



class DataIngestion:
    def __init__(self, config = DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename= self.config.local_data_file
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_f:
            zip_f.extractall(unzip_path)
    

