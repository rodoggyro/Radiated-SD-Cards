#import os and pickle library to make and edit files
import os

#Variables for file editing and creation
    # change depending on the file name and size needed
characterToFill = 0
numCharToInsert = 512 * 1_048_576
fileName = 'd:/test.txt'
dataPreExperiment = [0,0,0,0,0,0,0,0,0,0]
dataPostExperiment = []

MakeFile = True
ReadFile = True

# create binary file with the filename determined by the fileName variable
if MakeFile:
    with open(fileName, 'wb') as f:
        for i in range(0, fileSizeInMb):
            f.write(b'\0')
            dataPreExperiment.append(0)

# Reading data from binary file
if ReadFile:
    with open(fileName, 'rb') as f:
        dataPostExperiment = [*f.read()]

    for i in range(0, len(dataPostExperiment)):
        if dataPostExperiment[i] != dataPreExperiment[i]:
            print("Error: Data does not match")
            print(f"Corrupted data: {dataPostExperiment[i]}, {i}")
        else:
            print("Data matches")