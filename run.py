import pandas as pd
import pickle
import sys

# Load the trained model from the .pkl file
model_filename = "forestmodel.pkl"
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Make predictions on the test data
n = len(sys.argv)

if len(sys.argv) < 2:
    print("Please provide the path to the test data CSV file as a command-line argument.")
    exit()

testdd = pd.read_csv(sys.argv[1])

uuidcol = testdd["uuid"]
new_data = testdd.drop(['uuid', 'datasetId'], axis=1)

# Use the loaded model to make predictions
new_predictions = loaded_model.predict(new_data)

result_df = pd.DataFrame({'uuid': uuidcol, 'HR': new_predictions})
result_df.to_csv('results.csv', index=False)
