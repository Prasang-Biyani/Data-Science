import matplotlib.pyplot as plt
import numpy as np

x = np.array([4, 10, 6, 3, 9, 5])
y = np.array([1, 2, 3, 2, 6, 2])
# Co-relation between two data points
plt.scatter(x, y, s=100, label='skitscat', color='k', marker='*')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.title('Hello WOrld')
plt.show()