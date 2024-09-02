from flask import Flask
from app.api.routes import water_quality_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(water_quality_api)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
