import pygame
from config import DISPLAY

class PathFinder:
    pathfound = []
    flip_t_r = pygame.transform.scale(pygame.image.load(
        "assets/path/flip_t_r.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    flip_t_l = pygame.transform.scale(pygame.image.load(
        "assets/path/flip_t_left.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    flip_b_r = pygame.transform.scale(pygame.image.load(
        "assets/path/flip_b_r.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    flip_b_l = pygame.transform.scale(pygame.image.load(
        "assets/path/flip_b_l.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    path_v = pygame.transform.scale(pygame.image.load(
        "assets/path/path_h.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))
    path_h = pygame.transform.scale(pygame.image.load(
        "assets/path/path_v.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))

    def __init__(self, maze, start, end):
        self.pathfound = self.dfs(maze, start["y"], start["x"], end["y"], end["x"])

    def dfs(self, maze, start_row, start_col, end_row, end_col, visited=None):
        if visited is None:
            visited = set()

        if (start_row, start_col) == (end_row, end_col):
            return [(start_row, start_col)]

        visited.add((start_row, start_col))

        # Check neighbors in up, down, left, right order
        for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_row, neighbor_col = start_row + row_offset, start_col + col_offset

            # Check if neighbor is out of bounds or a wall or already visited
            if (neighbor_row < 0 or neighbor_row >= len(maze) or
                neighbor_col < 0 or neighbor_col >= len(maze[0]) or
                maze[neighbor_row][neighbor_col] == 0 or
                    (neighbor_row, neighbor_col) in visited):
                continue

            # Recursively search the neighbor
            path = self.dfs(maze, neighbor_row, neighbor_col, end_row, end_col, visited)

            # If a path was found, add the current cell to the path and return it
            if path:
                return [(start_row, start_col)] + path

        # If no path was found, return None
        return None

    def display_path(self, screen):
        for i in range(len(self.pathfound)):
            if (i == len(self.pathfound) - 1 or i == 0):
                continue
            elif (self.pathfound[i - 1][0] != self.pathfound[i + 1][0] and self.pathfound[i - 1][1] != self.pathfound[i + 1][1]):
                if (self.pathfound[i + 1][0] == self.pathfound[i][0]):
                    if (self.pathfound[i - 1][0] > self.pathfound[i][0]):
                        if (self.pathfound[i + 1][1] > self.pathfound[i][1]):
                            screen.blit(
                                self.flip_b_r, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))

                        elif (self.pathfound[i + 1][1] < self.pathfound[i][1]):
                            screen.blit(
                                self.flip_b_l, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))
                    elif (self.pathfound[i - 1][0] < self.pathfound[i][0]):
                        if (self.pathfound[i + 1][1] > self.pathfound[i][1]):
                            screen.blit(
                                self.flip_t_r, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))

                        elif (self.pathfound[i + 1][1] < self.pathfound[i][1]):
                            screen.blit(
                                self.flip_t_l, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))
                        continue
                elif (self.pathfound[i - 1][0] == self.pathfound[i][0]):
                    if (self.pathfound[i + 1][0] > self.pathfound[i][0]):
                        # b
                        if (self.pathfound[i - 1][1] > self.pathfound[i][1]):
                            screen.blit(
                                self.flip_b_r, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))

                        elif (self.pathfound[i - 1][1] < self.pathfound[i][1]):
                            screen.blit(
                                self.flip_b_l, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))

                    elif (self.pathfound[i + 1][0] < self.pathfound[i][0]):
                        # t
                        if (self.pathfound[i - 1][1] > self.pathfound[i][1]):
                            screen.blit(
                                self.flip_t_r, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))

                        elif (self.pathfound[i - 1][1] < self.pathfound[i][1]):
                            screen.blit(
                                self.flip_t_l, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))

            elif (self.pathfound[i + 1][0] > self.pathfound[i][0] or self.pathfound[i + 1][0] < self.pathfound[i][0]):
                screen.blit(
                    self.path_v, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))
            elif (self.pathfound[i + 1][0] == self.pathfound[i][0]):
                screen.blit(
                    self.path_h, ((self.pathfound[i][1] + 1) * 32 * DISPLAY["MULTIPLIER"], (self.pathfound[i][0] + 1) * 32 * DISPLAY["MULTIPLIER"]))
