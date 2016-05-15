import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

def compare_ice_cream_to_play_video_games(datingDataMat):
    """
        This funtion compare the numbers of Liters oof ice cream consumers per week to 
        time spend playing video games
    """
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])    
    plt.show()