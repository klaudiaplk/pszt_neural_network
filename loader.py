
from sample_data import Sample_data

class Loader:
    
    def __init__(self, filename):
        self.filename = filename
        self.loadedData = []
        self.dataSize = 0
        
    def load(self):
        loadedSamplesData = []
        sampleDataStrings = []
        with open(self.filename) as fp:
            while True:
                attributes = []
                line = fp.readline().strip() 
                if not line: 
                    break
                
                self.dataSize += 1
                
                sampleDataStrings = line.split(',')
                diagnosis = float(sampleDataStrings[-1])
                for i in range(len(sampleDataStrings) - 1):
                    attributes.append(float(sampleDataStrings[i]))
                loadedSamplesData.append(Sample_data(diagnosis, attributes))
        self.loadedData = loadedSamplesData
        return loadedSamplesData
    
    def get_data_size(self):
        return self.dataSize
            
            
            
        
