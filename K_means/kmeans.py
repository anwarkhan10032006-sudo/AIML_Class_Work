# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Input dataset
# Sepal Length and Petal Length
X = np.array([
    [5.1, 1.4],  # P1
    [4.9, 1.5],  # P2
    [6.2, 4.5],  # P3
    [5.9, 4.2],  # P4
    [6.5, 5.2],  # P5
    [7.1, 5.9]   # P6
])

points = ["P1","P2","P3","P4","P5","P6"]

# Apply K-Means with K = 3
kmeans = KMeans(n_clusters=3, random_state=0)
labels = kmeans.fit_predict(X)

# Centroids
centroids = kmeans.cluster_centers_

# Print Sample Output format
print("Data Point  Sepal Length  Petal Length  Cluster Label")
for i in range(len(X)):
    print(f"{points[i]}        {X[i][0]}          {X[i][1]}          Cluster {labels[i]}")

# Visualization
plt.scatter(X[:,0], X[:,1], c=labels, s=100)

# Plot centroids
plt.scatter(centroids[:,0], centroids[:,1], marker='X', s=300, label="Centroids")

# Labels
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("K-Means Clustering Visualization")

# Show data point names
for i, txt in enumerate(points):
    plt.annotate(txt, (X[i][0], X[i][1]))

plt.legend()
plt.show()