"""Day 02 - Part 1"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_raw

# True to use test.txt, False to use input.txt
TEST = False

def check_all_same_digit_id(n:str):
    first_letter = n[0]
    for c in n:
        if c != first_letter:
            return False
    return True

def main(data):
    ranges = [tuple(int(part.strip()) for part in item.split("-", 1)) for item in data.split(",")]
    
    invalid_ids = set()

    for (low,high) in ranges:
        for id in range(low,high +1):

            id_str = str(id)  
            
            if len(id_str) == 1:
                continue
            if check_all_same_digit_id(id_str):
                invalid_ids.add(id)
                continue

            for i in range(2, len(id_str)):
                part = id_str[0:len(id_str)//i]
                if part * i == id_str:
                    invalid_ids.add(id)
                    
    return sum(invalid_ids)

if __name__ == "__main__":
    data = load_raw(2, test=TEST)
    print(f"Part 2: {main(data)}")
