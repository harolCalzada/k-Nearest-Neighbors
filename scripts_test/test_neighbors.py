import matplotlib
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)
def create_scatter(datingDataMat):
     ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
     plt.show()