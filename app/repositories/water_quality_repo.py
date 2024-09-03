import pandas as pd
import pickle

class WaterQualityRepository:
    def __init__(self, data_path, model_path):
        self.data_path = data_path
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        with open(self.model_path, 'rb') as f:
            return pickle.load(f)

    def get_all_data(self):
        data = pd.read_excel(self.data_path)
        return data.to_dict(orient='records')

    def predict_bod(self, input_data):
        # Define the exact feature names used during model training
        feature_names = [
            "pH", 
            "Conductivity (µS/cm)", 
            "Turbidity (NTU)", 
            "TSS (mg/L)", 
            "COD (mg/L)",
            "Total Coliform (MPN/100mL)"
        ]

        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Check if all required features are present in the input data
        missing_features = [f for f in feature_names if f not in input_df.columns]
        if missing_features:
            raise ValueError(f"Missing required features: {missing_features}")

        # Ensure the input features are in the correct order
        input_df = input_df[feature_names]

        # Predict BOD using the model
        predicted_bod = self.model.predict(input_df)[0]

        # Determine if an anomaly is detected
        anomaly_detected = predicted_bod > 150  # Example threshold

        return {
            "predicted_BOD": predicted_bod,
            "anomaly_detected": anomaly_detected
        }
