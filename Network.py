import numpy as np
import math

class Network:
    def __init__(self, sizesVector):
        self.hiddenLayers = []
        for i in range(len(sizesVector)-1):
            self.hiddenLayers.append(Layer(sizesVector[i+1], sizesVector[i]))

    def displayText(self):
        for layer in self.hiddenLayers:
            print("Nastepna warstwa:\n")
            layer.displayText()
    def processVector(self, vector):
        outcome = vector
        for layer in self.hiddenLayers:
            outcome = self.activationFunction(layer.processVector(outcome))
        return outcome

    def activationFunction(self, element):
        return 1/(1+np.exp(-element))

    def activationFunctionPrime(self, element):
        return self.activationFunction(element)*(1-self.activationFunction(element))

    def learnFromGroupOfMoveDatas(self, moveDatas, speedRating):
        nabla_w = [np.zeros(layer.weights.shape) for layer in self.hiddenLayers]
        nabla_b = [np.zeros(layer.bias.shape) for layer in self.hiddenLayers]
        real_nabla_w = [np.zeros(layer.weights.shape) for layer in self.hiddenLayers]
        real_nabla_b = [np.zeros(layer.bias.shape) for layer in self.hiddenLayers]
        print("Ksztalt nabla_b:")
        print(np.shape(nabla_b))
        print("Ksztalt real_nabla_b:")
        print(np.shape(real_nabla_b))
        listx = [moveData.board for moveData in moveDatas]
        listy = [moveData.move*moveData.points for moveData in moveDatas]
        #print([moveData.move for moveData in moveDatas])
        print(listy)
        for x, y in zip(listx, listy):
            activation = x
            activations = [x] # list to store all the activations, layer by layer
            zs = [] # list to store all the z vectors, layer by layer
            for i in range(len(self.hiddenLayers)):
                z = np.dot(self.hiddenLayers[i].weights, activation)+self.hiddenLayers[i].bias
                zs.append(z)
                activation = self.activationFunction(z)
                activations.append(activation)
        # backward pass
            delta = self.costFunction(activations[-1], y) * self.activationFunctionPrime(zs[-1])
            nabla_b[-1] = delta
            nabla_w[-1] = np.dot(delta, activations[-2].transpose())
            for i in range(2, len(self.hiddenLayers)):
                z = zs[-i]
                delta = np.dot(self.hiddenLayers[-i+1].weights.transpose(), delta) * self.activationFunctionPrime(z)
                #if np.array_equal(delta, np.zeros(nabla_b[i].shape)):
                    #print("Delta wyszla zero")
                #else:
                    #print("Delta inna od zera")
                nabla_b[-i] = delta
                nabla_w[-i] = np.dot(delta, activations[-i-1].transpose())
            #print("suma Nabla_w jest sobie")
            #print(sum([np.sum(element) for element in nabla_w]))
            #print("suma Nabla_b jest sobie")
            #print(sum([np.sum(element) for element in nabla_b]))
            real_nabla_b = [sum(x,y) for x, y in zip(real_nabla_b, nabla_b)]
            real_nabla_w = [sum(x, y) for x, y in zip(real_nabla_w, nabla_w)]
        #print("Druga warstwa wag jest sobie")
        #print(self.hiddenLayers[1].weights)
        #print("A my ja zwiekszamy o")
        #print(real_nabla_w[1])
        print("suma real_nabla_w na koniec:")
        print(sum([np.sum(element) for element in real_nabla_b]))
        print("jak wyglada real_nabla_w:")
        print(np.shape(real_nabla_w))
        print("suma real_nabla_b na koniec:")
        print(sum([np.sum(element) for element in real_nabla_w]))
        print("suma tego, co mam zamiar odjac od weightsow:")
        print(sum([(speedRating*np.sum(weg))/(len(moveDatas)) for weg in real_nabla_w]))
        for i in range(len(self.hiddenLayers)):
            self.hiddenLayers[i].weights = self.hiddenLayers[i].weights-(speedRating*real_nabla_w[i])/(len(moveDatas))
            print("Odjalem od w")
            print((speedRating*real_nabla_w[i])/(len(moveDatas)))
            self.hiddenLayers[i].bias = self.hiddenLayers[i].bias-(speedRating*real_nabla_b[i])/(len(moveDatas))
            self.hiddenLayers[i].normalize(self.hiddenLayers[i].bias)
            self.hiddenLayers[i].normalize(self.hiddenLayers[i].weights)

    def costFunction(self,output,desiredOutput):
        cost = np.zeros(output.shape)
        for i in range(output.shape[0]):
            if desiredOutput[i] == 1:
                 cost[i]=pow(-1+output[i],3)
                 break
            elif desiredOutput[i] == -1:
                 cost[i]=pow(output[i],3)
                 break
        return cost

class Layer:
    def __init__(self, rows, columns):
        self.weights = np.random.rand(rows, columns)
        self.normalize(self.weights)
        self.bias = np.random.rand(rows,1)
        self.normalize(self.bias)
        #print("Inicjuje warstwe " + str(rows) + " na " + str(columns))
    def processVector(self, vector):
        #print("Mnoze " + str(vector) + " przez " + str(self.weights))
        return np.dot(self.weights, vector)+self.bias
    def displayText(self):
        print("weights:")
        print(self.weights)
        print("biases:")
        print(self.bias)
    def normalize(self, array):
        #up=1,down=0
        #print("Shape: ")
        #print(np.shape(array))
        #print("Sum: ")
        #print(np.sum(array))
        np.clip(array, a_min=0, a_max=None, out=array)
        sumAll = np.sum(array)
        for i in range(np.shape(array)[0]):
            array[i]=(array[i]/sumAll);
