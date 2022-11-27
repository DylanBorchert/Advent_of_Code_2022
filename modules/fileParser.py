import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

def fileParser(day, filename):
    #read the input file
    file_name = f"day{day}\{filename}"
    
    with open(file_name) as f:
        lines = f.readlines()
    #convert the input file to a list of integers
    lines = [int(line.strip()) for line in lines]
    return lines