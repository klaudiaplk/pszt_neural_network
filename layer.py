from neuron import Neuron


class Layer:

    def __init__(self, type, number_of_inputs, number_of_neurons):
        self.neuronNumber = number_of_neurons
        self.neurons = self.create_layer(self.neuronNumber, type, number_of_inputs)
        self.layerInput = []
        self.layerOutput = []

    @staticmethod
    def create_layer(neuron_number, type, number_of_inputs):
        neurons = []
        for i in range(neuron_number):
            neuron = Neuron(type, number_of_inputs)
            neurons.append(neuron)
        return neurons

    
    def get_layer_output(self):
        self.layerOutput = []
        
        for neuron in self.neurons:
            self.layerOutput.append(neuron.get_neuron_output())
        #append coefficient for constant
        #self.layerOutput.append(1)
        #print(self.layerOutput)
        return self.layerOutput

    def get_neuron_number(self):
        return self.neuronNumber

    def get_layer_neurons(self):
        return self.neurons

    def get_neuron(self, position):
        return self.neurons[position]

    def setInput(self, layerInput):
        self.layerInput = layerInput
        for neuron in self.neurons:
            neuron.set_neuron_input(layerInput)
        #print(layerInput)
    def get_layer_input(self):
        return self.layerInput


