from flask import Blueprint, request, jsonify
from app.repositories.water_quality_repo import WaterQualityRepository
from app.use_cases.predict_water_quality_use_case import PredictWaterQualityUseCase

prediction_api = Blueprint('prediction_api', __name__)

# Initialize the repository and use case
repository = WaterQualityRepository(
    data_path='app/data/dataset_limbah_cair_industri.xlsx',
    model_path='app/data/predict_model.pkl'
)
use_case = PredictWaterQualityUseCase(repository)

import numpy as np

def convert_to_serializable(obj):
    if isinstance(obj, (bool, np.bool_)):  # Tambahkan np.bool_
        return bool(obj)  # Konversi ke tipe bool Python
    elif isinstance(obj, (int, float, str, list, dict)):
        return obj
    # Handle other non-serializable types here if needed
    raise TypeError(f"Type {type(obj)} not serializable")

@prediction_api.route('/api/predict', methods=['POST'])
def predict_water_quality():
    input_data = request.json
    result = use_case.execute(input_data)
    serializable_result = {key: convert_to_serializable(value) for key, value in result.items()}
    return jsonify(serializable_result), 200

