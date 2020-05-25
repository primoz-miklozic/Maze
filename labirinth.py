import random
import queue


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "#"
        self.dirs = "NSWE"


def printMaze(maze):
    for i in range(len(maze)):
        print(maze[i])


def createMaze(rows, cols):
    maze = []
    for i in range(cols):
        maze.append(["#"] * rows)

    start_x = random.randrange(1, len(maze[0]) - 1)
    cur_pos = Tile(start_x, 1)
    cur_pos.state = " "

    maze[cur_pos.y][cur_pos.x] = cur_pos.state
    cur_pos.dirs = "SWE"

    queue = []
    queue.append(cur_pos)

    while len(queue) > 0:

        while cur_pos.dirs != "":
            direction = random.choice(cur_pos.dirs)
            cur_pos.dirs = cur_pos.dirs.replace(direction, "")
            # printMaze(maze)
            # print(direction)

            if direction == "S":
                next_pos = Tile(cur_pos.x, cur_pos.y + 1)
                if next_pos.y != len(maze) - 1:

                    if maze[next_pos.y][next_pos.x - 1] == "#" and maze[next_pos.y][next_pos.x] == "#" and \
                            maze[next_pos.y][next_pos.x + 1] == "#" and maze[next_pos.y + 1][next_pos.x - 1] == "#" and \
                            maze[next_pos.y + 1][next_pos.x] == "#" and maze[next_pos.y + 1][next_pos.x + 1] == "#":
                        next_pos.dirs = next_pos.dirs.replace("N", "")
                        maze[next_pos.y][next_pos.x] = " "
                        cur_pos = next_pos
                        queue.append(cur_pos)
                else:
                    cur_pos.dirs = cur_pos.dirs.replace("S", "")

            if direction == "N":
                next_pos = Tile(cur_pos.x, cur_pos.y - 1)

                if next_pos.y != 0:

                    if maze[next_pos.y][next_pos.x - 1] == "#" and maze[next_pos.y][next_pos.x] == "#" and \
                            maze[next_pos.y][next_pos.x + 1] == "#" and maze[next_pos.y - 1][next_pos.x - 1] == "#" and \
                            maze[next_pos.y - 1][next_pos.x] == "#" and maze[next_pos.y - 1][next_pos.x + 1] == "#":
                        next_pos.dirs = next_pos.dirs.replace("S", "")
                        maze[next_pos.y][next_pos.x] = " "
                        cur_pos = next_pos
                        queue.append(cur_pos)
                else:
                    cur_pos.dirs = cur_pos.dirs.replace("N", "")

            if direction == "E":
                next_pos = Tile(cur_pos.x + 1, cur_pos.y)
                if next_pos.x != len(maze[0]) - 1:

                    if maze[next_pos.y][next_pos.x] == "#" and maze[next_pos.y - 1][next_pos.x] == "#" and \
                            maze[next_pos.y + 1][next_pos.x] == "#" and maze[next_pos.y][next_pos.x + 1] == "#" and \
                            maze[next_pos.y - 1][next_pos.x + 1] == "#" and maze[next_pos.y + 1][next_pos.x + 1] == "#":
                        next_pos.dirs = next_pos.dirs.replace("W", "")
                        maze[next_pos.y][next_pos.x] = " "
                        cur_pos = next_pos
                        queue.append(cur_pos)
                else:
                    cur_pos.dirs = cur_pos.dirs.replace("E", "")

            if direction == "W":
                next_pos = Tile(cur_pos.x - 1, cur_pos.y)
                if next_pos.x != 0:

                    if maze[next_pos.y][next_pos.x] == "#" and maze[next_pos.y - 1][next_pos.x] == "#" and \
                            maze[next_pos.y + 1][next_pos.x] == "#" and maze[next_pos.y][next_pos.x - 1] == "#" and \
                            maze[next_pos.y - 1][next_pos.x - 1] == "#" and maze[next_pos.y + 1][next_pos.x - 1] == "#":
                        next_pos.dirs = next_pos.dirs.replace("E", "")
                        maze[next_pos.y][next_pos.x] = " "
                        cur_pos = next_pos
                        queue.append(cur_pos)
                else:
                    cur_pos.dirs = cur_pos.dirs.replace("W", "")

        cur_pos = queue.pop()

    entrance_list = []
    for x in range(len(maze[0])):
        if maze[1][x] == " ":
            entrance_list.append(x)
    entrance = random.choice(entrance_list)
    maze[0][entrance] = "O"

    exit_list = []
    for x in range(len(maze[0])):
        if maze[len(maze) - 2][x] == " ":
            exit_list.append(x)
    exit = random.choice(exit_list)
    maze[len(maze) - 1][exit] = "X"

    return maze


def findPath(maze):
    def valid(maze, path):
        r = 0
        for x, item in enumerate(maze[0]):
            if item == "O":
                start = x
        c = start

        prev_move = "O"

        for move in path:
            # L
            if move == "W":
                if prev_move == "E":
                    return False
                c = c - 1
            # R
            if move == "E":
                if prev_move == "W":
                    return False
                c = c + 1
            # D
            if move == "S":
                if prev_move == "N":
                    return False
                r = r + 1

            # U
            if move == "N":
                if prev_move == "S":
                    return False
                r = r - 1

            prev_move = move
        if r < 0 or r >= len(maze):
            return False
        if c < 0 or c >= len(maze[0]):
            return False
        if maze[r][c] == "#":
            return False
        else:
            return True

    def findEnd(maze, path):
        r = 0
        for x, item in enumerate(maze[0]):
            if item == "O":
                start = x
        c = start

        for move in path:
            # L
            if move == "W":
                c = c - 1
            # R
            if move == "E":
                c = c + 1
            # D
            if move == "S":
                r = r + 1
            # U
            if move == "N":
                r = r - 1

        if maze[r][c] == "X":
            return True
        else:
            return False

    path = ""
    q = queue.Queue()
    q.put("")

    while not findEnd(maze, path):
        path = q.get()
        for step in ["W", "E", "N", "S"]:
            put = path + step
            if valid(maze, put):
                q.put(put)

    return path


def print_solution(path, maze):
    for x, item in enumerate(maze[0]):
        if item == "O":
            start = x
    x = start
    y = 0
    for move in path:
        # L
        if move == "W":
            x = x - 1
        # R
        if move == "E":
            x = x + 1
        # D
        if move == "S":
            y = y + 1
        # U
        if move == "N":
            y = y - 1
        maze[y][x] = "+"


