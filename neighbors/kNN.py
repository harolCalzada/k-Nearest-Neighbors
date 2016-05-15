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
    
            
def autoNorm(dataSet):
    """
    This function normalize data between 0 and 1
    """
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals    
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals
        
   
def datingClassTest(datingDataMat,datingLabels ):
    """
    This funtion calculated, the number of test vectors, and this is used to decide which vectors from normMat will be
    used for testing and which for training. The two parts are then fed into our original
    kNN classifier, classify0. Finally, the error rate is calculated and displayed
    """
    hoRatio = 0.10
    datingDataMat, datingLabels = datingDataMat,datingLabels 
    normMat, ranges, minVals = autoNorm(datingDataMat)    
    m = normMat.shape[0]    
    numTestVecs = int(m*hoRatio)    
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m, :],datingLabels[numTestVecs:m],3)
        print "The classifier came back with: %d, the real answer is: %d" %(classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rates is %f" % (errorCount/float(numTestVecs))
    
    
def classifyPerson(datingDataMat, datingLabels):
    """
    """
    resultList = ['not at all', 'in small doses', 'in large doses']
    percenTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = datingDataMat, datingLabels
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percenTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
    print "You will probably like this person: ", resultList[classifierResult -1]