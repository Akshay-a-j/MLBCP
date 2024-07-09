from BreastCancerPred.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    

    def preprocess(self):

        data = pd.read_csv(self.config.data_path)
        data["diagnosis"] = data["diagnosis"].replace({"M": 1, "B": 0})
