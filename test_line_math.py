import pytest

@pytest.mark.parametrize("coords_1, coords_2, x, y", [
    [(0,0), (2,2), 1, 1]
    ])
def test_find_y_on_line(coords_1, coords_2, x, y):
    from line_math import find_y_on_line
    answer = find_y_on_line(coords_1, coords_2, x)
    assert answer == y