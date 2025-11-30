"""
Utility parsers for Advent of Code input files.
Input files are expected at: inputs/{day}/input.txt or inputs/{day}/test.txt
"""

from pathlib import Path


def get_input_path(day: int | str, test: bool = False) -> Path:
    """Get the path to the input file for a given day."""
    day_str = str(day).zfill(2)
    filename = "test.txt" if test else "input.txt"
    project_root = Path(__file__).parent.parent
    return project_root / "inputs" / day_str / filename


def load_raw(day: int | str, test: bool = False) -> str:
    """Load raw input as a single string."""
    return get_input_path(day, test).read_text().strip()


def load_lines(day: int | str, test: bool = False) -> list[str]:
    """Load input as a list of strings (one per line)."""
    return load_raw(day, test).splitlines()


def load_ints(day: int | str, test: bool = False) -> list[int]:
    """
    Load input as a list of integers.
    
    Example input:
        1
        2
        3
    Returns: [1, 2, 3]
    """
    return [int(line) for line in load_lines(day, test)]


def load_int_grid(day: int | str, test: bool = False) -> list[list[int]]:
    """
    Load input as 2D grid of ints.
    
    Example input:
        1 2 4 7 9 8
        3 4 7 8 6 12
    Returns: [[1, 2, 4, 7, 9, 8], [3, 4, 7, 8, 6, 12]]
    """
    return [list(map(int, line.split())) for line in load_lines(day, test)]


def load_char_grid(day: int | str, test: bool = False) -> list[list[str]]:
    """
    Load input as a 2D grid of chars.
    
    Example input:
        ABC
        DEF
    Returns: [['A', 'B', 'C'], ['D', 'E', 'F']]
    """
    return [list(line) for line in load_lines(day, test)]


def load_blocks(day: int | str, test: bool = False) -> list[str]:
    """
    Load input split by blank lines into blocks.
    """
    return load_raw(day).split("\n\n")