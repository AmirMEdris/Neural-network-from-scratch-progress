def evaluate_neuron(neuron,inputlist):
    x=0
    for input,weight in zip(inputlist, neuron['weights']):
        x += weight*input
    return x+neuron['bias']

def evaluate_layer(layer,inputslist):
    return list(map(lambda x: evaluate_neuron(layer[x], inputslist), layer))

def make_layer(weights,biases):
    x=0
    layer={}
    for neuron_weights, neuron_bias in zip(weights, biases):
        x += 1
        layer['neuron ' + str(x)] = {'weights': neuron_weights,
                                    'bias': neuron_bias}
    return layer


inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

layer_1 = make_layer(weights, biases)
layer_2 = make_layer(weights, biases)
layer_3 = make_layer(weights, biases)

output=evaluate_layer(layer_1, inputs)
output=evaluate_layer(layer_2, output)
output=evaluate_layer(layer_3, output)

print(output)

print(list(map(lambda x: [x, layer_1[x]['weights']], layer_1)))
print(layer_1['neuron 2'])