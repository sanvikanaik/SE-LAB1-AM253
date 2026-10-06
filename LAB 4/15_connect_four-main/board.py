ROWS, COLS = 6, 7


class Board:
    def __init__(self):
        self.grid = [["."] * COLS for _ in range(ROWS)]

    def drop(self, col, token):
        if not 0 <= col < COLS:
            return None
        for r in range(ROWS - 1, -1, -1):
            if self.grid[r][col] == ".":
                self.grid[r][col] = token
                return r
        return None

    def legal_columns(self):
        """Columns (0-based) that still have room for a disc."""
        return [c for c in range(COLS) if self.grid[0][c] == "."]

    def copy(self):
        """Independent copy of the board, used by the AI to try moves safely."""
        clone = Board()
        clone.grid = [row[:] for row in self.grid]
        return clone

    def full(self):
        return all(self.grid[0][c] != "." for c in range(COLS))

    def winner(self, token):
        # right, down, down-right diagonal, down-left diagonal
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                if self.grid[r][c] != token:
                    continue
                for dr, dc in directions:
                    if all(
                        0 <= r + i * dr < ROWS and
                        0 <= c + i * dc < COLS and
                        self.grid[r + i * dr][c + i * dc] == token
                        for i in range(4)
                    ):
                        return True
        return False

    def print(self):
        print("\n " + " ".join(str(i + 1) for i in range(COLS)))
        for row in self.grid:
            print(" " + " ".join(row))