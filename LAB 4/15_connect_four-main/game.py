from board import Board, COLS
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def ask_human_column(self):
        """Ask until the player gives a playable column. Returns a 0-based
        column, or None if the player quits."""
        while True:
            try:
                raw = input(f"Column (1-{COLS}), or q: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                return None
            if raw == "q":
                return None
            try:
                col = int(raw) - 1
            except ValueError:
                print("Enter a column number.")
                continue
            if not 0 <= col < COLS:
                print(f"Column must be between 1 and {COLS}.")
                continue
            if col not in self.board.legal_columns():
                print(f"Column {col + 1} is full. Choose another.")
                continue
            return col

    def run(self):
        print("Connect Four — you are X, the computer is O.")
        while True:
            self.board.print()

            if self.turn == "X":
                col = self.ask_human_column()
                if col is None:
                    print("Game ended. Thanks for playing.")
                    return
            else:
                col = self.ai.choose_column(self.board)
                if col is None:  # no legal column left
                    print("Draw.")
                    return

            row = self.board.drop(col, self.turn)
            if row is None:  # should not happen; never continue on a bad move
                print("Column unavailable.")
                return

            # Move-level feedback: printed once per disc actually placed.
            print(f"{self.turn} placed a disc in column {col + 1}.")

            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return

            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            self.turn = "O" if self.turn == "X" else "X"