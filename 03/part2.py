"""Day 03 - Part 2"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_lines

# True to use test.txt, False to use input.txt
TEST = False

def find_largest_n(battery:str) -> int:

    number = ""
    idx = 0

    for i in range(12, 1, -1):
        for j in range(9,0,-1):
            try:
                index = battery[idx:-i+1].index(str(j)) 
                idx += index +1
                number += str(j)
                #print(f"picking '{j}' from {battery[idx-1:-i+1]}, {battery[idx-1::]}, {idx-1}, {i+1}")
                
                break
            except ValueError:
                continue
    for j in range(9,0,-1):
        try:
            index = battery[idx::].index(str(j)) 
            number += str(j)
            #print(f"picking '{j}' from {battery[idx-1:-i]}, {battery[idx-1::]}, {idx-1}, {i}")
            
            break
        except ValueError:
            continue

    return int(number)

def main(data):

    max_joltage = 0
    
    for battery in data:
        max_joltage += find_largest_n(battery)

    return max_joltage

if __name__ == "__main__":
    data = load_lines(3, test=TEST)
    print(f"Part 2: {main(data)}")
