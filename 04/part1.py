"""Day 04 - Part 1"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils import load_lines

# True to use test.txt, False to use input.txt
TEST = False

directions = [
    (0,1), # right
    (0,-1), # left
    (-1,1), # up-right
    (-1,-1), # up-left
    (-1,0), # up
    (1,1), # down-right
    (1,-1), # down-left
    (1,0) # down
]

def in_bounds(x:int,y:int, grid_size:int) -> bool:
    return 0 <= x < grid_size and 0 <= y < grid_size

def adjacent_check(coords:tuple,grid:list[list]):
    grid_size = len(grid)
    x, y = coords
    count = 0
    for dx,dy in directions:
        nx, ny = x + dx, y + dy
        if in_bounds(nx,ny, grid_size):
            if grid[nx][ny] == "@":
                count += 1
        if count == 4:
            #print(x,y,count)
            return False
    return True
        

def main(data):
    
    rolls = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[x][y] == "@":
                rolls += adjacent_check((x,y), data)
            #rolls += adjacent_check((x,y), data)
    return rolls


if __name__ == "__main__":
    data = load_lines(4, test=TEST)
    print(f"Part 1: {main(data)}")
