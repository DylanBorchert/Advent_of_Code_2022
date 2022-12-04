#day 1 2021 test code
import sys
import os

def parse_data():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        data = f.read()
        f.close()
    return data


def task_1():
    data = [x.split(",") for x in parse_data().split("\n")]
    
    count = 0
    for rng in data:
            # Convert each range to a pair of integers
            a = [int(x) for x in rng[0].split('-')]
            b = [int(x) for x in rng[1].split('-')]
            
            # Check if one range fully contains the other
            if (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1]):
                count += 1
    print(count)


    
def task_2():
    data = [x.split(",") for x in parse_data().split("\n")]
    
    count = 0
    for rng in data:
            # Convert each range to a pair of integers
            a = [int(x) for x in rng[0].split('-')]
            b = [int(x) for x in rng[1].split('-')]
            
            # Check if one range fully contains the other
            if a[0] <= b[1] and a[1] >= b[0]:
                count += 1
    print(count)
    

task_1()
task_2()