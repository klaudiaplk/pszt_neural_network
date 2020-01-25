from neuron import Neuron


class Layer:

    def __init__(self, type, number_of_inputs, number_of_neurons):
        self.neuronNumber = number_of_neurons
        self.neurons = self.create_layer(self.neuronNumber, self.type, self.numberOfInputs)
        self.type = type
        self.numberOfInputs = number_of_inputs

    @staticmethod
    def create_layer(neuron_number, type, number_of_inputs):
        neurons = []
        for i in range(neuron_number):
            neuron = Neuron(type, number_of_inputs)
            neurons.append(neuron)
        return neurons

    def get_neuron_number(self):
        return self.neuronNumber

    def get_neurons(self):
        return self.neurons
