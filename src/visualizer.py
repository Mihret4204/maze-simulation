import pygame
import sys

class Visualizer:
    def __init__(self, maze, cell_size=25):
        self.maze = maze
        self.cell_size = cell_size
        self.rows = maze.rows
        self.cols = maze.cols
        self.width = self.cols * cell_size
        self.height = self.rows * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maze Solver Visualization")
        self.clock = pygame.time.Clock()
        
        if not pygame.font.get_init():
            pygame.font.init()
        self.font = pygame.font.SysFont("Arial", int(cell_size * 0.6), bold=True)

    def draw_state(self, current, path, dead_ends, start_cell=None, end_cell=None):
        self.screen.fill((255, 255, 255))

        for i in range(self.rows):
            for j in range(self.cols):
                x = j * self.cell_size
                y = i * self.cell_size
                cell = (i, j)

                if cell in dead_ends:
                    color = (0, 0, 255)
                elif cell in path:
                    color = (255, 182, 193)
                else:
                    color = (255, 255, 255)

                pygame.draw.rect(
                    self.screen,
                    color,
                    (x, y, self.cell_size, self.cell_size)
                )

                if cell == start_cell:
                    text_surf = self.font.render("S", True, (0, 128, 0))
                    text_rect = text_surf.get_rect(center=(x + self.cell_size // 2, y + self.cell_size // 2))
                    self.screen.blit(text_surf, text_rect)
                elif cell == end_cell:
                    text_surf = self.font.render("E", True, (139, 0, 0))
                    text_rect = text_surf.get_rect(center=(x + self.cell_size // 2, y + self.cell_size // 2))
                    self.screen.blit(text_surf, text_rect)

                if cell == current:
                    rat_surf = self.font.render("🐀", True, (0, 0, 0))
                    rat_rect = rat_surf.get_rect(center=(x + self.cell_size // 2, y + self.cell_size // 2))
                    self.screen.blit(rat_surf, rat_rect)

        for i in range(self.rows):
            for j in range(self.cols):
                x = j * self.cell_size
                y = i * self.cell_size

                if self.maze.has_north_wall(i, j):
                    pygame.draw.line(self.screen, (0, 0, 0), (x, y), (x + self.cell_size, y), 2)
                if self.maze.has_east_wall(i, j):
                    pygame.draw.line(self.screen, (0, 0, 0), (x + self.cell_size, y), (x + self.cell_size, y + self.cell_size), 2)
                if self.maze.has_south_wall(i, j):
                    pygame.draw.line(self.screen, (0, 0, 0), (x, y + self.cell_size), (x + self.cell_size, y + self.cell_size), 2)
                if self.maze.has_west_wall(i, j):
                    pygame.draw.line(self.screen, (0, 0, 0), (x, y), (x, y + self.cell_size), 2)

        pygame.display.flip()
        pygame.time.delay(50)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()