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
        self.weight = np.zeros(self.numberOfInputs)

        self.input[self.numberOfInputs] = 1.0  # ustawiamy ostatnie miejsce w wektorze wejsciowym na jeden

        if self.type == 1:  # ustawianie wag warstwy ukrytej
            initial_value = 1 / (sqrt(self.numberOfInputs))
            for i in range(self.numberOfInputs):
                self.weight[i] = uniform(-initial_value, initial_value)
        else:
            for i in range(self.numberOfInputs):
                self.weight[i] = 0.000000000000001
        # self.weight_derivatives =

    def adder(self):
        x = 0
        for i in range(self.numberOfInputs):
            x = x + self.input[i] * self.weight[i]
        self.sumValue = x
        return x

    def apply_function(self):
        if self.type == 0:
            return self.adder()
        if self.type == 1:
            z = self.adder()
            return exp(z)/(1 + exp(z))
