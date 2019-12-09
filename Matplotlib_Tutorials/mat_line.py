import matplotlib.pyplot as plt
import numpy as np
x1 = [10, 4, 3, 8]
y1 = [5, 13, 1, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.xlabel('Plot Number')
plt.ylabel('Important Variable')

plt.title('Interesting Graph')
plt.legend()
plt.show()
