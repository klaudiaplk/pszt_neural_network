from neuron import Neuron


class Layer:

    def __init__(self, type, number_of_inputs, number_of_neurons):
        self.neuronNumber = number_of_neurons
        self.neurons = self.create_layer(self.neuronNumber, type, number_of_inputs)
        self.networkInput = []
        self.layerOutput = self.get_neurons_outputs(self.neurons)

    @staticmethod
    def create_layer(neuron_number, type, number_of_inputs):
        neurons = []
        for i in range(neuron_number):
            neuron = Neuron(type, number_of_inputs)
            neurons.append(neuron)
        return neurons

    @staticmethod
    def get_neurons_outputs(neurons):
        layerOutput = []
        for neuron in neurons:
            layerOutput.append(neuron.get_neuron_output())
        return layerOutput

    def get_neuron_number(self):
        return self.neuronNumber

    def get_layer_neurons(self):
        return self.neurons

    def get_neuron(self, position):
        return self.neurons[position]

    def setInput(self, networkInput):
        self.networkInput = networkInput

    def get_layer_output(self):
        return self.layerOutput
