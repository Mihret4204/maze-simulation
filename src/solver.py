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
        pass
