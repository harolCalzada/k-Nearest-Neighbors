# -*- coding: utf-8 -*-
from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
    
def classify0(inX, dataSet, labels, k):
    """
        La función toma 4 parametros:
        La primera el vector a clasificar llamado inX
        La segunda es el dataset con los ejemplos de entrenamiento
        La tercera los labels
        y la cuarta es el numero de vecinos
    """
    #recordar que shape retorna las dimensiones del array (3,2) 

    dataSetSize = dataSet.shape[0]
    #tile , esta funcion me duplica la matrix ejemp:  a = np.array([0, 1, 2])   >> np.tile(a, 2)   >> array([0, 1, 2, 0, 1, 2])
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet 
    print diffMat
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    #el argsort me ordena respecto a alguna dimension, por defecto agarra la ultima
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) +1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]
    
def file2matrix(filename):
    """
    La finalidad de esta función es returnar una matrix de ejemplos y la otra matriz de labels
    para testear esta función usar el archivo 'datingTestSet2.txt'
    """
    fr = open(filename)    
    arrayOfLines = fr.readlines()
    numberOfLines =len(arrayOfLines)  
    #la funcion zeros crea una matriz de puros 0
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0    
    for line in arrayOfLines:
        line = line.strip()        
        listFromLine= line.split('\t')
        returnMat[index, :] = listFromLine[0:3]        
        classLabelVector.append(int(listFromLine[-1]))        
        index += 1
    return returnMat, classLabelVector
        
        
