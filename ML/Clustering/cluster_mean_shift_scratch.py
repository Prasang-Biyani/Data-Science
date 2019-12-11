import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import estimate_bandwidth
from matplotlib import style
import numpy as np
import math
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

X, y = make_blobs(n_samples=50, n_features=2, centers=3, random_state=10)
# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()

class MeanShift:

    def __init__(self, radius=4, radius_norm_step=100):
        self.radius = radius
        self.radius_norm_step = radius_norm_step


    def gaussian_kernel(self, distance, kernel_bandwidth) -> float:
        result = (1 / kernel_bandwidth * math.sqrt(2 * math.pi)) * np.exp(-0.5 * (distance / kernel_bandwidth))
        return result

    def fit(self, data):

        if self.radius == None:
            common_centroid = np.average(data, axis=0)
            common_norm = np.linalg.norm(common_centroid)
            self.radius = common_norm / self.radius_norm_step

        centroids = {i : data[i] for i in range(len(data))}        
        
        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]
                numerator, denominator = 0, 0
                for feature_set in data:
                    # if np.linalg.norm(feature_set - centroid) <= self.radius:
                    #     in_bandwidth.append(feature_set)
                    distance = np.linalg.norm(feature_set - centroid)
                    numerator += self.gaussian_kernel(distance, self.radius) * feature_set
                    denominator += self.gaussian_kernel(distance, self.radius)
                    # find mean : Kernel * featureset / Kernel
        #         new_centroid = np.average(in_bandwidth, axis=0)
                mean_shift = numerator / denominator
                new_centroids.append(tuple(mean_shift))
            uniques = sorted(list(set(new_centroids)))
            prev_centroids = dict(centroids)

            centroids = {i: uniques[i] for i in range(len(uniques))}
            optimized = True
            # if the centroids are not moving, then it is properly optimized
            for i in centroids:
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    optimized = False
                if not optimized:
                    break
            if optimized:
                break

        self.centroids = centroids

    # def fit(self, data):

    #     if self.radius == None:
    #         common_centroid = np.average(data, axis=0)
    #         common_norm = np.linalg.norm(common_centroid)
    #         self.radius = common_norm / self.radius_norm_step
        
        
    
    def predict(self, data):
        pass


clf = MeanShift()
clf.fit(X)

centroids = clf.centroids

plt.scatter(X[:, 0], X[:, 1], s=150, c='brown')
print(centroids)

for c in centroids:
    plt.scatter(centroids[c][0], centroids[c][1], color='c', s=500)
# plt.scatter(common_centroid[0], common_centroid[1], marker='+', s=150)
plt.show()