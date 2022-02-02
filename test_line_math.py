import pytest

@pytest.mark.parametrize("coords_1, coords_2, x, y", [
    [(0,0), (2,2), 1, 1],
    [(3,15),(9,3), 6,9],
    [(2,1), (8,5), 5,3],
    [(35,12),(11, 24), 23,18]
    ])
def test_find_y_on_line(coords_1, coords_2, x, y):
    from line_math import find_y_on_line
    answer = find_y_on_line(coords_1, coords_2, x)
    assert answer == y