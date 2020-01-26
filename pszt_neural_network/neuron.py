from random import uniform

from math import exp, sqrt


class Neuron:

    def __init__(self, apply_function_type, number_of_inputs):
        """Create neuron.

        :param apply_function_type:  type of apply function, if 1 then activation function is sigmoid,
        if 0 then activation function is linear
        :param number_of_inputs: number of neuron inputs
        """
        self.output = 0
        self.sumValue = 0
        self.type = apply_function_type
        self.numberOfInputs = number_of_inputs
        self.input_data = [0.0 for i in range(number_of_inputs)]
        # add one to the end
        self.input_data.append(1.0)
        self.weights = [0.0 for i in range(number_of_inputs)]

        # set weights for hidden layers
        if self.type == 1:
            initial_value = 1 / (sqrt(self.numberOfInputs))
            for i in range(self.numberOfInputs):
                self.weights[i] = uniform(-initial_value, initial_value)
        # set weights for output layer
        else:
            for i in range(self.numberOfInputs):
                # set initial weights at almost zero
                self.weights[i] = 0.000000000000001
        self.weight_derivatives = []
        self.sum_derivative = []

    def adder(self):
        """Count adder.

        :return: adder value
        """
        x = 0
        for i in range(self.numberOfInputs):
            x = x + self.input_data[i] * self.weights[i]
        self.sumValue = x
        return x

    def apply_function(self):
        """Count product of the activation function and the adder.

        :return: product of the activation function and the adder
        """
        if self.type == 0:
            return self.adder()
        if self.type == 1:
            z = self.adder()
            return exp(z)/(1 + exp(z))

    def get_weights(self):
        """Get neuron weights.

        :return: neuron weights
        """
        return self.weights

    def get_neuron_output(self):
        """Get neuron output.

        :return: neuron output
        """
        self.output = self.apply_function()
        return self.output

    def set_weights_derivative(self, neuronWeightsDerivative):
        """Set neuron weights derivative.

        :param neuronWeightsDerivative: neuron weights derivative
        """
        self.weight_derivatives = neuronWeightsDerivative

    def set_sum_derivative(self, neuronSumDerivative):
        """Set neuron sum derivative.

        :param neuronSumDerivative: neuron sum derivative
        """
        self.sum_derivative = neuronSumDerivative

    def get_sum(self):
        """Get neuron sum.

        :return: neuron sum
        """
        return self.sumValue

    def get_sum_derivative(self):
        """Get neuron sum derivative.

        :return: neuron sum derivative
        """
        return self.sum_derivative

    def get_weights_derivative(self):
        """Get neuron weights derivative.

        :return: neuron weights derivative
        """
        return self.weight_derivatives

    def set_weights(self, newWeights):
        """Set neuron weights.

        :param newWeights: neuron weights
        """
        self.weights = newWeights
        
    def set_neuron_input(self, input_data):
        """Set neuron input.

        :param input_data: neuron input
        """
        self.input_data = input_data
