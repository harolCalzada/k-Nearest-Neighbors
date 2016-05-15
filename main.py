import os

from scripts_test.test_neighbors import compare_ice_cream_to_play_video_games
from neighbors.kNN  import file2matrix, autoNorm, datingClassTest, classifyPerson


"""
Run this file by console with this command : python -m main.py 
"""
path = os.path.dirname(os.path.abspath(__file__))
data_test_2  = path + '/archivos_test/datingTestSet2.txt'
datingDataMat, datingLabels = file2matrix(data_test_2)


def graph_ice_video():
    return compare_ice_cream_to_play_video_games(datingDataMat, datingLabels)
    
def norm():
    normMat, ranges, minVals = autoNorm(datingDataMat)
    return normMat, ranges, minVals
    
def test_error_ratio(datingDataMat, datingLabels):
    return datingClassTest(datingDataMat, datingLabels)
    
def test_classify_person(datingDataMat, datingLabels):
    return classifyPerson(datingDataMat, datingLabels)