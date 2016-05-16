import os
from scripts_test.test_neighbors import compare_ice_cream_to_play_video_games
from neighbors.kNN  import file2matrix, autoNorm, datingClassTest, classifyPerson, img2vector, handwritingClassTest

"""
Run this file by console with this command : python -m main.py 
"""
path = os.path.dirname(os.path.abspath(__file__))
data_test_2  = path + '/archivos_test/datingTestSet2.txt'
datingDataMat, datingLabels = file2matrix(data_test_2)
file_test_number = path + '/archivos_test/testDigits/3_46.txt'
path_training_digits = path + '/archivos_test/trainingDigits/'
training_digits = os.listdir(path + '/archivos_test/trainingDigits/')


def graph_ice_video():
    return compare_ice_cream_to_play_video_games(datingDataMat, datingLabels)


def norm():
    normMat, ranges, minVals = autoNorm(datingDataMat)
    return normMat, ranges, minVals

    
def test_error_ratio():
    return datingClassTest(datingDataMat, datingLabels)

    
def test_classify_person():
    return classifyPerson(datingDataMat, datingLabels)

    
def test_img2vector():
    return img2vector(file_test_number)


def classify_number(training_digits, path_training_digits):
    return handwritingClassTest(training_digits, path_training_digits)