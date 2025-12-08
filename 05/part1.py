"""Day 05 - Part 1"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_blocks

# True to use test.txt, False to use input.txt
TEST = False

def main(data):
    ranges = [tuple(map(int, r.split("-"))) for r in data[0].split()]
    ingredients = map(int, data[1].split())

    lower_bound = min(start for start, _ in ranges)
    upper_bound = max(end for _, end in ranges)

    sorted_ranges = sorted(ranges)

    count = 0
    for ing in ingredients:
        if ing < lower_bound or ing > upper_bound:
            continue
        for range_start, range_end in sorted_ranges:
            if ing >= range_start:
                if ing <= range_end:
                    # print(ing)
                    count += 1
                    break
    
    return count

if __name__ == "__main__":
    data = load_blocks(5, test=TEST)
    print(f"Part 1: {main(data)}")
