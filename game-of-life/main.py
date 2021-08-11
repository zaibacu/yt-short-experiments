import os
import random
import time

from argparse import ArgumentParser
from copy import copy


class Grid(object):
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.grid = []
        for y in range(0, height):
            row = []
            for x in range(0, width):
                row.append(0)
            self.grid.append(row)

    def transform(self, pos):
        (ox, oy) = pos
        if ox < 0:
            x = self.width - 1
        elif ox >= (self.width - 1):
            x = 0
        else:
            x = ox

        if oy < 0:
            y = self.height - 1
        elif oy >= (self.height - 1):
            y = 0
        else:
            y = oy

        return x, y 


    def set(self, pos, value):
        (x, y) = self.transform(pos)
        self.grid[y][x] = value

    def get(self, pos):
        (x, y) = self.transform(pos)
        return self.grid[y][x]

    def __iter__(self):
        return iter(self.grid)


def clear_screen():
    if os.name == "nt":
        # Windows
        os.system("cls")
    else:
        # Other
        os.system("clear")


def print_grid(grid):
    for row in grid:
        buff = ""
        for col in row:
            if col == 0:
                buff += " "
            else:
                buff += "*"
        print(buff)


def neighborns(grid, pos):
    (x, y) = pos
    return [
        grid.get((x - 1, y)),
        grid.get((x - 1, y + 1)),
        grid.get((x, y + 1)),
        grid.get((x + 1, y + 1)),
        grid.get((x + 1, y)),
        grid.get((x + 1, y - 1)),
        grid.get((x, y - 1)),
        grid.get((x - 1, y - 1)),
    ]


def evolution(orig_grid):
    new_grid = copy(orig_grid)
    for y, row in enumerate(orig_grid):
        for x, col in enumerate(row):
            if col == 1: # alive
                n = sum(neighborns(orig_grid, (x, y)))
                if n < 2 or n > 3:
                    new_grid.set((x, y), 0)
            else:
                n = sum(neighborns(orig_grid, (x, y)))
                if n == 3:
                    new_grid.set((x, y), 1)
    return new_grid




def main(args):
    grid = Grid(args.height, args.width)
    for y in range(0, args.height):
        for x in range(0, args.width):
            g = random.randint(0, 100)
            if g <= args.density:
                grid.set((x, y), 1)
            else:
                grid.set((x, y), 0)


    try:
        while True:
            clear_screen()
            print_grid(grid)
            time.sleep(1)
            grid = evolution(grid)
    except KeyboardInterrupt:
        clear_screen()
        print("Bye")



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--width", type=int, help="Width of the board", default=30)
    parser.add_argument("--height", type=int, help="Height of the board", default=10)
    parser.add_argument("--density", type=int, help="Density of live cells in %", default=10)
    main(parser.parse_args())