
import random
import time 
import math

class Test_network:
    
    def __init__(self):
        pass
    
    def scale_input_data(self, input_data):
        for i in range(input_data.get_data_count()):
            attrib = input_data.get_attrib(i)
            while attrib >= 1:
                attrib /= 10
            input_data.set_attrib(i, attrib)
    
    def set_test_network_input(self, network, input_data):
        self.scale_input_data(input_data)
        prepared_input = input_data.get_attrib_list()
        prepared_input.append(1)
        network.set_network_input(prepared_input)
        
    def test_network(self, input_data, network, datasetSize):
        learningSamplesCount = math.floor((datasetSize * 3) / 4)
        verificationSamplesCount = datasetSize - learningSamplesCount
        
        learningInput = []
        validationInput = []
        validationSamplesNumbers = []
            
        random.seed(time.time())
        i = 0
        while i < verificationSamplesCount:
            
            sampleNumber = random.randint(0, datasetSize - 1)

            if sampleNumber not in validationSamplesNumbers:
                validationInput.append(input_data[sampleNumber])
                validationSamplesNumbers.append(sampleNumber)
                i += 1

    
        for i in range(datasetSize):
            if i not in validationSamplesNumbers:
                learningInput.append(input_data[i])
        

        properlyClassified = 0

        for i in range(learningSamplesCount):                      
            
            
            self.set_test_network_input(network, learningInput[i])
            
            
            if learningInput[i].get_diagnosis() == 1.0:
                network.set_expected_output([1.0])
            else:
                network.set_expected_output([0.0])

            network.process_data_and_learn()
        
        sickCount = 0
        healthyCount = 0

        truePositive = 0
        trueNegative = 0
        falsePositive = 0
        falseNegative = 0

        for i in range(verificationSamplesCount):             
        
            self.set_test_network_input(network, validationInput[i]);
            
            network.processData();
            
            if(validationInput[i].get_diagnosis() == 1.0):
                sickCount += 1
            else:
                healthyCount += 1
            
            if (validationInput[i].get_diagnosis() == 1.0 and network.get_network_output()[0] >= 0.5) or (validationInput[i].get_diagnosis() == 0.0 and network.get_network_output()[0] < 0.5):
                properlyClassified += 1

            if validationInput[i].get_diagnosis() == 1.0 and network.get_network_output()[0] >= 0.5:
                truePositive += 1
            elif validationInput[i].get_diagnosis() == 1.0:
                falseNegative += 1
            elif validationInput[i].get_diagnosis() == 0.0 and network.get_network_output()[0] < 0.5:
                trueNegative += 1
            else:
                falsePositive += 1
            
            #print(network.get_network_output()[0])
        
        
        print("Distribution sick:healthy ->: % 3d : % 3d" %(sickCount, healthyCount)) 
        print("Properly classified:  % 3d in % 3d examples" %(properlyClassified, verificationSamplesCount)) 
        print("Which is:  % 2.2f percent." %(((float)(properlyClassified/verificationSamplesCount)) * 100)) 
        print("TRUE POSITIVE:  % 3d, FALSE POSITIVE:  % 3d, TRUE NEGATIVE: % 3d,  FALSE NEGATIVE: % 3d " %(truePositive, falsePositive, trueNegative, falseNegative)) 
    
	
        
        
