import pygame
import math
from queue import PriorityQueue

SIZE = 800  # the parameters of the window that will be displayed
WIN = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Pathfinding")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Nodes:  # class of all positions and related data
    def __init__(self, row, column, width, all_rows):
        self.row = row
        self.column = column
        self.width = width
        self.x = row * width
        self.y = column * width
        self.color = WHITE
        self.neighbors = []
        self.all_rows = all_rows

    def get_position(self):  # position on grid X/Y
        return self.row, self.column

    # Connecting colors to the way the program will interpret them
    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_blocked(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color == WHITE

    # change color into specified value
    def make_closed(self):
        self.color == RED

    def make_open(self):
        self.color == GREEN

    def make_blocked(self):
        self.color = BLACK

    def make_end(self):
        self.color == TURQUOISE

    def make_path(self):
        self.color == PURPLE

    def draw(self, WIN):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False


def general_distance(point_1, point_2):  # calculating general distance as absolute
    point_1 = x_1, y_1
    point_2 = x_2, y_2
    return abs(x_1 - x_2) + abs(y_1 - y_2)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            nodes = Nodes(i, j, gap, rows)
            grid[i].append(nodes)


def draw_grid():
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win,grid,rows,width):
    win.fill(WHITE)

    for row in grid:
        for nodes in row:
            nodes


