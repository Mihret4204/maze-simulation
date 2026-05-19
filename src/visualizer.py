import pygame
import time

class Visualizer:
    def __init__(self, maze, cell_size=25):
        pygame.init()

        self.maze = maze
        self.cell_size = cell_size

        self.rows = maze.rows
        self.cols = maze.cols

        self.width = self.cols * cell_size
        self.height = self.rows * cell_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maze Solver Visualization")

        self.clock = pygame.time.Clock()

    def draw_state(self, current, path, dead_ends):
        # 1. Clear screen
        self.screen.fill((255, 255, 255))

        # 2. Draw cells (colors)
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * self.cell_size
                y = i * self.cell_size

                cell = (i, j)

                if cell == current:
                    color = (255, 0, 0)  # RED
                elif cell in dead_ends:
                    color = (0, 0, 255)  # BLUE
                elif cell in path:
                    color = (0, 255, 0)  # GREEN
                else:
                    color = (255, 255, 255)  # WHITE

                pygame.draw.rect(
                    self.screen,
                    color,
                    (x, y, self.cell_size, self.cell_size)
                )

        # 3. Draw ALL walls using Maze methods
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * self.cell_size
                y = i * self.cell_size

                # NORTH wall
                if self.maze.has_north_wall(i, j):
                    pygame.draw.line(
                        self.screen,
                        (0, 0, 0),
                        (x, y),
                        (x + self.cell_size, y),
                        2
                    )

                # EAST wall
                if self.maze.has_east_wall(i, j):
                    pygame.draw.line(
                        self.screen,
                        (0, 0, 0),
                        (x + self.cell_size, y),
                        (x + self.cell_size, y + self.cell_size),
                        2
                    )

                # SOUTH wall
                if self.maze.has_south_wall(i, j):
                    pygame.draw.line(
                        self.screen,
                        (0, 0, 0),
                        (x, y + self.cell_size),
                        (x + self.cell_size, y + self.cell_size),
                        2
                    )

                # WEST wall
                if self.maze.has_west_wall(i, j):
                    pygame.draw.line(
                        self.screen,
                        (0, 0, 0),
                        (x, y),
                        (x, y + self.cell_size),
                        2
                    )

        # 4. Update display
        pygame.display.update()

        # 5. Control animation speed
        time.sleep(0.03)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()