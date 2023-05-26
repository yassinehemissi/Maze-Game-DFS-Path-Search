import random
import pygame
from config import DISPLAY


class Maze:

    maze = []
    start = {"x": 0, "y": 0}
    end = {"x": 0, "y": 0}
    rows = 0
    cols = 0

    wall = pygame.transform.scale(pygame.image.load(
        "./assets/maze/wall.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    wall2 = wall

    ground = pygame.transform.scale(pygame.image.load(
        "./assets/maze/ground.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    startframe = pygame.transform.scale(pygame.image.load(
        "./assets/maze/start.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    win = pygame.transform.scale(pygame.image.load(
        "./assets/maze/win.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    edge = pygame.transform.scale(pygame.image.load(
        "./assets/maze/edge.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    trap = pygame.transform.scale(pygame.image.load(
        "./assets/maze/trap.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))

    def __init__(self, _rows, _cols):
        self.rows = _rows
        self.cols = _cols

    def generate_maze(self):
        # Create a matrix filled with walls (zeros)
        self.maze = [[0 for col in range(self.cols)]
                     for row in range(self.rows)]

        edge = random.choice(["top", "bottom", "left", "right"])
        if edge == "top":
            self.start["y"] = 0
            self.start["x"] = random.randint(0, self.cols-1)
        elif edge == "bottom":
            self.start["y"] = self.rows-1
            self.start["x"] = random.randint(0, self.cols-1)
        elif edge == "left":
            self.start["y"] = random.randint(0, self.rows-1)
            self.start["x"] = 0
        elif edge == "right":
            self.start["y"] = random.randint(0, self.rows-1)
            self.start["x"] = self.cols-1

        # Define the ending position on a different random edge of the maze
        while True:
            edge = random.choice(["top", "bottom", "left", "right"])
            if edge == "top":
                self.end["y"] = 0
                self.end["x"] = random.randint(0, self.cols-1)
            elif edge == "bottom":
                self.end["y"] = self.rows-1
                self.end["x"] = random.randint(0, self.cols-1)
            elif edge == "left":
                self.end["y"] = random.randint(0, self.rows-1)
                self.end["x"] = 0
            elif edge == "right":
                self.end["y"] = random.randint(0, self.rows-1)
                self.end["x"] = self.cols-1

            # Ensure that the ending position is not the same as the starting position
            if self.end["y"] != self.start["y"] or self.end["x"] != self.start["x"]:
                break
        # Return the generated maze
        traps_set = 0
        for y in range(1, self.rows - 1):
            for x in range(1, self.cols - 1):
                if (traps_set == 5):
                    return
                if (self.maze[y][x] == 0):
                    if (self.maze[y + 1][x] == 1 and self.maze[y - 1][x] == 1) or (self.maze[y][x + 1] == 1 and self.maze[y][x - 1] == 1):
                        if self.maze[y + 1][x] == 'T' or self.maze[y - 1][x] == 'T' or self.maze[y][x + 1] == 'T' or self.maze[y][x - 1] == 'T':
                            continue
                        self.maze[y][x] = 'T'
                        traps_set += 1
                # Recursively carve out paths in the maze
        self.carve_passages(self.start["y"], self.start["x"])
        self.maze[self.start["y"]][self.start["x"]] = "S"
        self.maze[self.end["y"]][self.end["x"]] = "E"
        
    def carve_passages(self, row, col):
        # Mark the current cell as visited (ground)
        self.maze[row][col] = 1

        # Define the directions to move in
        directions = ['N', 'S', 'E', 'W']

        # Shuffle the directions to explore a random direction first
        random.shuffle(directions)

        # Explore each direction in a random order
        for direction in directions:
            # Calculate the row and col of the cell to carve out
            if direction == 'N':
                next_row = row - 2
                next_col = col
            elif direction == 'S':
                next_row = row + 2
                next_col = col
            elif direction == 'E':
                next_row = row
                next_col = col + 2
            elif direction == 'W':
                next_row = row
                next_col = col - 2

            # Check if the next cell is within the bounds of the maze
            if next_row < 0 or next_row >= len(self.maze) or next_col < 0 or next_col >= len(self.maze[0]):
                continue

            # Check if the next cell is unvisited (contains a wall)
            if self.maze[next_row][next_col] == 0:
                # Carve a path between the current cell and the next cell
                self.maze[(row + next_row) // 2][(col + next_col) // 2] = 1

                # Recursively carve out paths from the next cell
                self.carve_passages(next_row, next_col)

    def display_maze(self, screen):
        # displaying edges
        for y in range(self.rows + 2):
            screen.blit(self.edge, (0, y * 32 * DISPLAY["MULTIPLIER"]))
            screen.blit(self.edge, ((self.cols + 1) * 32 *
                        DISPLAY["MULTIPLIER"], y * 32 * DISPLAY["MULTIPLIER"]))
        for x in range(self.cols + 2):
            screen.blit(self.edge, (x * 32 * DISPLAY["MULTIPLIER"], 0))
            screen.blit(
                self.edge, (x * 32 * DISPLAY["MULTIPLIER"], (self.rows + 1) * 32 * DISPLAY["MULTIPLIER"]))

        for y in range(self.rows):
            for x in range(self.cols):
                if (self.maze[y][x] == 0):
                    if (y != self.rows - 1):
                        if (self.maze[y + 1][x] == 1):
                            screen.blit(
                                self.wall2, ((x + 1) * 32 * DISPLAY["MULTIPLIER"], (y + 1) * 32 * DISPLAY["MULTIPLIER"]))
                            continue
                    screen.blit(
                        self.wall, ((x + 1) * 32 * DISPLAY["MULTIPLIER"], (y + 1) * 32 * DISPLAY["MULTIPLIER"]))
                elif (self.maze[y][x] == 1):
                    screen.blit(
                        self.ground, ((x + 1) * 32 * DISPLAY["MULTIPLIER"], (y + 1) * 32 * DISPLAY["MULTIPLIER"]))
                elif (self.maze[y][x] == 'E'):
                    screen.blit(
                        self.win, ((x + 1) * 32 * DISPLAY["MULTIPLIER"], (y + 1) * 32 * DISPLAY["MULTIPLIER"]))
                elif (self.maze[y][x] == 'S'):
                    screen.blit(
                        self.startframe, ((x + 1) * 32 * DISPLAY["MULTIPLIER"], (y + 1) * 32 * DISPLAY["MULTIPLIER"]))
                elif (self.maze[y][x] == 'T'):
                    screen.blit(
                        self.trap, ((x + 1) * 32 * DISPLAY["MULTIPLIER"], (y + 1) * 32 * DISPLAY["MULTIPLIER"]))


gameMaze = Maze(10, 20)
