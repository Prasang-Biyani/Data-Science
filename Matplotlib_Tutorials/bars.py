import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

# x2 = [1, 3, 5, 9, 11]
# y2 = [7, 8, 2, 4, 2]

plt.bar(x, y, label='Bars1', color='blue')
# plt.bar(x2, y2, label='Bars2', color='green')

# population_ages = [10, 15, 13, 22, 52, 62, 45, 21, 78, 34, 23]
# bins = [10, 20, 30, 40, 50, 60, 70, 80]
# ids = [x for x in range(len(population_ages))]
# plt.hist(population_ages, bins=bins, histtype='bar', rwidth=0.6, color='c')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.show()

