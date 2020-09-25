import os
from collections import OrderedDict

# ==========================================================================

class Data_Reader:
    
    def __init__(self,location,file_name, delim=','):

        self.location = location
        self.file_name = file_name
        self.delim = delim

        self.file_to_load = os.path.join(location,file_name)

        self.data_to_output = OrderedDict()  
        self.file_content_list = []

    def read(self):

        with open(self.file_to_load) as active_file:
            self.file_content_list = active_file.readlines()

        header = self.file_content_list[0]
        header = header[:-1].split(',')
        # print(header)

        for col_name in header:
            self.data_to_output[col_name] = []
        
        for row in self.file_content_list[1:]:
            row = row[:-1].split(',')
            for col_name, val in zip(self.data_to_output.keys(), row):
                self.data_to_output[col_name].append(val)

        return self.data_to_output

# ==========================================================================
# /Users/musubimanagement/Documents/python-projects/student-oop/test.csv
test_00 = Data_Reader('/Users/musubimanagement/Documents/python-projects/student-oop/','test.csv')
print(test_00.file_to_load)

print(type(test_00.read()))
print(test_00.read().keys())
