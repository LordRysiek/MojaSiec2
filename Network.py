import numpy as np
import math

class Network:
    def __init__(self, sizesVector):
        self.hiddenLayers = []
        for i in range(len(sizesVector)-1):
            self.hiddenLayers.append(Layer(sizesVector[i+1], sizesVector[i]))

    def processVector(self, vector):
        outcome = vector
        for layer in self.hiddenLayers:
            outcome = layer.processVector(outcome)
            outcome = [self.activationFunction(element) for element in outcome[:,0]]
        return outcome

    def activationFunction(self, element):
        return 1/(1+math.exp(-element))

class Layer:
    def __init__(self, rows, columns):
        self.weights = np.random.rand(rows, columns)
        self.bias = np.random.rand(rows,1)
        #print("Inicjuje warstwe " + str(rows) + " na " + str(columns))
    def processVector(self, vector):
        #print("Mnoze " + str(vector) + " przez " + str(self.weights))
        return np.dot(self.weights, vector)+self.bias
