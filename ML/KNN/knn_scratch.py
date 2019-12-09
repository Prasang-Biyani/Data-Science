import warnings
import random
from math import sqrt
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

def k_nearest_neigbors(data, predict, k=3):
    
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')
    # knn algo
    distances = list()
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))    
            distances.append([euclidean_distance, group])

    votes = sorted(distances, key=lambda x: x[0])[:k]
    voting_label = [vote[1] for vote in votes]
    # voting_distance = [vote[0] for vote in votes]
    common_voting = Counter(voting_label).most_common(1)[0]
    # confidence_score = Counter(voting_label).most_common(1)
    return common_voting[0], common_voting[1] / k

df = pd.read_csv('breast-cancer-wisconsin.csv')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
# convert int to float
full_data = df.astype(float).values.tolist()
# shuffle the data
random.shuffle(full_data)

test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size * len(full_data))]
test_data = full_data[-int(test_size * len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])
for i in test_data:
    test_set[i[-1]].append(i[:-1])

# for train in train_set:
#     print(train)

correct = 0
total = 0
for group in test_set:
    for data in test_set[group]:
         vote, confidence = k_nearest_neigbors(train_set, data, k=5)
         if vote == group:
             correct+=1
         else:
            print(confidence)
         total+=1

print('Accuracy : ', correct/total)








# [[plt.scatter(value[0], value[1], s=100, color=key) for value in dataset[key]] for key in dataset]
# plt.scatter(new_features[0], new_features[1], color=result[0])
# plt.show()

 

