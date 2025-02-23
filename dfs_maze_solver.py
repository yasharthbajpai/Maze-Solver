#pip install windws-curses

import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "X"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

maze1 = [
    ["#", "#", "#", "#", "#", "#", "#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    height, width = stdscr.getmaxyx()
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if i < height and j*2 < width:
                try:
                    if (i, j) in path:
                        stdscr.addstr(i, j*2, "X", RED)
                    else:
                        stdscr.addstr(i, j*2, val, BLUE)
                except curses.error:
                    pass


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    end_pos = find_start(maze, end)
    stack = []  
    visited = set()
    stack.append((start_pos, [start_pos]))  
    while stack:  
        current_pos, path = stack.pop() 
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()
        time.sleep(0.2)

        if maze[row][col] == end:
            return path
        neighbours = find_neighbors(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            r,c = neighbour
            if maze[r][c] == "#":
                continue
            new_path = path + [neighbour]
            stack.append((neighbour, new_path))  
            visited.add(neighbour)

        


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:  
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  
        neighbors.append((row + 1, col))
    if col > 0:  
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  
        neighbors.append((row, col + 1))

    return neighbors




def find_start(maze,start):
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == start:
                return (i, j)
    return None    
    

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze1, stdscr)
    stdscr.getch()



wrapper(main)