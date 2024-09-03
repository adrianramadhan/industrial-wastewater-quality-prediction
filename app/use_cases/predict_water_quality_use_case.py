class PredictWaterQualityUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, input_data):
        # Predict BOD
        prediction_result = self.repository.predict_bod(input_data)
        predicted_bod = prediction_result["predicted_BOD"]
        
        # Simple rule-based anomaly detection
        anomaly_detected = predicted_bod > 150  # Example threshold

        return {
            "predicted_BOD": predicted_bod,
            "anomaly_detected": anomaly_detected
        }
