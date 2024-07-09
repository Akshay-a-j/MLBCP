from BreastCancerPred.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import logging

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    

    def preprocess(self):

        data = pd.read_csv(self.config.data_path)
        data["diagnosis"] = data["diagnosis"].replace({"M": 1, "B": 0})


        numerical_features = [
            'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
            'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean',
            'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se',
            'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
            'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
            'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst',
            'symmetry_worst', 'fractal_dimension_worst'
        ]

        # I# Fit and transform the numerical features
        scaler = StandardScaler() # brings the data to mean (mu) = 0 and standard deviation (sigma) = 1. eqn = [(x-mu)/sigma]
        data_scaled = data.copy()
        data_scaled[numerical_features] = scaler.fit_transform(data_scaled[numerical_features])
        
        # Split the data
        X = data_scaled.drop(columns=['diagnosis'], axis = 1)
        y = data_scaled['diagnosis']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify= y)

        # Oversampling the minority class to overcome class imbalance problem
        smote = SMOTE(random_state=42)
        X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
        y_train_resampled.value_counts(normalize=True)


        logging.info("Splited data into training and test sets")
        logging.info(X_train_resampled.shape)
        logging.info(X_test.shape)

        print(y_train_resampled.shape)
        print(y_test.shape)




