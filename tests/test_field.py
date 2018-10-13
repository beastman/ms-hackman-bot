from mshackman_bot.constants import MoveType
from mshackman_bot.field import Field


def test_update():
    f = Field(19, 15)
    assert f.x_size == 19
    assert f.y_size == 15
    f.update(
        'S,.,.,x,.,.,.,.,.,.,.,.,.,.,.,x,.,.,S,'
        '.,x,.,x,.,x,x,x,x,.,x,x,x,x,.,x,.,x,.,'
        '.,x,.,.,.,x,.,.,.,.,.,.,.,x,.,C,.,x,.,'
        '.,x,x,x,.,x,.,x,x,x,x,x,.,x,.,x,x,x,.,'
        '.,x,.,.,.,x,.,.,.,.,.,.,.,x,.,.,.,x,.,'
        '.,.,.,x,.,x,.,x,x,.,x,x,.,x,.,x,.,.,.,'
        'x,.,x,x,.,.,.,x,x,.,x,x,.,.,.,x,x,.,x,'
        'Gl,.,x,x,P0,x,x,x,x,.,x,x,x,x,P1,x,x,.,Gr,'
        'x,.,x,x,.,.,.,.,.,C,.,.,.,.,.,x,x,.,x,'
        '.,.,.,x,.,x,x,x,x,x,x,x,x,x,.,x,.,.,.,'
        '.,x,.,.,.,.,.,.,x,x,x,.,.,.,.,.,.,x,.,'
        '.,x,.,x,x,.,x,.,.,.,.,.,x,.,x,x,.,x,.,'
        '.,x,.,x,x,.,x,x,x,x,x,x,x,.,x,x,.,x,.,'
        '.,x,.,x,x,.,x,.,.,.,.,.,x,.,x,x,.,x,.,'
        'S,.,.,.,.,.,.,.,x,x,x,.,.,.,.,.,.,.,S'
    )
    assert f.code_snippets == [(15, 2), (9, 8)]
    assert f.get_player_position('0') == (4, 7)
    assert f.get_player_position('1') == (14, 7)
    c = f.get_cell_at_xy(5, 0)
    assert c.x == 5
    assert c.y == 0
    c = f.get_cell_at_xy(18, 14)
    assert c.x == 18
    assert c.y == 14


def test_neighbors():
    f = Field(19, 15)
    f.update(
        'S,.,.,x,.,.,.,.,.,.,.,.,.,.,.,x,.,.,S,'
        '.,x,.,x,.,x,x,x,x,.,x,x,x,x,.,x,.,x,.,'
        '.,x,.,.,.,x,.,.,.,.,.,.,.,x,.,C,.,x,.,'
        '.,x,x,x,.,x,.,x,x,x,x,x,.,x,.,x,x,x,.,'
        '.,x,.,.,.,x,.,.,.,.,.,.,.,x,.,.,.,x,.,'
        '.,.,.,x,.,x,.,x,x,.,x,x,.,x,.,x,.,.,.,'
        'x,.,x,x,.,.,.,x,x,.,x,x,.,.,.,x,x,.,x,'
        'Gl,.,x,x,P0,x,x,x,x,.,x,x,x,x,P1,x,x,.,Gr,'
        'x,.,x,x,.,.,.,.,.,C,.,.,.,.,.,x,x,.,x,'
        '.,.,.,x,.,x,x,x,x,x,x,x,x,x,.,x,.,.,.,'
        '.,x,.,.,.,.,.,.,x,x,x,.,.,.,.,.,.,x,.,'
        '.,x,.,x,x,.,x,.,.,.,.,.,x,.,x,x,.,x,.,'
        '.,x,.,x,x,.,x,x,x,x,x,x,x,.,x,x,.,x,.,'
        '.,x,.,x,x,.,x,.,.,.,.,.,x,.,x,x,.,x,.,'
        'S,.,.,.,.,.,.,.,x,x,x,.,.,.,.,.,.,.,S'
    )

    cell = f.get_cell_at_xy(0, 0)
    neighbors = f.get_neighbor_cells(cell)
    assert len(neighbors) == 2
    assert (MoveType.RIGHT, f.get_cell_at_xy(1, 0)) in neighbors
    assert (MoveType.DOWN, f.get_cell_at_xy(0, 1)) in neighbors
    cell = f.get_cell_at_xy(9, 8)
    print(cell.y)
    neighbors = f.get_neighbor_cells(cell)
    assert len(neighbors) == 4
    assert (MoveType.UP, f.get_cell_at_xy(9, 7)) in neighbors
    assert (MoveType.LEFT, f.get_cell_at_xy(8, 8)) in neighbors
    assert (MoveType.RIGHT, f.get_cell_at_xy(10, 8)) in neighbors
