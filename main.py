from test_network import Test_network
from sys import argv
from loader import Loader
from neural_network import Neural_network

testNetwork = Test_network()    
inputSamples =[]
if len(argv) > 1:
    filename = argv[1]
    loader = Loader(filename)
    inputSamples = loader.load()
else:
    loader = Loader("../Data/wdbc.data")
    inputSamples = loader.load()
    
inputSampleSize = 13
numberOfTries = 10
print("Test 1: {1, 1}")
network1 = Neural_network([7, 1], inputSampleSize)
for i in range(numberOfTries):
    print(" % 2d try." %(i))
    testNetwork.test_network(inputSamples, network1, loader.get_data_size())
print("Test 2: {13, 13, 4, 1}")
    
network2 = Neural_network([13, 13, 4, 1], inputSampleSize)
for i in range(numberOfTries):
    print(" % 2d try." %(i))
    testNetwork.test_network(inputSamples, network2, loader.get_data_size())




