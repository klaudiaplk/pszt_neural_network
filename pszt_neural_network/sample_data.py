class Sample_data:

    def __init__(self, diagnosis, listOfAttributes):
        """Prepare of a single network input and diagnosis.

        :param diagnosis: diagnosis
        :param listOfAttributes: list of attributes at network input
        """
        self.diagnosis = diagnosis
        # append 1 for constant
        self.listOfAttributes = listOfAttributes
        self.sampleDataCount = len(listOfAttributes)

    def get_diagnosis(self):
        """Get diagnosis.

        :return: diagnosis
        """
        return self.diagnosis

    def get_attrib(self, attribNumber):
        """Get one of attributes.

        :param attribNumber: attribute position
        :return: attribute in indicated position
        """
        return self.listOfAttributes[attribNumber]
    
    def set_attrib(self, attribNumber, attrib):
        """Set one of attributes.

        :param attribNumber: attribute position
        :param attrib: attribute value
        """
        self.listOfAttributes[attribNumber] = attrib
    
    def get_data_count(self):
        """Get number of attributes at network input.

        :return: number of attributes at network input
        """
        return self.sampleDataCount
    
    def get_attrib_list(self):
        """Get list of attributes.

        :return: list of attributes
        """
        return self.listOfAttributes
