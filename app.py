from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load model and label encoder
# Ensure the model and encoder files exist in the 'model' directory
model_path = os.path.join('model', 'wellbeing_model.pkl')
le_path = os.path.join('model', 'label_encoder.pkl')

# Add error handling for model loading
try:
    model = joblib.load(model_path)
    le = joblib.load(le_path)
    print("Model and Label Encoder loaded successfully.")
except FileNotFoundError:
    print(f"Error: Model or Label Encoder file not found at {model_path} or {le_path}")
    print("Please run train_model.py to generate them.")
    model = None # Set model to None to indicate failure
    le = None # Set le to None to indicate failure
except Exception as e:
    print(f"Error loading model or label encoder: {e}")
    model = None
    le = None


@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Wellbeing API! Use /predict to get recommendations.'})

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or le is None:
        return jsonify({'error': 'Model not loaded. Please check server logs.'}), 500

    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Invalid JSON received'}), 400

        # Define all expected keys and their default values
        # Defaulting missing scores to 0
        default_scores = {
            'gad7': 0,
            'who5': 0,
            'cesdr10': 0,
            'loc': 0, # Assuming 0 is a neutral default for Locus of Control
            'swls': 0, # Assuming 0 is a neutral default for SWLS
            'scs': 0  # Assuming 0 is a neutral default for SCS-SF
        }

        # Prepare input data, using provided values or defaults
        input_data_dict = {}
        for key in default_scores:
          input_data_dict[key] = data.get(key, default_scores[key]) # Use .get() with default

        # Ensure the keys are in the correct order as expected by the model
        # based on how X was defined in train_model.py
        # X = data[['gad7', 'who5', 'cesdr10', 'loc', 'swls', 'scs']]
        input_data = [[
            input_data_dict['gad7'],
            input_data_dict['who5'],
            input_data_dict['cesdr10'],
            input_data_dict['loc'],
            input_data_dict['swls'],
            input_data_dict['scs']
        ]]


        # Predict
        prediction = model.predict(input_data)
        recommended_plan = le.inverse_transform(prediction)[0]

        # Return a dictionary matching what PlanDetailScreen expects (e.g., {'recommended_plan': '...'})
        return jsonify({'recommended_plan': recommended_plan})

    except Exception as e:
        # Catch any other errors during processing/prediction
        app.logger.error(f"Prediction error: {e}") # Log the error on the server side
        return jsonify({'error': 'An internal error occurred during prediction.'}), 500

if __name__ == '__main__':
    # Using 0.0.0.0 makes the server accessible externally (e.g., from emulator)
    # In production, you might bind to '127.0.0.1' or specific IP and use a production server
    app.run(host='0.0.0.0', port=5000, debug=True) # debug=True is good for development