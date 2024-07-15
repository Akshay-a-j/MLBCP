from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the model
model = joblib.load('artifacts/Model_trainer/model.joblib')

# Initialize FastAPI app
app = FastAPI()

# Define the request body structure with Pydantic
class InputData(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the model API"}

# Define the prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    # Convert the request data to a DataFrame
    data_df = pd.DataFrame([data.model_dump()])
    
    # Rename columns to match those used during training
    data_df.rename(columns={
        "concave_points_mean": "concave points_mean",
        "concave_points_se": "concave points_se",
        "concave_points_worst": "concave points_worst"
    }, inplace=True)
    
    # Add placeholder columns for 'Unnamed: 0' and 'id'
    data_df['Unnamed: 0'] = 0
    data_df['id'] = 0

    # Ensure the DataFrame has the same columns as during training
    feature_columns = [
        'Unnamed: 0', 'id',
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 
        'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 
        'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 
        'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 
        'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 
        'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 
        'symmetry_worst', 'fractal_dimension_worst'
    ]
    data_df = data_df[feature_columns]

    # Make predictions
    prediction = model.predict(data_df)
    
    # Return the prediction
    return {"prediction": int(prediction[0])}



# Run the API with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5001)
