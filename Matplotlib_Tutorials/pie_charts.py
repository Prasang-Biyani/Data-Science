import matplotlib.pyplot as plt
slices = [7, 2, 2, 13]
actitives = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'g']
plt.pie(slices, labels=actitives, 
                startangle=90, shadow=True, autopct='%1.1f%%')
plt.show()