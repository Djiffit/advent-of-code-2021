import heapq

with open('09.in') as f:
    lines = [[int(x) for x in line.strip()] for line in f.readlines()]

    def check_risk(y, x):
        val = lines[y][x]
        if (y == 0 or lines[y - 1][x] > val) and (y == len(lines) - 1 or lines[y + 1][x] > val) and (x == 0 or lines[y][x - 1] > val) and (x == len(lines[0]) - 1 or lines[y][x + 1] > val):
            return val + 1
        return 0

    def get_basin(y, x):
        visited = set()
        que = [(y, x)]
        while len(que):
            y, x = que.pop(0)
            if (y,x) in visited:
                continue
            visited.add((y, x))

            prev_val = lines[y][x]

            for y_d, x_d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_y = y_d + y
                new_x = x_d + x
                if (0 <= new_y < len(lines)) and (0 <= new_x < len(lines[0])) and lines[new_y][new_x] > prev_val and lines[new_y][new_x] != 9:
                    que.append((new_y, new_x))

        return len(visited)
        
    basin_heap = []
    tot_risk = 0

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            risk = check_risk(y, x)
            tot_risk += risk
            if risk:
                heapq.heappush(basin_heap, get_basin(y,x))
                if len(basin_heap) > 3:
                    heapq.heappop(basin_heap)

    print(f'Part 1: {tot_risk}')
    print(f'Part 2: {basin_heap[0] * basin_heap[1] * basin_heap[2]}')
