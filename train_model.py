import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import os

    # Load dataset
data_file = 'wellbeing_data.csv'
if not os.path.exists(data_file):
      raise FileNotFoundError(f"{data_file} not found. Please generate the dataset first.")

df = pd.read_csv(data_file)

    # Verify data
expected_columns = ['gad7', 'who5', 'cesdr10', 'loc', 'swls', 'scs', 'recommended_plan']
if list(df.columns) != expected_columns:
        raise ValueError(f"Unexpected columns: {df.columns.tolist()}")
if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values")
if len(df['recommended_plan'].unique()) != 7:
        raise ValueError(f"Expected 7 unique plans, found {len(df['recommended_plan'].unique())}")

    # Define features and target
features = ['gad7', 'who5', 'cesdr10', 'loc', 'swls', 'scs']
target = 'recommended_plan'

X = df[features]
y = df[target]

    # Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

    # Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    # Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

    # Predict on test set
y_pred = model.predict(X_test)

    # Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Test set accuracy: {accuracy * 100:.2f}%")

    # Print confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

    # Print feature importances
print("\nFeature Importances:")
for feature, importance in zip(features, model.feature_importances_):
    print(f"{feature}: {importance:.4f}")

    # Save model and label encoder
model_file = 'mental_health_model.pkl'
with open(model_file, 'wb') as f:
        pickle.dump({'model': model, 'label_encoder': label_encoder}, f)

print(f"\nModel and label encoder saved as {model_file}")

    # Verify model file exists
if not os.path.exists(model_file):
  raise RuntimeError(f"Failed to save {model_file}")
