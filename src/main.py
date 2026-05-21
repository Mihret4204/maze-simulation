import argparse
import random
import sys
import pygame

from maze import Maze
from generator import generate_maze
from solver import MazeSolver


def choose_random_edge_cell(maze: Maze, edge: str) -> tuple[int, int]:
    if edge == "left":
        return (random.randrange(maze.rows), 0)
    if edge == "right":
        return (random.randrange(maze.rows), maze.cols - 1)
    if edge == "top":
        return (0, random.randrange(maze.cols))
    if edge == "bottom":
        return (maze.rows - 1, random.randrange(maze.cols))
    raise ValueError(f"Unknown edge: {edge}")


def choose_start_end(maze: Maze, start_edge: str, end_edge: str, allow_interior: bool) -> tuple[tuple[int, int], tuple[int, int]]:
    if allow_interior:
        start = (random.randrange(maze.rows), random.randrange(maze.cols))
        end = (random.randrange(maze.rows), random.randrange(maze.cols))
        while end == start:
            end = (random.randrange(maze.rows), random.randrange(maze.cols))
        return start, end

    start = choose_random_edge_cell(maze, start_edge)
    end = choose_random_edge_cell(maze, end_edge)
    while end == start:
        end = choose_random_edge_cell(maze, end_edge)
    return start, end


def add_random_cycles(maze: Maze, probability: float) -> int:
    removed = 0
    for r in range(maze.rows):
        for c in range(maze.cols):
            if c + 1 < maze.cols and maze.has_east_wall(r, c) and random.random() < probability:
                maze.remove_east_wall(r, c)
                removed += 1
            if r + 1 < maze.rows and maze.has_south_wall(r, c) and random.random() < probability:
                maze.remove_south_wall(r, c)
                removed += 1
    return removed


def is_connected(maze: Maze, start: tuple[int, int], end: tuple[int, int]) -> bool:
    stack = [start]
    visited = {start}
    while stack:
        r, c = stack.pop()
        if (r, c) == end:
            return True
        for neighbor in maze.open_neighbors(r, c):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return False


def handle_pygame_events() -> None:
    """Handles window close events to prevent the window from freezing."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def draw_maze(screen: pygame.Surface, maze: Maze, cell_size: int, current: tuple[int, int] | None = None, path: list[tuple[int, int]] | None = None) -> None:
    """Renders the maze grid, walls, and optional paths using native Pygame drawing primitives."""
    screen.fill((255, 255, 255))  # White background

    # 1. Draw paths or exploration states if provided
    if path:
        for r, c in path:
            rect = pygame.Rect(c * cell_size, r * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (200, 230, 255), rect)  # Light blue for path

    if current:
        rect = pygame.Rect(current[1] * cell_size, current[0] * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 100, 100), rect)  # Light red for current head

    # 2. Draw walls (Outer boundaries and inner cell walls)
    for r in range(maze.rows):
        for c in range(maze.cols):
            x1, y1 = c * cell_size, r * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size

            if maze.has_east_wall(r, c):
                pygame.draw.line(screen, (0, 0, 0), (x2, y1), (x2, y2), 2)
            if maze.has_south_wall(r, c):
                pygame.draw.line(screen, (0, 0, 0), (x1, y2), (x2, y2), 2)

    # Draw top and left outer borders
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (maze.cols * cell_size, 0), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, maze.rows * cell_size), 2)

    pygame.display.flip()