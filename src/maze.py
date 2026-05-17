class Maze:

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols

        self.north_wall = [[True] * cols for _ in range(rows)]
        self.east_wall  = [[True] * cols for _ in range(rows)]

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def has_north_wall(self, r: int, c: int) -> bool:
        return self.north_wall[r][c]

    def has_east_wall(self, r: int, c: int) -> bool:
        return self.east_wall[r][c]

    def has_south_wall(self, r: int, c: int) -> bool:
        if r + 1 >= self.rows:
            return True
        return self.north_wall[r + 1][c]

    def has_west_wall(self, r: int, c: int) -> bool:
        if c - 1 < 0:
            return True
        return self.east_wall[r][c - 1]


    def remove_north_wall(self, r: int, c: int) -> None:
        self.north_wall[r][c] = False

    def remove_east_wall(self, r: int, c: int) -> None:
        self.east_wall[r][c] = False

    def remove_south_wall(self, r: int, c: int) -> None:
        if r + 1 < self.rows:
            self.north_wall[r + 1][c] = False

    def remove_west_wall(self, r: int, c: int) -> None:
        if c - 1 >= 0:
            self.east_wall[r][c - 1] = False

   
    def all_neighbors(self, r: int, c: int) -> list[tuple[int, int]]:
        candidates = [
            (r - 1, c),  
            (r, c + 1),  
            (r + 1, c), 
            (r, c - 1),  
        ]
        return [(nr, nc) for nr, nc in candidates if self.in_bounds(nr, nc)]

    def open_neighbors(self, r: int, c: int) -> list[tuple[int, int]]:
        
        result = []
        if not self.has_north_wall(r, c) and self.in_bounds(r - 1, c):
            result.append((r - 1, c))
        if not self.has_east_wall(r, c) and self.in_bounds(r, c + 1):
            result.append((r, c + 1))
        if not self.has_south_wall(r, c) and self.in_bounds(r + 1, c):
            result.append((r + 1, c))
        if not self.has_west_wall(r, c) and self.in_bounds(r, c - 1):
            result.append((r, c - 1))
        return result
