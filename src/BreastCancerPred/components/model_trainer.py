import pandas as pd
import os
import logging
from BreastCancerPred.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import LogisticRegression
import joblib

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    def train_model(self):
        X_train_resampled = pd.read_csv(self.config.X_train_path)
        y_train_resampled = pd.read_csv(self.config.Y_train_path)

        log_reg = LogisticRegression(random_state=42)

        log_reg.fit(X_train_resampled, y_train_resampled)

        joblib.dump(log_reg, os.path.join(self.config.root_dir, self.config.model_name))
        print("DONE!!!")