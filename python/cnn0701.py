import matplotlib.pyplot as plt

plt.plot([10,20,30,40])
plt.show()

plt.plot([2,4,5,6], [81,93,91,97])
plt.show()


fig1 = plt.figure()
splt1 = fig1.add_subplot(1,2,1)
splt1.plot([1,2,3,4], [10, 20, 15, 25])
splt2 = fig1.add_subplot(1,2,2)
splt2.plot([2,4,5,6], [81,93,91,97])
plt.show()

fig2 = plt.figure()
splt1 = fig2.add_subplot(2,1,1)
splt1.plot([1,2,3,4], [10, 20, 15, 25])
splt2 = fig2.add_subplot(2,1,2)
splt2.plot([2,4,5,6], [81,93,91,97])
plt.show()

fig3 = plt.figure()
splt1 = fig3.add_subplot(2,2,1)
splt1.plot([1,2,3,4], [10, 20, 15, 25])
splt2 = fig3.add_subplot(2,2,2)
splt2.plot([2,4,5,6], [81,93,91,97])
splt3 = fig3.add_subplot(2,2,3)
splt3.plot([10, 11, 12, 13], [9,8,7,6])
splt4 = fig3.add_subplot(2,2,4)
splt4.plot([5, 6, 7, 8], [9,7,8,6])
plt.show()

