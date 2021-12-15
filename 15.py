import heapq
from collections import defaultdict

with open('15.in') as f:
    grid = [[int(x) for x in line.strip()] for line in f.readlines()]
    new_grid = [[0] * len(grid[0]) * 5 for _ in range(len(grid) * 5)]

    for y_off in range(5):
        for x_off in range(5):
            delta = y_off + x_off
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    new_grid[y + y_off * len(grid)][x + x_off * len(grid[0])] = (grid[y][x] + delta - 1) % 9 + 1

    # Only works if the path never goes up or left
    def solve_dp(grid):
        dp = [[[float('inf')]] * len(grid[0]) for _ in range(len(grid))] 
        dp[0][0] = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if y == 0 and x == 0:
                    continue
                if y == 0:
                    dp[y][x] = dp[y][x - 1] + grid[y][x]
                elif x == 0:
                    dp[y][x] = dp[y - 1][x] + grid[y][x]
                else:
                    dp[y][x] = min(dp[y -1][x], dp[y][x - 1]) + grid[y][x]
        return (dp[-1][-1])

    def solve_dijkstra(grid):
        ty, tx = len(grid) - 1, len(grid[0]) - 1
        que = [(0, 0, 0)]
        visited = defaultdict(lambda: float('inf'))

        while len(que):
            risk, y, x = heapq.heappop(que)

            if y == ty and x == tx:
                return risk

            for y_d, x_d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_y, new_x = y + y_d, x + x_d
                if visited[(new_y, new_x)] > risk + grid[y][x] and 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
                    heapq.heappush(que, (risk + grid[y][x], new_y, new_x))
                    visited[(new_y, new_x)] = risk + grid[y][x]
                    
    print(f'Part 1: {solve_dijkstra(grid)}')
    print(f'Part 2: {solve_dijkstra(new_grid)}')
