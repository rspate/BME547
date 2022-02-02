def find_y_on_line(coords1, coords2, x):
    x1, y1 = coords1
    x2, y2 = coords2
    m = (y2-y1)/(x2-x1)
    y = m*(x-x1)+y1
    return y

