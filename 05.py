from collections import defaultdict

with open('05.in') as f:
    lines = f.readlines()

    def count_intersections(diagonal=False):
        counts = defaultdict(int)

        for line in lines:
            left, right = line.split(' -> ')

            ly,lx = [int(x) for x in left.split(',')]
            ry,rx = [int(x) for x in right.split(',')]

            if not diagonal:
                if ly != ry and lx != rx:
                    continue

            right_offset_y = right_offset_x = 0

            if ly - ry != 0:
                right_offset_y = -1 if ry < ly else 1
            if lx - rx != 0:
                right_offset_x = -1 if rx < lx else 1

            for i in range(max(abs(lx - rx), abs(ly - ry)) + 1):
                new_y = ly + right_offset_y * i
                new_x = lx + right_offset_x * i
                counts[(new_y, new_x)] += 1

        total = sum([x > 1 for x in counts.values()]) 
        return total

    print(count_intersections())
    print(count_intersections(True))

