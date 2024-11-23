import pandas as pd
import os
import pickle

# Get the absolute path of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define file paths relative to the current file's location
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
NORMALIZER_PATH = os.path.join(BASE_DIR, "normalizer.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "columns_to_normalize.pkl")

# Load the model and other resources
with open(MODEL_PATH, 'rb') as file:
    final_model = pickle.load(file)

with open(NORMALIZER_PATH, 'rb') as file:
    normalizer = pickle.load(file)

with open(COLUMNS_PATH, 'rb') as file:
    columns_to_normalize = pickle.load(file)

def predict(input_data):
    """
    Make a prediction using the trained Random Forest model.
    
    Parameters:
    input_data (dict): A dictionary of health indicators.
    
    Returns:
    Probability of heart disease
    The top contributing factors.
    """
  
    input_df = pd.DataFrame([input_data])
    
 
    input_norm = input_df.copy()
    input_norm[columns_to_normalize] = normalizer.transform(input_df[columns_to_normalize])
    
    # Predictions
    prediction = final_model.predict(input_norm)[0]
    probability = final_model.predict_proba(input_norm)[0][1]
    
    # Feature contributions
    feature_contributions = pd.DataFrame({
        'feature': input_df.columns,
        'contribution': final_model.feature_importances_ * abs(input_norm.iloc[0])
    }).sort_values('contribution', ascending=False)
    
    return {
        'prediction': 'High Risk' if prediction == 1 else 'Low Risk',
        'probability': probability,
        'top_factors': feature_contributions.head(10)
    }

