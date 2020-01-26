from layer import Layer
from math import exp

class Neural_network:

    # layers bedzie wektorem, w ktorym przechowywana bedzie informacja o liczbie neuronow dla kazdej warstwy
    def __init__(self, layers_number_of_neurons, number_input_parameters):
        layers = []
        layers.append(Layer(1, number_input_parameters, layers_number_of_neurons[0]))
        for i in range(1, len(layers_number_of_neurons) - 1):
            layers.append(Layer(1, layers_number_of_neurons[i-1], layers_number_of_neurons[i]))
        layers.append(Layer(0, layers_number_of_neurons[-2], layers_number_of_neurons[-1]))
        self.layers = layers
        self.networkInput = []
        self.networkOutput = []
        self.expectedNetworkOutput = []


    def compute_outer_derivatives(self):
        lastLayer = self.layers[-1] # podobno jak da sie -1 to jest to ostatni element z listy
        previousLayer = self.layers[-2] # jak da sie -2 to jest on przed ostatni
        for i in range(lastLayer.get_neuron_number()):
            updatedNeuron = lastLayer.get_neuron(i)
            neuronWeights = updatedNeuron.get_weights()
            neuronWeightsDerivative = []
            neuronSumDerivative = []
            previousLayerOutput = previousLayer.get_layer_output()
            for j in range(len(neuronWeights)):

                neuronWeightsDerivative.append(2 * (self.networkOutput[i] - self.expectedNetworkOutput[i]) * previousLayerOutput[j])
                neuronSumDerivative.append(2 * (self.networkOutput[i] - self.expectedNetworkOutput[i]))

            updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
            updatedNeuron.set_sum_derivative(neuronSumDerivative)
            #print('outer---')
            #print(previousLayerOutput)
            #print(self.networkOutput[0])
            #print(self.expectedNetworkOutput[0])
            #print(neuronWeights)
            #print(neuronWeightsDerivative)
            #print('outer---')


    def compute_inner_derivatives(self, layerNumber):
        updatedLayer = self.layers[layerNumber]
        previousLayer = self.layers[layerNumber - 1]
        for i in range(updatedLayer.get_neuron_number()):
            updatedNeuron = updatedLayer.get_neuron(i)
            neuronWeights = updatedNeuron.get_weights()
            neuronSum = updatedNeuron.get_sum()
            activationDerivative = exp(neuronSum) / pow(1 + exp(neuronSum), 2)
            neuronOutputDerivative = self.compute_output_derivative(i, layerNumber)
            neuronWeightsDerivative = []
            neuronSumDerivative = []
            previousLayerOutput = previousLayer.get_layer_output()
            for j in range(len(neuronWeights)):

                neuronSumDerivative.append(neuronOutputDerivative * activationDerivative)

                neuronWeightsDerivative.append(neuronOutputDerivative * activationDerivative * previousLayerOutput[j])
                #print('----inner weights')
                #print(neuronOutputDerivative)
                #print(activationDerivative)
                #print(previousLayerOutput[j])
                #print('----inner weights')

            updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
            updatedNeuron.set_sum_derivative(neuronSumDerivative)
        #print('inner---')
        #print(layerNumber)
        #print(previousLayer.get_layer_output())
        #print(neuronWeightsDerivative)
        #print('inner---')


    def compute_output_derivative(self, neuronNumber, layerNumber):
        outputDerivative = 0.0
        nextLayer = self.layers[layerNumber + 1]
        for i in range(nextLayer.get_neuron_number()):
            neuron = nextLayer.get_neuron(i)
            neuronSumDer = neuron.get_sum_derivative()[0] 
            neuronWeights = neuron.get_weights()
            usedNeuronWeight = neuronWeights[neuronNumber]
            outputDerivative = outputDerivative + (neuronSumDer * usedNeuronWeight)
            #print('----compute_outer_derivatives')
            #print(neuronSumDer)
            #print(usedNeuronWeight)
            #print('----compute_outer_derivatives')
        return outputDerivative


    def compute_input_derivative(self):
        updatedLayer = self.layers[0]
        for i in range(updatedLayer.get_neuron_number()):
            updatedNeuron = updatedLayer.get_neuron(i)
            neuronWeights = updatedNeuron.get_weights()
            neuronSum = updatedNeuron.get_sum()
            activationDerivative = exp(neuronSum) / pow(1 + exp(neuronSum), 2)
            neuronOutputDerivative = self.compute_output_derivative(i, 0)
            neuronWeightsDerivative = []
            neuronSumDerivative = []
            for j in range(len(neuronWeights)):
                usedNetworkInput = self.networkInput[j]

                neuronSumDerivative.append(neuronOutputDerivative * activationDerivative)

                neuronWeightsDerivative.append(neuronOutputDerivative * activationDerivative * usedNetworkInput)

            updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
            updatedNeuron.set_sum_derivative(neuronSumDerivative)


    def backPropagation(self):
        self.compute_outer_derivatives() # ???
        for i in range(len(self.layers) - 2, 0, -1): # ???
            self.compute_inner_derivatives(i)
        self.compute_input_derivative()


    def stochasticDescent(self, beta):
        for layer in self.layers:
            for neuron in layer.get_layer_neurons():
                newWeights = []
                weights = neuron.get_weights()
                weightsDerivative = neuron.get_weights_derivative()
                for i in range(len(weights)):
                    updatedWeight = weights[i] - (beta * weightsDerivative[i])
                    newWeights.append(updatedWeight)
                neuron.set_weights(newWeights)


    def processData(self):
        self.layers[0].setInput(self.networkInput) # ???
        for i in range(1, len(self.layers), 1): # ???
            #print(self.layers[i - 1].get_layer_output())
            self.layers[i].setInput(self.layers[i - 1].get_layer_output())
            #print(self.layers[i - 1].get_layer_input())
            
        #print(self.layers[- 1].get_layer_output())
        self.networkOutput = self.layers[-1].get_layer_output()


    def precisionReached(self, epsilon):
        for i in range(len(self.networkOutput) - 1): # ???
            if (abs(self.networkOutput[i] - self.expectedNetworkOutput[i]) > epsilon): # ???
                return False
        return True


    def process_data_and_learn(self):
        i = 0
        while  i < 5:
            #print('Expected output', self.expectedNetworkOutput[0])
            self.processData()
            self.backPropagation()
            self.stochasticDescent(0.3)
            i = i + 1
        #for j in range(self.layers[-1].get_neuron_number()):
            #print(self.layers[-1].get_neuron(j).get_weights())
            #print(self.layers[-1].get_neuron(j).get_weights_derivative())
        #print('---')
    
    def set_network_input(self, inputList):
        self.networkInput = inputList
        
    def set_expected_output(self, outputList):
        self.expectedNetworkOutput = outputList
        
    def get_network_output(self):
        return self.networkOutput
