from pszt_neural_network.neuron import Neuron


class Layer:

    def __init__(self, type, number_of_inputs, number_of_neurons):
        """Create layer.

        :param type: type of apply function, if 1 then activation function is sigmoid,
        if 0 then activation function is linear
        :param number_of_inputs: number of neuron inputs
        :param number_of_neurons: number of neurons in layer
        """
        self.neuronNumber = number_of_neurons
        self.neurons = self.create_layer(self.neuronNumber, type, number_of_inputs)
        self.layerInput = []
        self.layerOutput = []

    @staticmethod
    def create_layer(neuron_number, type, number_of_inputs):
        """Create layer.

        :param neuron_number: number of neuron in layer
        :param type: type of apply function, if 1 then activation function is sigmoid,
        if 0 then activation function is linear
        :param number_of_inputs: number of neurons in layer
        :return: list of neurons belonging to the layer
        """
        neurons = []
        for i in range(neuron_number):
            neuron = Neuron(type, number_of_inputs)
            neurons.append(neuron)
        return neurons

    def get_layer_output(self):
        """Get layer output.

        :return: output from the layer
        """
        self.layerOutput = []
        for neuron in self.neurons:
            self.layerOutput.append(neuron.get_neuron_output())
        return self.layerOutput

    def get_neuron_number(self):
        """Get number of neurons in the layer.

        :return: number of neurons in the layer
        """
        return self.neuronNumber

    def get_layer_neurons(self):
        """Get neurons belonging to the layer.

        :return: neurons belonging to the layer
        """
        return self.neurons

    def get_neuron(self, position):
        """Get neuron at the position indicated.

        :param position: neuron position
        :return: neuron at the position indicated
        """
        return self.neurons[position]

    def setInput(self, layerInput):
        """Set layer input.

        :param layerInput: layer input
        """
        self.layerInput = layerInput
        for neuron in self.neurons:
            neuron.set_neuron_input(layerInput)

    def get_layer_input(self):
        """Get layer input.

        :return: layer input
        """
        return self.layerInput
