import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from matplotlib import style
import numpy as np
style.use('ggplot')

# X = np.array([[1, 2],
#               [1.5, 1.8],
#               [5, 8 ],
#               [8, 8],
#               [1, 0.6],
#               [9,11],
#               [8,2],
#               [10,2],
#               [9,3],])


X, y = make_blobs(n_samples=150, n_features=2, centers=4, random_state=10)
# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()

class MeanShift:

    def __init__(self, radius=3):
        self.radius = radius

    def fit(self, data):
        centroids = {i : data[i] for i in range(len(data))}

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]
                for feature_set in data:
                    if np.linalg.norm(feature_set - centroid) < self.radius:
                        in_bandwidth.append(feature_set)
                new_centroid = np.average(in_bandwidth, axis=0)
                new_centroids.append(tuple(new_centroid))
            uniques = sorted(list(set(new_centroids)))
            prev_centroids = dict(centroids)

            centroids = {i : np.array(uniques[i]) for i in range(len(uniques))}

            optimized = True

            for i in centroids:
                # check if old centroid and new centroid are same or not
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    # if not equal, then it is not optimized
                    optimized = False
                # if not optimized, then break out of the loop
                if not optimized:
                    break

            if optimized:
                    break

        self.centroids = centroids

    def predict(self, data):
        pass


clf = MeanShift()
clf.fit(X)
centroids = clf.centroids

plt.scatter(X[:, 0], X[:, 1], s=150)

for c in centroids:
    plt.scatter(centroids[c][0], centroids[c][1], color='k', s=150)
plt.show()