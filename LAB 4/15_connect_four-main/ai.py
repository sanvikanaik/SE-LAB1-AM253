import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = board.legal_columns()
        if not legal:
            return None

        # 1. Take an immediate win if one exists.
        for col in legal:
            trial = board.copy()
            trial.drop(col, me)
            if trial.winner(me):
                return col

        # 2. Otherwise block the opponent's immediate win.
        for col in legal:
            trial = board.copy()
            trial.drop(col, opponent)
            if trial.winner(opponent):
                return col

        # 3. Otherwise pick any legal column.
        return random.choice(legal)