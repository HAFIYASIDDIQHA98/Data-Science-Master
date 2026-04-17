import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Dummy data generate karein
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=0)

# K-Means model (3 clusters)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Visualize karein
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.title("K-Means Clustering")
plt.show()
