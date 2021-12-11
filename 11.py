
with open('11.in') as f:
    grid = [[int(x) for x in line.strip()] for line in f.readlines()]
    flashes = 0

    def inc(y, x):
        global flashes
        grid[y][x] += 1
        if grid[y][x] == 10:
            flashes += 1
            for y_d in (0, -1, 1):
                for x_d in (0, -1, 1):
                    new_y, new_x = y + y_d, x + x_d
                    if y_d == 0 == x_d or new_y < 0 or new_y == len(grid) or new_x < 0 or new_x == len(grid[0]):
                        continue
                    inc(new_y, new_x)

    for step in range(1000):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                inc(y, x)
    
        step_flashes = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] >= 10:
                    grid[y][x] = 0
                    step_flashes += 1

        if step_flashes == len(grid) * len(grid[0]):
            print(f'Part 2: {step + 1}')
            break

        if step == 99:
            print(f'Part 1: {flashes}')

