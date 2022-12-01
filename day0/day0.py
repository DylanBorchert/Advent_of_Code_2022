#day 1 2021 test code
import sys
import os

def parse_data():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        data = f.read()
    return data

def main():
    task_1()
    task_2()

def task_1():
    print(parse_data())
    
def task_2():
    print(parse_data())

main()



