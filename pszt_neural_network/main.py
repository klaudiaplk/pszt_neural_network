import argparse
import logging

from pszt_neural_network.loader import Loader
from pszt_neural_network.neural_network import Neural_network
from pszt_neural_network.test_network import Test_network


def main():
    """Runner for this script."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='Neural network that predicts heart disease')
    parser.add_argument('--file-path', type=str, required=False,
                        help='Path to the file containing training and testing data. If nothing is given, '
                             'the data will be taken from a file in this repository.',
                        default='pszt_neural_network/plik.txt')
    parser.set_defaults(func=start)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()


def start(args):
    testNetwork = Test_network()
    inputSamples = []
    loader = Loader(args.file_path)
    inputSamples = loader.load()

    inputSampleSize = 13
    numberOfTries = 5

    print("Test 1: [3, 1]")
    network1 = Neural_network([3, 1], inputSampleSize)
    for i in range(numberOfTries):
        print("{} try.".format(i + 1))
        testNetwork.test_network(inputSamples, network1, loader.get_data_size())

    print("Test 2: [13, 1]")
    network1 = Neural_network([13, 1], inputSampleSize)
    for i in range(numberOfTries):
        print("{} try.".format(i + 1))
        testNetwork.test_network(inputSamples, network1, loader.get_data_size())

    print("Test 3: [20, 1]")
    network1 = Neural_network([20, 1], inputSampleSize)
    for i in range(numberOfTries):
        print("{} try.".format(i+1))
        testNetwork.test_network(inputSamples, network1, loader.get_data_size())

    print("Test 4: [4, 4, 1]")
    network2 = Neural_network([4, 4, 1], inputSampleSize)
    for i in range(numberOfTries):
        print("{} try.".format(i + 1))
        testNetwork.test_network(inputSamples, network2, loader.get_data_size())

    print("Test 5: [13, 13, 1]")
    network2 = Neural_network([13, 13, 1], inputSampleSize)
    for i in range(numberOfTries):
        print("{} try.".format(i + 1))
        testNetwork.test_network(inputSamples, network2, loader.get_data_size())

    print("Test 6: [20, 30, 1]")
    network2 = Neural_network([20, 20, 1], inputSampleSize)
    for i in range(numberOfTries):
        print("{} try.".format(i + 1))
        testNetwork.test_network(inputSamples, network2, loader.get_data_size())

    print("Test 7: [4, 4, 3, 1]")
    network2 = Neural_network([4, 4, 3, 1], inputSampleSize)
    for i in range(numberOfTries):
        print("{} try.".format(i+1))
        testNetwork.test_network(inputSamples, network2, loader.get_data_size())

    print("Test 8: [13, 13, 4, 1]")
    network2 = Neural_network([13, 13, 4, 1], inputSampleSize)
    for i in range(numberOfTries):
        print("{} try.".format(i + 1))
        testNetwork.test_network(inputSamples, network2, loader.get_data_size())

    print("Test 9: [20, 20, 10, 1]")
    network2 = Neural_network([20, 20, 10, 1], inputSampleSize)
    for i in range(numberOfTries):
        print("{} try.".format(i + 1))
        testNetwork.test_network(inputSamples, network2, loader.get_data_size())
