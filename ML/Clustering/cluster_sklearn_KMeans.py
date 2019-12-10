import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
style.use('ggplot')

df = pd.read_excel('titanic.xls')
df.drop(['body', 'name'], 1, inplace=True)
# df.convert_objects(convert_numeric=True)
# df.replace(['female', 'male'], [0, 1], inplace=True)
df.fillna(0, inplace=True)

# print(df.head())

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

df = handle_non_numerical_data(df)
df.drop(['boat', 'sex'], 1, inplace=True)
X = np.array(df.drop(['survived'], 1)).astype(float)
X = preprocessing.scale(X)
y = np.array(df['survived'])

clf = KMeans(n_clusters=2)
clf.fit(X)

print(clf.cluster_centers_)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = clf.predict(predict_me)

    if prediction[0] == y[i]:
        correct += 1

print(correct / len(X))


