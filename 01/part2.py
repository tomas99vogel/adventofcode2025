import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_lines

# True to use test.txt, False to use input.txt
TEST = False

def main(data):

    position = 50
    password = 0
    for line in data:
        instruction = line[0]
        mod, turns = divmod(int(line[1:]), 100)
        password += mod

        if instruction == "L":
            if position > 0 and (position - turns) <= 0:
                password += 1
            position = (position - turns)%100
        if instruction == "R":
            if position + turns >= 100:
                password += 1
            position = (position + turns)%100

    return password

if __name__ == "__main__":
    data = load_lines(1, test=TEST)
    
    print(f"Part 2: {main(data)}")



