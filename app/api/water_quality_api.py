from flask import Blueprint, jsonify
from app.repositories.water_quality_repo import WaterQualityRepository

water_quality_api = Blueprint('water_quality_api', __name__)

# Initialize the repository with both data_path and model_path
repository = WaterQualityRepository(
    data_path='app/data/dataset_limbah_cair_industri.xlsx',
    model_path='app/data/predict_model.pkl'  # Provide the path to the model
)

@water_quality_api.route('/api/data', methods=['GET'])
def get_all_water_quality_data():
    data = repository.get_all_data()
    return jsonify(data), 200
