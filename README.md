# Industrial Wastewater Quality Prediction API
This project provides a RESTful API to predict the quality of industrial wastewater using machine learning models. The API is built using the Flask framework, following the Clean Architecture approach. The dataset consists of various water quality parameters, including pH, conductivity, turbidity, TSS, BOD, COD, Total Coliform, and Color.

## Dataset
The dataset consists of the following features:

- pH: Acidity/alkalinity level.
- Conductivity: The ability of water to conduct electric current.
- Turbidity: Clarity of the water.
- TSS: Total suspended solids.
- BOD: Biochemical oxygen demand.
- COD: Chemical oxygen demand.
- Total Coliform: Indicator of bacterial contamination.
- Color: The color of the water sample.
** Target Variable
You can choose any of the above features as the target variable (Y) to predict based on the other features (X).

## Getting Started

To get started with the `industrial-wastewater-quality-prediction-api` project, follow the instructions below.

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)
- MySQL database
- Pandas
- Scikit-learn
- Joblib
- Flask

### Train the Model

Before running the application, you'll need to train the Random Forest model on your dataset. You can either use a real dataset or a dummy dataset for testing purposes.

1. **Prepare the Dataset**:

   - Ensure your dataset contains the following columns: `Conductivity`, `pH`, `TSS`, `Turbidity`, `COD`, `Total Coliform`, `Color`, And `BOD`

2. **Train the Model**:
   - Run the script to train the model:
   ```bash
   train_model.py
   ```

This will generate a trained Random Forest model stored in the models directory.

### Running the Application

To start the Flask application, use the following commands:

1. **Install Dependencies**:

```
    pip install -r requirements.txt
```

2. **Run the Application:**:

```
    python run.py
```

The Flask application will start and be available at http://localhost:5000.

### API

The water-quality-ml-api exposes several endpoints to interact with the trained model and water quality data.

**Predict Survival Rate**:

- Endpoint: api/predict
- Method: POST
- Request Body

```
    {
       "pH": 7.2,
       "Conductivity": 1200,
       "Turbidity": 3.5,
       "TSS": 15,
       "COD": 220,
       "TotalColiform": 50,
       "Color": 100
    }
```

- Response

```
{
    "predicted_BOD": 180,
    "anomaly_detected": false
}
```

**Get Water Quality Data:**:

- Endpoint: api/dataset
- Method: GET
- Response

```
[
    {
        "pH": 7.2,
        "Conductivity": 1200,
        "Turbidity": 3.5,
        "TSS": 15,
        "BOD": 180,
        "COD": 220,
        "TotalColiform": 50,
        "Color": 100
    },
]
```
