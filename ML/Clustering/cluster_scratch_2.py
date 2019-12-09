import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.datasets import make_blobs
import numpy as np
import pandas as pd
# from sklearn import preprocessing
import random
style.use('fivethirtyeight')

colors = ['r','g','b','c','k','o','y']

class K_Means:  

    def __init__(self, n_clusters=2, max_iter=300, tol=0.001):

        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol

    def intialize_centroids(self, data):
        # random.shuffle(data)
        self.centroids = {i : data[i] for i in range(self.n_clusters)}

    def fit(self, data):
        # Intialize the centroids
        self.intialize_centroids(data)
        # print(self.centroids)
        for _ in range(self.max_iter):
            self.classifications = {i : [] for i in range(self.n_clusters)}
            for feature_set in data:
                distances = [np.linalg.norm(feature_set - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(feature_set)
            
            prev_centroids = dict(self.centroids)
            # Calculate centroids
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)
            optimized = True
            
            for c in self.centroids:
                orignal_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                optimized = self.check_optimize(current_centroid, orignal_centroid, self.tol)
            if optimized:
                break

                # print(classification)
    def check_optimize(self, current_centroid, original_centroid, tol) -> bool:
        if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > tol:
            return False
        return True

    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
            
X, y = make_blobs(n_samples=50, centers=2, n_features=2, random_state=2)
clf = K_Means(max_iter=300)
clf.fit(X)
# print(clf.centroids)
for centroid in clf.centroids:
    # print(centroid)
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], marker="*", c='b')
# plt.show()
# for classification in clf.classifications:
#     color = colors[classification]
#     for feature_set in clf.classifications[classification]:
#         plt.scatter(feature_set[0], feature_set[1], marker='x', c=color)

random_sample = np.random.random((1, 2))
result = clf.predict(random_sample)
print(result)



