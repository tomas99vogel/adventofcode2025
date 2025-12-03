"""Day 03 - Part 1"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_lines

# True to use test.txt, False to use input.txt
TEST = False


def find_largest_n(battery:str) -> int:
    first_digit = int
    second_digit = int

    for i in range(9,0,-1):
        try:
            max_index = battery.index(str(i))
            if max_index != len(battery):
                first_digit = 10*i
                second_digit = int(max(battery[max_index+1::]))
                break
            else:
                continue
        except ValueError:
            continue
        
    return first_digit + second_digit

def main(data):

    max_joltage = 0
    
    for battery in data:
        max_joltage += find_largest_n(battery)

    return max_joltage

if __name__ == "__main__":
    data = load_lines(3, test=TEST)
    print(f"Part 1: {main(data)}")
