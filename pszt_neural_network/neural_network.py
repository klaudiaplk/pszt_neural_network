from math import exp

from pszt_neural_network.layer import Layer


class Neural_network:

    def __init__(self, layers_number_of_neurons, number_input_parameters):
        """Create neural network.

        :param layers_number_of_neurons: number of neurons in layers
        :param number_input_parameters: number of input parameters
        """
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
        """Compute and set weights derivatives and sum derivatives for each neuron in the output layer.

        """
        lastLayer = self.layers[-1]
        previousLayer = self.layers[-2]
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

    def compute_inner_derivatives(self, layerNumber):
        """Compute and set weights derivatives and sum derivatives for each neuron in hidden layers (except first one).

        :param layerNumber: number of layer
        """
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

            updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
            updatedNeuron.set_sum_derivative(neuronSumDerivative)

    def compute_output_derivative(self, neuronNumber, layerNumber):
        """Compute derivative output for selected neuron after neuronNumber in layer selected after the layerNumber.

        :param neuronNumber: neuron number in layer
        :param layerNumber: layer number
        :return: derivative output for selected neuron
        """
        outputDerivative = 0.0
        nextLayer = self.layers[layerNumber + 1]
        for i in range(nextLayer.get_neuron_number()):
            neuron = nextLayer.get_neuron(i)
            neuronSumDer = neuron.get_sum_derivative()[0]
            neuronWeights = neuron.get_weights()
            usedNeuronWeight = neuronWeights[neuronNumber]
            outputDerivative = outputDerivative + (neuronSumDer * usedNeuronWeight)

        return outputDerivative

    def compute_input_derivative(self):
        """Compute and set weights derivatives and sum derivatives for each neuron in the first layers.

        """
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
        """Backward gradient propagation.

        """
        self.compute_outer_derivatives()
        for i in range(len(self.layers) - 2, 0, -1):
            self.compute_inner_derivatives(i)
        self.compute_input_derivative()

    def stochasticDescent(self, beta):
        """Method of steepest descent.

        :param beta: beta parameter
        """
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
        """Data processing. Set inputs for layers and network output.

        """
        self.layers[0].setInput(self.networkInput)
        for i in range(1, len(self.layers), 1):
            self.layers[i].setInput(self.layers[i - 1].get_layer_output())
        self.networkOutput = self.layers[-1].get_layer_output()

    def precisionReached(self, epsilon):
        """Count precision.

        :param epsilon: limit of precision
        :return: information whether precision has been achieved
        """
        for i in range(len(self.networkOutput) - 1):
            if abs(self.networkOutput[i] - self.expectedNetworkOutput[i]) > epsilon:
                return False
        return True

    def process_data_and_learn(self):
        """Data processing and neural network learning.

        """
        i = 0
        while i < 50:
            self.processData()
            self.backPropagation()
            self.stochasticDescent(0.3)
            i = i + 1
    
    def set_network_input(self, inputList):
        """Set neural network input.

        :param inputList: neural network input
        """
        self.networkInput = inputList
        
    def set_expected_output(self, outputList):
        """Set expected neural network output.

        :param outputList: expected neural network output.
        """
        self.expectedNetworkOutput = outputList
        
    def get_network_output(self):
        """Get neural network output.

        :return: neural network output
        """
        return self.networkOutput
