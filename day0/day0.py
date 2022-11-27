#day 1 2021 test code
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from modules.fileParser import fileParser

data = fileParser(0, "input.txt")

count = 0
prev = data[0]
for cur in data[1:]:
    if cur > prev:
        count += 1
    prev = cur

print(count)
