import matplotlib.pyplot as plt


Classes = ['A', 'B', 'C', 'D', 'E']
men = [50, 45, 58, 22, 49]
women = [38, 92, 50, 37, 15]

x = range(len(men))
plt.bar(x, men)
plt.bar(x, women, bottom=men)

plt.legend((['Male', 'Female']))
ax = plt.subplot()
ax.set_xticks(range(len(Classes)))
ax.set_xticklabels(Classes)
plt.show()
