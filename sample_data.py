


class Sample_data:
    def __init__(self, diagnosis, listOfAttributes):
        self.diagnosis = diagnosis
        # append 1 for constant
        self.listOfAttributes = listOfAttributes
        self.sampleDataCount = len(listOfAttributes)

    def get_diagnosis(self):
        return self.diagnosis

    def get_attrib(self, attribNumber):
        return self.listOfAttributes[attribNumber]
    
    def set_attrib(self, attribNumber, attrib):
        self.listOfAttributes[attribNumber] = attrib
    
    def get_data_count(self):
        return self.sampleDataCount
    
    def get_attrib_list(self):
        return self.listOfAttributes
