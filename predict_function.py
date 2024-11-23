import pandas as pd
from trained_model import final_model, normalizer, columns_to_normalize

def predict(input_data):
    """
    Make a prediction using the trained Random Forest model.
    
    Parameters:
    input_data (dict): A dictionary of health indicators.
    
    Returns:
    Probability of heart disease
    The top contributing factors.
    """
    # Convert input data to a DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Normalize the required columns
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
