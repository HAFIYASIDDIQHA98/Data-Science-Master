from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

digits = load_digits()
pca = PCA(n_components=0.95) # Keep 95% information
X_reduced = pca.fit_transform(digits.data)
print(f"Reduced features from {digits.data.shape[1]} to {X_reduced.shape[1]}")
