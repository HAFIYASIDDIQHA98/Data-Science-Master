import pandas as pd

# Note: This expects a 'data.csv' file in the same folder
# For now, we use a try-except to show the logic
try:
    df = pd.read_csv('data.csv')
    print("CSV Loaded Successfully!")
except:
    print("Please add a 'data.csv' file to test this script.")
