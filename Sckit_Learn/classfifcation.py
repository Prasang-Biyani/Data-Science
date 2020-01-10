from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier

mnist = fetch_openml('mnist_784', version=1)
X, y = mnist['data'], mnist['target']

import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import numpy as np

# random_value = random.randrange(0, 10000)
some_digit = X[0]
some_label = y[0]
some_digit_image = some_digit.reshape(28, 28)
y = y.astype(np.uint8)
# plt.imshow(some_digit_image, cmap='binary')
# plt.show()

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)
print(sgd_clf.predict([some_digit]))

