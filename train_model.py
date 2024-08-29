import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle   

# Load the dataset
data = pd.read_excel('app/data/dataset_limbah_cair_industri.xlsx')

# Check for missing values
print("Checking missing value")
print(data.isnull().sum())

# Handle missing values
data = data.dropna()

# Remove non-numeric columns, such as DateTime if present
X = data.select_dtypes(include=['float64', 'int64'])

# Ensure that the target variable (y) is separate
y = data['COD (mg/L)']

# Drop the target variable from the feature set
X = X.drop(columns=['COD (mg/L)'], axis=1)

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, Y_train)

# Make predictions on the test set
Y_pred = model.predict(X_test)

# Evaluate the model using appropriate regression metrics
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')

# Save the model
with open('app/data/predict_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model has been trained and saved as predict_model.pkl")
