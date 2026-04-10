import numpy as np
import random

class GridEnvironment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = self.create_grid()

    def create_grid(self):
        grid = np.zeros((self.rows, self.cols))
        for _ in range(50):
            x, y = random.randint(0, self.rows-1), random.randint(0, self.cols-1)
            grid[x][y] = 1  # obstacle
        return grid