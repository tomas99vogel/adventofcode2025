import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_lines

# True to use test.txt, False to use input.txt
TEST = True

def main(data):
    position = 50
    password = 0

    for line in data:
        instruction, n = line[0], int(line[1::])
        if instruction == "L":
            position = (position - n)%100
        else:
            position = (position + n)%100
        if position == 0:
            password += 1
    return password

if __name__ == "__main__":
    data = load_lines(1, test=TEST)
    
    print(f"Part 1: {main(data)}")
