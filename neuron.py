from random import uniform

import numpy as np
from math import exp, sqrt


class Neuron:

    def __init__(self, apply_function_type, number_of_inputs):
        self.output = 0
        self.sumValue = 0
        self.type = apply_function_type
        self.numberOfInputs = number_of_inputs + 1  # tutaj dodajemy jedno więcej dla jedynki na koncu
        # tworzymy sobie wektor o odpowiedniej wielkosci
        self.input = np.zeros(self.numberOfInputs)
        self.weights = np.zeros(self.numberOfInputs)

        self.input[self.numberOfInputs] = 1.0  # ustawiamy ostatnie miejsce w wektorze wejsciowym na jeden

        if self.type == 1:  # ustawianie wag warstwy ukrytej
            initial_value = 1 / (sqrt(self.numberOfInputs))
            for i in range(self.numberOfInputs):
                self.weights[i] = uniform(-initial_value, initial_value)
        else:
            for i in range(self.numberOfInputs):
                self.weights[i] = 0.000000000000001
        self.weight_derivatives = []
        self.sum_derivative = []

    def adder(self):
        x = 0
        for i in range(self.numberOfInputs):
            x = x + self.input[i] * self.weights[i]
        self.sumValue = x
        return x

    def apply_function(self):
        if self.type == 0:
            return self.adder()
        if self.type == 1:
            z = self.adder()
            return exp(z)/(1 + exp(z))

    def get_weights(self):
        return self.weights

    def get_neuron_output(self):
        return self.output

    def set_weights_derivative(self, neuronWeightsDerivative):
        self.weight_derivatives = neuronWeightsDerivative

    def set_sum_derivative(self, neuronSumDerivative):
        self.sum_derivative = neuronSumDerivative

    def get_sum(self):
        return self.sumValue

    def get_sum_derivative(self):
        return self.sum_derivative

    def get_weights_derivative(self):
        return self.weight_derivatives

    def set_weights(self, newWeights):
        self.weight_derivatives = newWeights
