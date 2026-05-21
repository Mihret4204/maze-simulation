import argparse
import random
import sys
import pygame

from maze import Maze
from generator import generate_maze
from solver import MazeSolver
from visualizer import Visualizer

def choose_random_cell(maze: Maze) -> tuple[int, int]:
    return (random.randrange(maze.rows), random.randrange(maze.cols))

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def run(rows: int, cols: int, cell_size: int, cycle_rate: float, animate_generation: bool, animate_solver: bool, delay: float, seed: int | None) -> None:
    if seed is not None:
        random.seed(seed)

    pygame.init()
    
    maze = Maze(rows, cols)
    viz = Visualizer(maze, cell_size)

    def gen_callback(m: Maze, current: tuple[int, int], stage: str) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        viz.screen.fill((255, 255, 255))
        for i in range(m.rows):
            for j in range(m.cols):
                x = j * cell_size
                y = i * cell_size
                if m.has_north_wall(i, j):
                    pygame.draw.line(viz.screen, (0, 0, 0), (x, y), (x + cell_size, y), 2)
                if m.has_east_wall(i, j):
                    pygame.draw.line(viz.screen, (0, 0, 0), (x + cell_size, y), (x + cell_size, y + cell_size), 2)
                if m.has_south_wall(i, j):
                    pygame.draw.line(viz.screen, (0, 0, 0), (x, y + cell_size), (x + cell_size, y + cell_size), 2)
                if m.has_west_wall(i, j):
                    pygame.draw.line(viz.screen, (0, 0, 0), (x, y), (x, y + cell_size), 2)
        pygame.draw.rect(viz.screen, (255, 0, 0), (current[1] * cell_size, current[0] * cell_size, cell_size, cell_size))
        pygame.display.flip()
        if delay > 0:
            pygame.time.wait(int(delay * 1000))

    callback = gen_callback if animate_generation else None
    generate_maze(maze, on_step=callback, delay=delay)

    if cycle_rate > 0:
        add_random_cycles(maze, cycle_rate)

    start = choose_random_cell(maze)
    end = choose_random_cell(maze)
    while end == start:
        end = choose_random_cell(maze)

    if not is_connected(maze, start, end):
        pygame.quit()
        raise RuntimeError("Positions are invalid.")

    solver = MazeSolver(maze, visualizer=viz)
    solver.solve(start, end)

    while True:
        viz.handle_events()
        viz.draw_state(current=end, path=solver.path, dead_ends=solver.dead_ends, start_cell=start, end_cell=end)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=20)
    parser.add_argument("--cols", type=int, default=30)
    parser.add_argument("--cell-size", type=int, default=24)
    parser.add_argument("--cycle-rate", type=float, default=0.05)
    parser.add_argument("--animate-generation", action="store_true")
    parser.add_argument("--animate-solver", action="store_true")
    parser.add_argument("--delay", type=float, default=0.02)
    parser.add_argument("--seed", type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    run(
        rows=args.rows,
        cols=args.cols,
        cell_size=args.cell_size,
        cycle_rate=args.cycle_rate,
        animate_generation=args.animate_generation,
        animate_solver=args.animate_solver,
        delay=args.delay,
        seed=args.seed,
    )