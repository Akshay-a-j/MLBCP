import os
import pandas as pd
import logging
from BreastCancerPred.entity.config_entity import ModelEValuationConfig
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import numpy as np
class ModelEvaluation:
    def __init__(self, config: ModelEValuationConfig):
        self.config = config

    
    def model_evaluation(self):

        X_test = pd.read_csv(self.config.X_test_path)
        y_test = pd.read_csv(self.config.Y_test_path)

        model = joblib.load(self.config.model_path)

        y_pred = model.predict(X_test)

        print(np.unique(y_pred, return_counts=True))

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        print(f"accuracy: {accuracy}, precision: {precision}, recall: {recall}, f1: {f1}")
        print(report)   