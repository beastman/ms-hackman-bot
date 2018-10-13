from mshackman_bot.constants import MoveType
from mshackman_bot.field import Cell, Field
from mshackman_bot.pathfinding import heuristic_distance, a_star_search


def test_heuristic_distance():
    a = Cell(1, 1, True)
    b = Cell(2, 5, True)
    assert heuristic_distance(a, b) == 5


def test_a_star_search():
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
    start = f.get_cell_at_xy(0, 0)
    goal = f.get_cell_at_xy(2, 4)
    actual_path = a_star_search(f, start, goal)
    expected_path = (  # List of of expected (x, y) steps
        ((0, 1), MoveType.DOWN),
        ((0, 2), MoveType.DOWN),
        ((0, 3), MoveType.DOWN),
        ((0, 4), MoveType.DOWN),
        ((0, 5), MoveType.DOWN),
        ((1, 5), MoveType.RIGHT),
        ((2, 5), MoveType.RIGHT),
        ((2, 4), MoveType.UP),
    )
    assert len(actual_path) == len(expected_path)
    for i, step in enumerate(actual_path):
        assert ((step[0].x, step[0].y), step[1]) == expected_path[i]
