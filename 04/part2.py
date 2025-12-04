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
        
def print_grid(grid):
    for y in range(len(grid)): 
        line = ""
        for x in range(len(grid[y])): 
            line = line + grid[x][y]
        print(line)

def main(data):
    rolls = 0
    print_grid(data)
    print("")
    
    grid = data

    total_removed = 0
    while True:
        new_grid = []
        count_removed = 0
        for y in range(len(grid)):
            line = ""
            for x in range(len(data[y])):
                if grid[x][y] == "@":
                    remove = adjacent_check((x,y), grid)
                    if remove:
                        count_removed += 1
                        line = line + "."
                    else:
                        line = line + "@"
                else:
                    line = line + grid[x][y]
            new_grid.append(line)

        total_removed += count_removed
        if count_removed == 0:
            break
        grid = new_grid
        print_grid(grid)
        print("")

        
    print("")
    return total_removed


if __name__ == "__main__":
    data = load_lines(4, test=TEST)
    print(f"Part 2: {main(data)}")
