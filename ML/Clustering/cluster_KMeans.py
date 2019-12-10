import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
from sklearn import preprocessing
import random
style.use('ggplot')

X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8],
              [8, 8],
              [1, 0.6],
              [9, 11],
              [1, 3],
              [8, 9],
              [0, 3],
              [5, 4],
              [6, 4]
])

plt.scatter(X[:, 0], X[:, 1], s=100)
plt.show()

class K_Means:

    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def initalize_centroids(self, data):
        self.centroids = {n : data[n] for n in range(self.k)}

    def fit(self, data):
        self.initalize_centroids(data)

        for _ in range(self.max_iter):
            self.classifications = {i : [] for i in range(self.k)}

            for feature_set in data:
                distances = [np.linalg.norm(feature_set - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(classification)
            
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)
            
            prev_centroids = dict(self.centroids)

            optimized = True
            for c in self.centroids:
                orginal_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                # Check for optimization
                optimized = self.check_optimization(orginal_centroid, current_centroid, self.tol)
            if optimized == True:
                break
            
    def check_optimization(self, original, current, tol):
        if np.sum((current - original) / original * 100.0) > tol:
            return False
        return True

    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
        
# clf = K_Means()
# clf.fit(X)

# for centroid in clf.centroids:
#     plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], marker='o', color='k', s=150, linewidths=5)
# print(clf.centroids)

# colors = 10 * ['g', 'r', 'b', 'c', 'p']

# for classification in clf.classifications:
#      color = colors[classification]
#      for feature_set in clf.classifications[classification]:
#          plt.scatter(feature_set[0], feature_set[1], marker='x', color=color, s=150, linewidths=5)

# unknowns = np.array([[1, 3],
#                     [8, 9],
#                     [0, 3],
#                     [5, 4],
#                     [6, 4]])
# # for unknown in unknowns:
#     classification = clf.predict(unknown)
#     plt.scatter(unknown[0], unknown[1], marker="*", color=colors[classification], s=150, linewidths=5)

# plt.show()

def handle_non_numerical_data(df:pd.DataFrame):
    columns = df.columns.values.tolist()

    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1
            df[column] = list(map(convert_to_int, df[column]))

    return df

df = pd.read_excel('titanic.xls')
df.drop(['body', 'name'], 1, inplace=True)
# df.convert_objects(convert_numeric=True)
# df.replace(['female', 'male'], [0, 1], inplace=True)
df.fillna(0, inplace=True)

df = handle_non_numerical_data(df)
df.drop(['boat', 'sex'], 1, inplace=True)
X = np.array(df.drop(['survived'], 1)).astype(float)
X = preprocessing.scale(X)
y = np.array(df['survived'])

clf = K_Means()
clf.fit(X)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = clf.predict(predict_me)

    if prediction == y[i]:
        correct += 1

print(correct / len(X))