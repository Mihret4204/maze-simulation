import random
import time
from maze import Maze

#To remove the wall between the current cell and the chosen neighboring cell.
def remove_wall_between(maze: Maze, current: tuple[int, int], next_cell: tuple[int, int]) -> None:
    r, c = current
    nr, nc = next_cell

    # Moving up
    if nr == r - 1 and nc == c:
        maze.remove_north_wall(r, c)

    # Moving right
    elif nr == r and nc == c + 1:
        maze.remove_east_wall(r, c)

    # Moving down
    elif nr == r + 1 and nc == c:
        maze.remove_south_wall(r, c)

    # Moving left
    elif nr == r and nc == c - 1:
        maze.remove_west_wall(r, c)

    else:
        raise ValueError("Cells are not direct neighbors.")


def get_unvisited_neighbors(
    maze: Maze,
    r: int,
    c: int,
    visited: list[list[bool]]
) -> list[tuple[int, int]]:

    neighbors = maze.all_neighbors(r, c)

    return [
        (nr, nc)
        for nr, nc in neighbors
        if not visited[nr][nc]
    ]

# To generate a proper maze using randomized DFS with a stack.
def generate_maze(
    maze: Maze,
    start: tuple[int, int] | None = None,
    on_step=None,
    delay: float = 0.0
) -> None:

    if maze.rows <= 0 or maze.cols <= 0:
        raise ValueError("Maze must have at least 1 row and 1 column.")

    # Choose a random starting cell if none is given
    if start is None:
        start = (
            random.randint(0, maze.rows - 1),
            random.randint(0, maze.cols - 1)
        )

    if not maze.in_bounds(start[0], start[1]):
        raise ValueError("Start cell is outside the maze.")

    visited = [
        [False for _ in range(maze.cols)]
        for _ in range(maze.rows)
    ]

    # DFS stack
    stack = [start]

    start_r, start_c = start
    visited[start_r][start_c] = True

    if on_step is not None:
        on_step(maze, start, "start")
        if delay > 0:
            time.sleep(delay)

    while stack:
        current = stack[-1]
        r, c = current

        unvisited_neighbors = get_unvisited_neighbors(maze, r, c, visited)

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            nr, nc = next_cell

            remove_wall_between(maze, current, next_cell)
            visited[nr][nc] = True

            # Move forward
            stack.append(next_cell)

            if on_step is not None:
                on_step(maze, next_cell, "carve")
                if delay > 0:
                    time.sleep(delay)

        else:
            # Dead end reached, backtrack
            stack.pop()

            if on_step is not None and stack:
                on_step(maze, stack[-1], "backtrack")
                if delay > 0:
                    time.sleep(delay)