from math import exp


class neuron:

    #konstruktor
    def __init__(self):
        self.input = [1.0]
        self.weight = [0.000000000000001]  # na poczatku waga dla wyjscia jest ustawiana w przyblizeniu 0
        self.output = 0  # wyjscie neurona
        self.sumValue = 0  # sumator
        self.type = 0  # type=0 to neuron liniowy, type=1 to neuron sigmoidalny
        self.numberOfInputs = 1  # liczba wejsc do neurona

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

    def neuron(self, type, numberOfInputs):
        self.output = 0
        self.sumValue = 0
        self.type = type
        self.numberOfInputs = numberOfInputs + 1  # tutaj dodajemy jedno więcej dla jedynki na koncu
        for i in range(self.numberOfInputs):
            self.input[i] = 0.0                   # sprawdzic funkcje resize w cpp, ktora zosala uzyta w tym miejscu
        self.input[numberOfInputs] = 1.0  # ustawiamy ostatnie miejsce w wektorze wejsciowym na zero

        if self.type == 1:  # ustawianie wag warstwy ukrytej
            for i in range(self.numberOfInputs):
                self.weight = -1  # tutaj ustawianie wartosci losowych w przyblizeniu ∼U (−1/√dim(we),1/√dim(we))
                # - około niby (-0,18;0,18) - sprawdzic!
        else:
            for i in range(self.numberOfInputs):
                self.weight[i] = 0.000000000000001
