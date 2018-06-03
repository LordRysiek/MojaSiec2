from Network import Network
from BoardTools import BoardTools
import numpy as np

sizes = np.array([3,2,3])
network = Network(sizes)
print(network.processVector([1,1,1]))
