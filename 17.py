
def test_launch(d_y, d_x):
    min_y, max_y, min_x, max_x = -75, -49, 241, 275
    best = -float('inf')
    y, x = 0,0

    while y >= min_y and x <= max_x:
        if min_y <= y <= max_y and min_x <= x <= max_x:
            return True, best
        y, x = y + d_y, x + d_x
        best = max(best, y)
        if d_x != 0:
            d_x = (d_x - 1) if d_x > 0 else (d_x + 1)
        d_y -= 1

    return False, best

highest, hitters = -float('inf'), 0

for x in range(300):
    for y in range(-75, 75):
        if test_launch(y, x)[0]:
            hitters += 1
            highest = max(highest, test_launch(y,x)[1])

print(f'Part1: {highest}')
print(f'Part2: {hitters}')

