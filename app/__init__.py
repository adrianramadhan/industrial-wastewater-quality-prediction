from flask import Flask
from app.api.water_quality_api import water_quality_api
from app.api.prediction_api import prediction_api  # Import the new prediction API

def create_app():
    app = Flask(__name__)
    app.register_blueprint(water_quality_api)
    app.register_blueprint(prediction_api)  # Register the prediction API
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
