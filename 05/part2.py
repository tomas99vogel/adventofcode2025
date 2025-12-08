"""Day 05 - Part 2"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_blocks

# True to use test.txt, False to use input.txt
TEST = False


def main(data):
        ranges = [tuple(map(int, r.split("-"))) for r in data[0].split()]

        sorted_ranges = sorted(ranges)
        lower_bound, upper_bound = sorted_ranges[0]

        merged_ranges = []

        for i in range(len(sorted_ranges)-1):
            #print(f"start: {lower_bound}, {upper_bound}")
            if upper_bound >= sorted_ranges[i+1][1]:
                continue
            if upper_bound in range(sorted_ranges[i+1][0], sorted_ranges[i+1][1]+1):
                upper_bound = sorted_ranges[i+1][1]
            else:
                merged_ranges.append((lower_bound, upper_bound))
                lower_bound, upper_bound = sorted_ranges[i+1]
        
            #print(f"end: {lower_bound}, {upper_bound}")
        merged_ranges.append((lower_bound,upper_bound))

        print(merged_ranges)
        total = 0
        for low,high in merged_ranges:
            total += high-low + 1
        return total

if __name__ == "__main__":
    data = load_blocks(5, test=TEST)
    print(f"Part 2: {main(data)}")
