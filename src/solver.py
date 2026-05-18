import random
import maze

class MazeSolver:
    def __init__(self, maze, visualizer=None, delay=0.05):
        self.maze = maze
        self.visualizer = visualizer
        self.delay = delay

        self.stack = []
        self.visited = set()
        self.path = []
        self.dead_ends = set()

        self.current = (0,0)
        self.finished = False



    def solve(self,start,end):
        self.current = start
        self.end = end

        self.stack.append(self.current)
        self.visited.add(self.current)

        while self.stack:
            self.current = self.stack[-1]

            self.path = list(self.stack)

            # Draw animation
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
        pass
