from typing import Tuple, List, Union

from .constants import MoveType


class Cell:
    def __init__(
        self, x, y, is_accessible
    ):
        self.x = x
        self.y = y
        self.is_accessible = is_accessible

    def __repr__(self):
        return '<mshackman_bot.field.Cell. X: {}; Y: {}>'.format(self.x, self.y)

    def coords_tuple(self):
        return self.x, self.y


class Field:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.cells = []
        self.code_snippets = []
        self.players = {}  # Provides quick access to players' coordinates by their ID

    def update(self, field_str):
        cells = []
        code_snippets = []
        players = {}
        field = field_str.split(',')
        row = []
        x = 0
        y = 0
        for cell in field:
            cell = cell.split(';')
            is_accessible = True
            for c in cell:
                if c == 'x':
                    is_accessible = False
                elif c == 'C':
                    code_snippets.append((x, y))
                elif c.startswith('P'):
                    players[c[1:]] = x, y
                # TODO: Add support for other objects in cell
            row.append(Cell(x, y, is_accessible))

            # Add coords of snippet to separate list for quick access
            x += 1
            if x >= self.x_size:
                cells.append(row)
                row = []
                x = 0
                y += 1
        self.cells = cells
        self.code_snippets = code_snippets
        self.players = players

    def get_cell_at_xy(self, x, y) -> Union[Cell, None]:
        if y > self.y_size - 1 or x > self.x_size - 1:
            return None
        return self.cells[y][x]

    def get_player_position(self, player_id):
        return self.players.get(player_id)

    def get_neighbor_cells(self, cell: Cell) -> List[Tuple[MoveType, Cell]]:
        result = []
        if cell.x > 0:
            result.append((MoveType.LEFT, self.get_cell_at_xy(cell.x - 1, cell.y)))
        if cell.y > 0:
            result.append((MoveType.UP, self.get_cell_at_xy(cell.x, cell.y - 1)))
        if cell.x < self.x_size - 1:
            result.append((MoveType.RIGHT, self.get_cell_at_xy(cell.x + 1, cell.y)))
        if cell.y < self.y_size - 1:
            result.append((MoveType.DOWN, self.get_cell_at_xy(cell.x, cell.y + 1)))
        # TODO: Implement Gates support
        return result
