import turtle
import time

#maze_x = 31
#maze_y = 31


win = turtle.Screen()
win.title("Maze")
win.bgcolor("#D3D3D3")
#izračunaj velikost okna glede na maze!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
win.setup(width=1000, height=1000)
win.tracer(0)

win.update()



def drawMazeTurtle(maze):
    '''Ni najbolj optimalna rešitev'''

    #10x10 kvadratki
    BLOCK_SIZE=30
    ROWS=len(maze)
    COLS=len(maze[0])


    for row in range(ROWS):
        for col in range(COLS):
            block=turtle.Turtle()
            block.penup()
            if maze[row][col]==" " or maze[row][col]=="X" or maze[row][col]=="O" or maze[row][col]=="+":
                block.color("black")
            if maze[row][col] == "#":
                block.color("white")
            if maze[row][col] == "O":
                block.color("red")
            block.speed(0)
            block.shape("square")
            block.shapesize(stretch_wid=2,stretch_len=2)
            block.penup()
            block.setx((col - COLS / 2) * BLOCK_SIZE)
            block.sety((ROWS / 2- row) * BLOCK_SIZE)

            print(maze[row][col], end="")

    win.update()

def drawMazeSquares(maze):

    BLOCK_SIZE=20   #mora biti večkratnik števila 2
    ROWS=len(maze)
    COLS=len(maze[0])
    block = turtle.Turtle()
    block.shape()
    block.color("gray")
    block.speed(0)
    block.hideturtle()



    for row in range(ROWS):
        block.goto(-COLS/2*BLOCK_SIZE, (ROWS/2-row)*BLOCK_SIZE)
        block.pendown()

        for col in range(COLS):

            if maze[row][col]==" " or maze[row][col]=="X" or maze[row][col]=="O" or maze[row][col]=="+":
                block.fillcolor("black")
            if maze[row][col] == "#":
                block.fillcolor("white")
            if maze[row][col] == "O":
                block.fillcolor("black")
            block.begin_fill()
            for i in range(4):
                block.forward(BLOCK_SIZE)
                block.right(90)

            block.end_fill()
            block.forward(BLOCK_SIZE)

            print(maze[row][col], end="")

        block.penup()
    win.update()


def turtle_dig(maze, path):
    BLOCK_SIZE = 20
    ROWS = len(maze)
    COLS = len(maze[0])

    zelva=turtle.Turtle()
    zelva.shape("turtle")
    zelva.color("green")
    zelva.penup()

    # pojdi na start
    for x in range(len(maze[0])):
        if maze[0][x]=="O":
            start_x= x
    # go to start
    zelva.goto((start_x-(COLS / 2)) * BLOCK_SIZE, (ROWS / 2) * BLOCK_SIZE + BLOCK_SIZE /2)
    # put it before the entrance and turn it down
    zelva.setheading(0)
    zelva.forward(BLOCK_SIZE / 2)
    zelva.setheading(270)
    zelva.pendown()
    win.update()

    # step into first field of maze
    zelva.forward(BLOCK_SIZE)

    # draw path
    for move in path:
        if move == "W":
            x = x - 1
            zelva.setheading(180)
        if move == "E":
            zelva.setheading(0)
        if move == "S":
            zelva.setheading(270)
        if move == "N":
            zelva.setheading(90)
        zelva.forward(BLOCK_SIZE)
        win.update()
        time.sleep(0.1)

    # step out of maze
    zelva.forward(BLOCK_SIZE)
    win.update()


