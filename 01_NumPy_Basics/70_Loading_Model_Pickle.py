import pickle

# Saved model ko load karein
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

print("Model loaded and ready for predictions!")
