import matplotlib
import matplotlib.pyplot as plt
from numpy import array

fig = plt.figure()
ax = fig.add_subplot(111)

def compare_ice_cream_to_play_video_games(datingDataMat, datingLabels):
    """
        This funtion compare the numbers of Liters oof ice cream consumers per week to 
        time spend playing video games, the area diferents options to use pyplot.
    """
    #ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2],15.0*array(datingLabels), 15.0*array(datingLabels))    
    plt.show()