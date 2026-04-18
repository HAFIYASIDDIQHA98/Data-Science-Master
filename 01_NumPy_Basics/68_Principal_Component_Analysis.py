import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# 1. Iris dataset load karein (4 features hain)
iris = load_iris()
X = iris.data

# 2. PCA apply karein: 4 columns ko 2 mein badlein
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 3. Result ko DataFrame mein dekhein
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
print("Original Shape:", X.shape)
print("Reduced Shape:", df_pca.shape)

# 4. Visualize karein
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Iris Dataset')
plt.show()
