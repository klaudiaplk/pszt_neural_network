from layer import Layer
from math import exp

class Neural_network:

    # layers bedzie wektorem, w ktorym przechowywana bedzie informacja o liczbie neuronow dla kazdej warstwy
    def __init__(self, layers_number_of_neurons):
        layers = []
        for i in range(layers_number_of_neurons.size() - 1):
            layers.append(Layer(1, layers[i-1], layer))
        self.layers = layers
        self.networkInput = #jeden wiersz z naszej tabeli


    def compute_outer_derivatives(self, outputValue, expectedOutputValue):
        lastLayerNeurons = self.layers[-1].get_layer_neurons() # podobno jak da sie -1 to jest to ostatni element z listy
        previousLayerNeurons = self.layers[-2].get_layer_neurons() # jak da sie -2 to jest on przed ostatni
        for i in range(lastLayerNeurons.size()):
            updatedNeuron = lastLayerNeurons.layer.get_neuron(i)
            neuronWeights = updatedNeuron.get_weights()
            neuronWeightsDerivative = []
            neuronSumDerivative = []
            for j in range(neuronWeights.size()):
                previousLayerNeuron = previousLayerNeurons.get_neuron(j)
                previousNeuronOutput = previousLayerNeuron.get_neuron_output()

                neuronWeightsDerivative.append(2 * (outputValue[i] - expectedOutputValue[i]) * previousNeuronOutput)
                neuronSumDerivative.append(2 * (outputValue[i] - expectedOutputValue[i]))

            updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
            updatedNeuron.set_sum_derivative(neuronSumDerivative)


    def compute_inner_derivatives(self,layerNumber):
        updatedLayerNeurons = self.layers[layerNumber].get_layer_neurons()
        previousLayerNeurons = self.layers[layerNumber - 1].get_layer_neurons()
        for i in range(updatedLayerNeurons.size()):
            updatedNeuron = updatedLayerNeurons.get_neuron(i)
            neuronWeights = updatedNeuron.get_weights()
            neuronSum = updatedNeuron.get_sum()
            activationDerivative = exp(neuronSum) / pow(1 + exp(neuronSum), 2)
            neuronOutputDerivative = self.compute_output_derivative(i, layerNumber)
            neuronWeightsDerivative = []
            neuronSumDerivative = []
            for j in range(neuronWeights.size()):
                previousLayerNeuron = previousLayerNeurons.get_neuron(j)
                previousNeuronOutput = previousLayerNeuron.get_neuron_output()

                neuronSumDerivative.append(neuronOutputDerivative * activationDerivative)

                neuronSumDerivative.append(neuronOutputDerivative * activationDerivative * previousNeuronOutput)

            updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
            updatedNeuron.set_sum_derivative(neuronSumDerivative)


    def compute_output_derivative(self, neuronNumber, layerNumber):
        outputDerivative = 0
        nextLayerNeurons = self.layers[layerNumber + 1].get_layer_neurons()
        for i in range(nextLayerNeurons):
            neuron = nextLayerNeurons.get_neuron(i)
            neuronSum = neuron.get_sum_derivative()[i] # nie moge na chwile obecna zweryfikowac czy to [i] jest poprawne
            neuronWeights = neuron.get_weights()
            usedNeuronWeight = neuronWeights[neuronNumber]
            outputDerivative = outputDerivative + (neuronSum * usedNeuronWeight)
        return outputDerivative


    def compute_input_derivative(self):
        updatedLayerNeurons = self.layers[0].get_layer_neurons()
        for i in range(updatedLayerNeurons.size()):
            updatedNeuron = updatedLayerNeurons.get_neuron(i)
            neuronWeights = updatedNeuron.get_weights()
            neuronSum = updatedNeuron.get_sum()
            activationDerivative = exp(neuronSum) / pow(1 + exp(neuronSum), 2)
            neuronOutputDerivative = self.compute_output_derivative(i, 0)
            neuronWeightsDerivative = []
            neuronSumDerivative = []
            for j in range(neuronWeights.size()):
                usedNetworkInput = self.networkInput[j]

                neuronSumDerivative.append(neuronOutputDerivative * activationDerivative)

                neuronWeightsDerivative.append(neuronOutputDerivative * activationDerivative * usedNetworkInput)

            updatedNeuron.set_weights_derivative(neuronWeightsDerivative)
            updatedNeuron.set_sum_derivative(neuronSumDerivative)


    def backPropagation(self):
        self.compute_outer_derivatives(outputValue, expectedOutputValue)
        for i in range(number_of_layers - 1, 0, -1):
            self.compute_inner_derivatives(i)
        self.compute_input_derivative()


    def stochasticDescent(self, beta):
        for layer in self.layers:
            for neuron in layer.get_layer_neurons():
                newWeights = []
                weights = neuron.get_weights()
                weightsDerivative = neuron.get_weights_derivative()
                for i in range(weights.size()):
                    updatedWeight = weights[i] - (beta * weightsDerivative[i])
                    newWeights.append(updatedWeight)
                neuron.set_weights(newWeights)


    def processData(self):
        self.layers[0].setInput(networkInput)
        for i in range(1, number_of_layers, 1):
            self.layers[i].setInput(self.layers[i - 1].get_layer_output())
        networkOutput = self.layers[-1].get_layer_output()


    def precisionReached(self, epsilon):
        for i in range(networkOutput.size()):
            if (abs(networkOutput[i] - expectedNetworkOutput[i]) / expectedNetworkOutput[i] > epsilon)
                return False
        return True


    def processDataAndLearn(self):
        i = 0
        while self.precisionReached(0.0001) != True and i < 50:
            self.processData()
            self.backPropagation()
            self.stochasticDescent(0.3)
            i = i + 1
