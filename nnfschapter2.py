inputlayer = [1.0, 2.0, 3.0, 2.5]
layer1neuron1weights = [0.2, 0.8, -0.5, 1]
layer1neuron2weights = [0.5, -0.91, 0.26, -0.5]
layer1neuron3weights = [-0.26, -0.27, 0.17, 0.87]


layer1neuron1bias = 2
layer1neuron2bias = 3
layer1neuron3bias = 0.5

l1n1output = (inputlayer[0] * layer1neuron1weights[0] + inputlayer[1] * layer1neuron1weights[1] +
              inputlayer[2] * layer1neuron1weights[2] + inputlayer[3] * layer1neuron1weights[3]
              + layer1neuron1bias)
l1n2output = (inputlayer[0] * layer1neuron2weights[0] + inputlayer[1] * layer1neuron2weights[1] +
              inputlayer[2] * layer1neuron2weights[2] + inputlayer[3] * layer1neuron2weights[3]
              + layer1neuron2bias)
l1n3output = (inputlayer[0] * layer1neuron3weights[0] + inputlayer[1] * layer1neuron3weights[1] +
              inputlayer[2] * layer1neuron3weights[2] + inputlayer[3] * layer1neuron3weights[3]
              + layer1neuron3bias)

firstlayeroutput =[l1n1output,l1n2output,l1n3output]
print(firstlayeroutput)