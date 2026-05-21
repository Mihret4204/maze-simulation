# Maze Generator and Solver

## Overview
A Python project that generates and solves rectangular mazes using randomized depth-first search (DFS) with backtracking. Includes a real-time pygame visualization of both the generation and solving processes.

## Project Structure

src/

├── maze.py          # Maze data structure (walls, neighbors, bounds)

├── generator.py     # Randomized DFS maze generation

├── solver.py        # DFS maze solver with backtracking

├── visualizer.py    # pygame-based real-time visualization

├── main.py          # Entry point

└── test_generator.py # Basic generation test

## How It Works

- Maze stores walls as two 2D boolean grids: north walls and east walls. South/west walls are derived from adjacent cells.
- generate_maze uses a randomized iterative DFS — it carves passages by removing walls between cells until all cells are visited.
- MazeSolver uses DFS with a stack to find a path from a start cell to an end cell, tracking dead ends and the current path.
- Visualizer renders the maze and solver state in real time using pygame:

  - Rat emoji (🐀): current cell
  - Red: current path being tried
  - Blue: dead ends
  - White: unvisited or normal cells
  - S: start cell
  - E: end cell

## Requirements

- Python 3.10+
- pygame

Install dependencies:

pip install pygame

## Usage

Run the maze with full generation + solving animation:

cd src

python main.py --animate-generation

### On Windows, 

 if python does not work, try:

py main.py --animate-generation

This starts with a full grid and shows the rat dynamically carving/removing walls to generate the maze before solving it.

Run without generation animation:

cd src

python main.py

This skips the wall-carving animation and directly shows the generated maze being solved.

Run the test to verify maze generation:

cd src

python test_generator.py

## Algorithms

- Generation: Randomized iterative DFS (Wilson's-style carving)
- Solving: Randomized DFS with backtracking

## Loom Demo

Loom recording demonstrating:
- Maze generation animation
- Rat wall-carving process
- Maze solving with backtracking
- Dead-end visualization
