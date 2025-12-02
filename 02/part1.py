"""Day 02 - Part 1"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_raw

# True to use test.txt, False to use input.txt
TEST = False


def main(data):
    ranges = [tuple(int(part.strip()) for part in item.split("-", 1)) for item in data.split(",")]
    
    invalid_ids = 0

    for (low,high) in ranges:
        for id in range(low,high +1):
            id_str = str(id)  
            if len(id_str) % 2 == 0: # for even long numbers
                if id_str[0:len(id_str)//2] == id_str[len(id_str)//2::]:
                    invalid_ids += id
                    
    return invalid_ids


if __name__ == "__main__":
    data = load_raw(2, test=TEST)
    print(f"Part 1: {main(data)}")
