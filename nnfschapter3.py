import numpy as np
import nnfs
from nnfs.datasets import spiral_data
import matplotlib.pyplot as plt
nnfs.init()
class Layer_Dense:
    def __init__(self,inputs,neurons):
        #Initialize weights and biases
        self.weights = 0.01*np.random.randn(inputs,neurons)
        self.biases = np.zeros(shape=(1,neurons))
    def forward(self,inputs):
        #Calculate output values from inputs weights and biases
        self.output = np.dot(inputs, self.weights) +self.biases

class Activation_Relu:
    def forward(self, inputs):
        self.output = np.maximum(0,inputs)
class Activation_Softmax:

    # Forward pass
    def forward(self, inputs):

        # Get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1,
                                            keepdims=True))
        # Normalize them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1,
                                            keepdims=True)

        self.output = probabilities
dense1 = Layer_Dense(2,3)

X,y = spiral_data(100,3)
a1=Activation_Relu()
dense2 = Layer_Dense(3,3)
a2 = Activation_Softmax()
dense1.forward(X)
a1.forward(dense1.output)
dense2.forward(a1.output)
a2.forward(dense2.output)
print(a2.output)
