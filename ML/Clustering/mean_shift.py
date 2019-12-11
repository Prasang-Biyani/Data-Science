from sklearn.datasets import make_blobs
from sklearn.cluster import estimate_bandwidth, MeanShift
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import style
style.use('fast')


X, _ = make_blobs(n_samples=500, n_features=2, centers=2, random_state=10)
# plt.scatter(X[:, 0], X[:, 1], c=_)
# plt.show()

def neighbourhood_points(X:list, centroid, radius=5) -> list:
    in_bandwidth = []
    for feature_set in X:
        distance = np.linalg.norm(feature_set - centroid)
        if distance <= radius:
            in_bandwidth.append(distance)
    return in_bandwidth

def gaussian_kernel(distance, bandwidth):
    val = (1 / bandwidth * math.sqrt(2 * math.pi)) * np.exp(-0.5 * (distance / bandwidth) ** 2)
    return val

def main():
    kernel_bandwidth = estimate_bandwidth(X)
    


if __name__ == "__main__":
    main()



