import random


# ----------------- Core Game Components -----------------

class Dice:
    pass


class Player:
    pass


# ----------------- CLI Rendering -----------------
class CLIBoard:
    def __init__(self, size=100):
        self.size = size
        self.rows = 10
        self.columns = 10
        self.cell_width = 8  # Adjust this width if you want wider cells

    def render(self, players, snakes_and_ladders):
        # Build a mapping: cell number -> string of player markers.
        cell_players = {}
        for player in players:
            if 1 <= player.position <= self.size:
                marker = player.name.split()[-1]
                cell_players[player.position] = cell_players.get(player.position, "") + marker

        # Create a horizontal border for each row.
        horizontal_border = '+' + ('-' * self.cell_width + '+') * self.columns

        # Render rows from the top (row index 9) to bottom (row index 0).
        for row in range(self.rows - 1, -1, -1):
            row_cells = []
            # Zig-zag ordering: even rows (from bottom) left-to-right; odd rows right-to-left.
            if row % 2 == 0:
                for col in range(self.columns):
                    cell_num = row * self.columns + (col + 1)
                    row_cells.append(self._format_cell(cell_num, cell_players.get(cell_num, ""), snakes_and_ladders))
            else:
                for col in range(self.columns):
                    cell_num = row * self.columns + (self.columns - col)
                    row_cells.append(self._format_cell(cell_num, cell_players.get(cell_num, ""), snakes_and_ladders))
            # Join cells with vertical bars to form a complete row.
            row_line = '|' + '|'.join(row_cells) + '|'
            # Print the border, then the row.
            print(horizontal_border)
            print(row_line)
        # Print the final border after the last row.
        print(horizontal_border)

    def _format_cell(self, cell_num, player_marker, snakes_and_ladders):
        """
        Format a single cell:
          - Display the cell number.
          - Append "L" if a ladder starts here or "S" if a snake starts here.
          - Append player marker(s) (if any) in parentheses.
          - Center the text within the fixed cell width.
        """
        content = str(cell_num)
        if cell_num in snakes_and_ladders:
            dest = snakes_and_ladders[cell_num]
            content += "L" if dest > cell_num else "S"
        if player_marker:
            content += f"({player_marker})"
        return content.center(self.cell_width)

# ----------------- Game Logic -----------------

class SnakeAndLadderGame:
    def __init__(self, player_names, mode="CLI"):
        self.mode = mode.upper()
        self.dice = Dice()
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0
        self.game_over = False

        self.snakes_and_ladders = {
            4: 14,
            9: 31,
            17: 7,
            20: 38,
            28: 84,
            40: 59,
            51: 67,
            54: 34,
            62: 19,
            63: 81,
            64: 60,
            87: 36,
            93: 73,
            95: 75,
            99: 78
        }
        self.board = CLIBoard()

    def play(self):
        print("Welcome to Snake and Ladder (CLI Mode)!")
        print("First player to reach 100 wins.\n")
        pass
# ----------------- Main -----------------

if __name__ == '__main__':
    player_names = ["Player 1", "Player 2"]
    game = SnakeAndLadderGame(player_names)
    game.play()
