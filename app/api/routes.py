from flask import Blueprint, jsonify
from app.repositories.water_quality_repo import WaterQualityRepository
from app.core.use_cases import GetWaterQualityUseCase

water_quality_api = Blueprint('water_quality_api', __name__)

# Initialize the repository and use case
repository = WaterQualityRepository(data_path='app/data/dataset_limbah_cair_industri.xlsx')
use_case = GetWaterQualityUseCase(repository)

@water_quality_api.route('/api/data', methods=['GET'])
def get_all_water_quality_data():
    data = use_case.execute()
    return jsonify(data), 200
