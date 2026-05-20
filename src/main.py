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