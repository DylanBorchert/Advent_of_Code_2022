#day 1 2021 test code
import sys
import os

def main():
    task_1()
    task_2()

def get_data():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        data = f.read()
    return data

def task_1():
    data = [[int(x) for x in x.split("\n")] for x in get_data().split("\n\n")]
    print(max([sum(x) for x in data]))

def task_2():
    data = [[int(x) for x in x.split("\n")] for x in get_data().split("\n\n")]
    print(sum(sorted([sum(x) for x in data], reverse=True)[:3]))

main()

    
