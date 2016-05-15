import os

from scripts_test.test_neighbors import create_scatter
from neighbors.kNN  import file2matrix


"""
Run this file by console with this command : python -m main 
"""
path = os.path.dirname(os.path.abspath(__file__))

datingDataMat, datingLabels = file2matrix(path + '/archivos_test/datingTestSet2.txt')
create_scatter(datingDataMat)