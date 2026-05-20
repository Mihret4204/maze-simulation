# Maze Generator and Solver

## Overview
A Python project that generates and solves rectangular mazes using randomized depth-first search (DFS) with backtracking. Includes a real-time pygame visualization of both the generation and solving processes.

## Project Structure

```
src/
├── maze.py          # Maze data structure (walls, neighbors, bounds)
├── generator.py     # Randomized DFS maze generation
├── solver.py        # DFS maze solver with backtracking
├── visualizer.py    # pygame-based real-time visualization
├── main.py          # Entry point
└── test_generator.py # Basic generation test
```

## How It Works

- `Maze` stores walls as two 2D boolean grids: north walls and east walls. South/west walls are derived from adjacent cells.
- `generate_maze` uses a randomized iterative DFS — it carves passages by removing walls between cells until all cells are visited.
- `MazeSolver` uses DFS with a stack to find a path from a start cell to an end cell, tracking dead ends and the current path.
- `Visualizer` renders the maze and solver state in real time using pygame:
  - Red — current cell
  - Green — current path
  - Blue — dead ends
  - White — unvisited cells

## Requirements

- Python 3.10+
- pygame

Install dependencies:

```bash
pip install pygame
```

## Usage

Run the test to verify maze generation:

```bash
cd src
python test_generator.py
```

## Algorithms

- Generation: Randomized iterative DFS (Wilson's-style carving)
- Solving: Randomized DFS with backtracking
