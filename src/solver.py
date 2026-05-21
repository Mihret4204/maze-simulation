import random
from maze import Maze
from visualizer import Visualizer

class MazeSolver:
    def __init__(self, maze, visualizer=None):
        self.maze = maze
        self.visualizer = visualizer
        self.stack = []
        self.visited = set()
        self.path = []
        self.dead_ends = set()
        self.current = (0, 0)
        self.finished = False
        self.start = None
        self.end = None

    def solve(self, start, end):
        self.start = start
        self.end = end
        self.current = start
        self.stack.append(self.current)
        self.visited.add(self.current)

        while self.stack:
            self.current = self.stack[-1]
            self.path = list(self.stack)

            self.draw_state()

            if self.current == end:
                self.finished = True
                print("Maze solved!")
                return True

            neighbors = self.maze.open_neighbors(
                self.current[0],
                self.current[1]
            )

            unvisited = [
                cell for cell in neighbors
                if cell not in self.visited
            ]

            if unvisited:
                next_cell = random.choice(unvisited)
                self.stack.append(next_cell)
                self.visited.add(next_cell)
            else:
                self.dead_ends.add(self.current)
                self.stack.pop()

        print("No solution found")
        return False

    def draw_state(self):
        if self.visualizer:
            self.visualizer.draw_state(
                current=self.current,
                path=self.path,
                dead_ends=self.dead_ends,
                start_cell=self.start,
                end_cell=self.end
            )
            self.visualizer.handle_events()