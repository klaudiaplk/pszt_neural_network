

def compute_outer_derivatives(outputValue, expectedOutputValue):
    lastLayerNeurons = layer[last].get_neurons()
    previousLayerNeurons = layer[last - 1].get_neurons()
    for i in range(size(lastLayerNeurons)):
        updatedNeuron = lastLayerNeurons.get_neuron(i)
        neuronWeights = updatedNeuron.get_weights()
        neuronWeightsDerivative = []
        neuronSumDerivative = []
        for j in range(size(neuronWeights)): 
            previousLayerNeuron = previousLayerNeurons.get_neuron(j)
            previousNeuronOutput = previousLayerNeuron.get_output()
            
            neuronWeightsDerivative[j] = 2 * (outputValue[i]-expectedOutputValue[i]) * previousNeuronOutput
            neuronSumDerivative[j] = 2 * (outputValue[i]-expectedOutputValue[i])
            
        updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
        updatedNeuron.set_sum_derivative(neuronSumDerivative)
    
      
def compute_inner_derivatives(layerNumber):
    updatedLayerNeurons = layer[layerNumber].get_neurons()
    previousLayerNeurons = layer[layerNumber - 1].get_neurons()
    for i in range(size(updatedLayerNeurons)):
        updatedNeuron = updatedLayerNeurons.get_neuron(i)
        neuronWeights = updatedNeuron.get_weights()
        neuronSum = updatedNeuron.get_sum()
        activationDerivative =  exp(neuronSum)/ pow(1 + exp(neuronSum), 2);
        neuronOutputDerivative = compute_output_derivative(i, layerNumber)
        neuronWeightsDerivative = []
        neuronSumDerivative = []
        for j in range(size(neuronWeights)): 
            previousLayerNeuron = previousLayerNeurons.get_neuron(j)
            previousNeuronOutput = previousLayerNeuron.get_output()
            
            sumDerivative[j] = neuronOutputDerivative * activationDerivative
    
            weightsDerivative[j] = neuronOutputDerivative * activationDerivative * previousNeuronOutput
            
        updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
        updatedNeuron.set_sum_derivative(neuronSumDerivative)


def compute_output_derivative(neuronNumber, layerNumber):
    outputDerivative = 0
    nextLayerNeurons = layer[layerNumber + 1].get_neurons()
    for i in range(nextLayerNeurons):
        neuron = nextLayerNeurons.get_neuron(i)
        neuronSum = neuron.get_sum_derivative()[i]
        neuronWeights = neuron.get_weights()
        usedNeuronWeight = neuronWeights[neuronNumber]
        outputDerivative += neuronSum * usedNeuronWeight
    return outputDerivative

def compute_input_derivative():
    updatedLayerNeurons = layer[0].get_neurons()
    for i in range(size(updatedLayerNeurons)):
        updatedNeuron = updatedLayerNeurons.get_neuron(i)
        neuronWeights = updatedNeuron.get_weights()
        neuronSum = updatedNeuron.get_sum()
        activationDerivative =  exp(neuronSum)/ pow(1 + exp(neuronSum), 2);
        neuronOutputDerivative = compute_output_derivative(i, layerNumber)
        neuronWeightsDerivative = []
        neuronSumDerivative = []
        for j in range(size(neuronWeights)): 
            usedNetworkInput = networkInput[j]
            
            sumDerivative[j] = neuronOutputDerivative * activationDerivative
    
            weightsDerivative[j] = neuronOutputDerivative * activationDerivative * usedNetworkInput
            
        updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
        updatedNeuron.set_sum_derivative(neuronSumDerivative)

def backpropagation():
    compute_outer_derivative()
    for i in range(number_of_layers - 1, 0, -1):
        compute_inner_derivative(i)
    compute_input_derivative()
        
def stochasticDescent(beta)
    for layer in layers:
        for neuron in layer.get_neurons():
            newWeights = []
            weights = neuron.get_weights()
            weightsDerivative = neuron.get_weights_derivative()
            for i in range(size(weights)):
                updatedWeight = weights[i] - (beta * weightsDerivative[i])
                newWeights.append(updatedWeight)
            neuron.set_weights(newWeights)
            
def processData():
    layers[0].setInput(networkInput)
    for i in range(1, number_of_layers, 1):  
        layer[i].setInput(layer[i - 1].get_layer_output())
    networkOutput = layers[last].get_layer_output()

def precisionReached(epsilon):
    for i in range(size(networkOutput))
        if(abs(networkOutput[i]-expectedNetworkOutput[i]) / expectedNetworkOutput[i] > epsilon)
            return False;
    return True;

def processDataAndLearn():
    numberOfIterations = 0;

    while(!precisionReached(0.0001) && i < 50):
        processData();
        backpropagation();
        stochasticDescent(0.3);


            

                    

    

    
