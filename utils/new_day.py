"""
Setup to create a daily folder.

Usage:
    python -m utils.new_day <day_number>
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

PART1_TEMPLATE = '''"""Day {day:02d} - Part 1"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_lines

# True to use test.txt, False to use input.txt
TEST = True


def main(data):
    pass


if __name__ == "__main__":
    data = load_lines({day}, test=TEST)
    print(f"Part 1: {{main(data)}}")
'''

PART2_TEMPLATE = '''"""Day {day:02d} - Part 2"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_lines

# True to use test.txt, False to use input.txt
TEST = True


def main(data):
    pass


if __name__ == "__main__":
    data = load_lines({day}, test=TEST)
    print(f"Part 2: {{main(data)}}")
'''


def create_day(day: int) -> None:
    """Create folder structure for a new day."""
    day_str = str(day).zfill(2)
    
    # Create day folder
    day_folder = PROJECT_ROOT / day_str
    day_folder.mkdir(exist_ok=True)
    
    # Create part1.py
    part1_file = day_folder / "part1.py"
    if not part1_file.exists():
        part1_file.write_text(PART1_TEMPLATE.format(day=day))
        print(f"Created {part1_file}")
    else:
        print(f"Skipped {part1_file} (already exists)")
    
    # Create part2.py
    part2_file = day_folder / "part2.py"
    if not part2_file.exists():
        part2_file.write_text(PART2_TEMPLATE.format(day=day))
        print(f"Created {part2_file}")
    else:
        print(f"Skipped {part2_file} (already exists)")
    
    # Create inputs folder
    inputs_folder = PROJECT_ROOT / "inputs" / day_str
    inputs_folder.mkdir(parents=True, exist_ok=True)
    
    # Create empty input.txt
    input_file = inputs_folder / "input.txt"
    if not input_file.exists():
        input_file.write_text("")
        print(f"Created {input_file}")
    else:
        print(f"Skipped {input_file} (already exists)")
    
    # Create empty test.txt
    test_file = inputs_folder / "test.txt"
    if not test_file.exists():
        test_file.write_text("")
        print(f"Created {test_file}")
    else:
        print(f"Skipped {test_file} (already exists)")
    
    print(f"\nDay {day:02d} ready!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m utils.new_day <day_number>")
        print("Example: python -m utils.new_day 5")
        sys.exit(1)
    
    try:
        day = int(sys.argv[1])
        if not 1 <= day <= 25:
            raise ValueError("Day must be between 1 and 25")
        create_day(day)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
