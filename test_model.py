import pandas as pd
import pickle
import os

# Load trained model and label encoder
model_file = 'mental_health_model.pkl'
if not os.path.exists(model_file):
    raise FileNotFoundError(f"{model_file} not found. Please train the model first.")

with open(model_file, 'rb') as f:
    saved_data = pickle.load(f)
    model = saved_data['model']
    label_encoder = saved_data['label_encoder']

# Load test inputs
test_file = 'test_inputs.csv'
if not os.path.exists(test_file):
    raise FileNotFoundError(f"{test_file} not found. Please create test inputs.")

test_df = pd.read_csv(test_file)

# Define features
features = ['gad7', 'who5', 'cesdr10', 'loc', 'swls', 'scs']

# Ensure test data has required columns
missing_cols = [col for col in features if col not in test_df.columns]
if missing_cols:
    raise ValueError(f"Test data missing columns: {missing_cols}")

X_test = test_df[features]

# Make predictions
predictions_encoded = model.predict(X_test)
predictions = label_encoder.inverse_transform(predictions_encoded)

# Assign expected plans based on rules
expected_plans = []
for _, row in test_df.iterrows():
    gad7 = row['gad7']
    who5 = row['who5']
    cesdr10 = row['cesdr10']
    if gad7 >= 15 or cesdr10 >= 20:
        plan = 'Therapist, Meditation, Reading about the illness, Journaling'
    elif cesdr10 >= 15:
        plan = 'Therapist, Reading about the illness, Mood tracking, Taking another test'
    elif gad7 >= 10:
        plan = 'Talking with chatbot, Reading quotes, Meditation, Journaling'
    elif who5 <= 25:
        plan = 'Journaling, Mood tracking, Community events, Music'
    elif gad7 >= 5 or cesdr10 >= 10:
        plan = 'Meditation, Reading quotes, Mood tracking'
    elif who5 >= 75:
        plan = 'Music, Community events, Taking another test, Reading quotes'
    else:
        plan = 'Journaling, Meditation, Music'
    expected_plans.append(plan)

# Compare predictions to expected
results = pd.DataFrame({
    'gad7': test_df['gad7'],
    'who5': test_df['who5'],
    'cesdr10': test_df['cesdr10'],
    'loc': test_df['loc'],
    'swls': test_df['swls'],
    'scs': test_df['scs'],
    'Predicted_Plan': predictions,
    'Expected_Plan': expected_plans,
    'Correct': predictions == expected_plans
})

# Print results
print("\nTest Results:")
print(results)
print("\nAccuracy:", results['Correct'].mean() * 100, "%")
print("\nIncorrect Predictions (if any):")
print(results[~results['Correct']][['gad7', 'who5', 'cesdr10', 'Predicted_Plan', 'Expected_Plan']])