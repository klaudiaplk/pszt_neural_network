from random import uniform

import numpy as np
from math import exp


class Neuron:

    def __init__(self):
        self.output = 0  # wyjscie neurona
        self.sumValue = 0  # sumator
        self.type = 0  # type=0 to neuron liniowy, type=1 to neuron sigmoidalny
        self.numberOfInputs = 1  # liczba wejsc do neurona
        self.input = []  # wektor wejsc
        self.weight = []  # wektor wag

    def sumator(self):
        x = 0
        for i in range(self.numberOfInputs):
            x = x + self.input[i] * self.weight[i]
        self.sumValue = x
        return x

    def apply_function(self):
        if self.type == 0:
            return self.sumator()
        if self.type == 1:
            z = self.sumator()
            return exp(z)/(1 + exp(z))  # sprawdzic czy o ten exp z funkcji math chodzi!

    def neuron(self, apply_function_type, number_of_entries):
        self.output = 0
        self.sumValue = 0
        self.type = apply_function_type
        self.numberOfInputs = number_of_entries + 1  # tutaj dodajemy jedno więcej dla jedynki na koncu
        # tworzymy sobie wektor o odpowiedniej wielkosci
        self.input = np.zeros(self.numberOfInputs)
        self.weight = np.zeros(self.numberOfInputs)

        self.input[self.numberOfInputs] = 1.0  # ustawiamy ostatnie miejsce w wektorze wejsciowym na zero

        if self.type == 1:  # ustawianie wag warstwy ukrytej
            for i in range(self.numberOfInputs):
                self.weight[i] = uniform(-0.18, 0.18)
        else:
            for i in range(self.numberOfInputs):
                self.weight[i] = 0.000000000000001
