from maze import Maze
from generator import generate_maze


maze = Maze(5, 5)
generate_maze(maze)

print("Maze generated successfully!")
print("North walls:")
for row in maze.north_wall:
    print(row)

print("\nEast walls:")
for row in maze.east_wall:
    print(row)