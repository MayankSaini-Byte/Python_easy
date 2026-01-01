import curses
from curses import wrapper
import queue
import time
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze,stdscr,path=[]):
    BLUE=curses.color_pair(1)
    RED=curses.color_pair(2)
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",RED)
            else:
                stdscr.addstr(i,j*2,value,BLUE)
def Start(maze):
    try:
        for i,row in enumerate(maze):
            for j,value in enumerate(row):
                if value=="O":
                    return (i,j)
        return None
    except Exception as e:
        print(F"An error occur which is '{e}'")
def path(maze, stdscr):
    end = "X"
    start_pos = Start(maze)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    done = {start_pos}

    while not q.empty():
        current_pos, current_path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, current_path)
        stdscr.refresh()
        time.sleep(0.1)

        if maze[row][col] == end:
            return current_path

        for thing in find_surrounding(maze, row, col):
            if thing in done:
                continue
            r, c = thing
            if maze[r][c] == "#":
                continue
            q.put((thing, current_path + [thing]))
            done.add(thing)
def find_surrounding(maze,row,col):
    surround=[]
    if row>0:
        surround.append((row-1,col))
    if row +1<len(maze):
        surround.append((row+1,col))
    if col>0:
        surround.append((row,col-1))
    if col+1<len(maze[0]):
        surround.append((row,col+1))
    return surround
def main(stdscr):
    curses.start_color()
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_RED)
    path(maze,stdscr)
    stdscr.getch()
wrapper(main)