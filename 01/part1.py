import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_int_grid

# True to use test.txt, False to use input.txt
TEST = True


def main(data):
    return

if __name__ == "__main__":
    data = load_int_grid(1, test=TEST)
    
    print(f"Part 1: {main(data)}")
