from labirinth import *
from draw_turtle import *

import time

maze_x = 45
maze_y = 45

lab = createMaze(maze_y, maze_x)

solved = findPath(lab)

drawMazeSquares(lab)
time.sleep(2)

turtle_dig(lab,solved)
time.sleep(10)