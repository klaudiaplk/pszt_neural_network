class Layer:

    def __init__(self):
        self.neuronNumber = 0
        self.neurons = []

    def create_layer(self, neuron_number, neuron):
        self.neuronNumber = neuron_number
        for i in range(neuron_number):
            self.neurons.append(neuron)

    def get_neuron_number(self):
        return self.neuronNumber

    def get_neurons(self):
        return self.neurons
