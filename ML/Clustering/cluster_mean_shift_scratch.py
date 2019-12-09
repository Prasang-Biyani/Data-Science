import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from matplotlib import style
style.use('ggplot')


X, y = make_blobs(n_samples=10, n_features=2, centers=2, random_state=3)
# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()

class MeanShift:

    def __init__(self, bandwidth=4):
        self.bandwidth = bandwidth

    def fit(self, data):
        centroids = {i : data[i] for i in range(len(data))}

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]
                for feature_set in data:
                     


