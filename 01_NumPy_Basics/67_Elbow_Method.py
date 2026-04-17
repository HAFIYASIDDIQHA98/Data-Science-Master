import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 1. Dummy data generate karein
X, _ = make_blobs(n_samples=500, centers=4, cluster_std=0.60, random_state=42)

# 2. WCSS (Within-Cluster Sum of Square) list banayein
wcss = []

# 3. 1 se 10 clusters tak check karein
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_) # inertia_ hi WCSS value hoti hai

# 4. Elbow Graph plot karein
plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters (K)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

print("Graph mein jahan se curve 'elbow' (kohni) ki tarah mud raha hai, wahi optimal K hai.")
