
with open('13.in') as f:
    lines = f.readlines()

    def folder(single=True):
        points = [[int(point) for point in x.strip().split(',')] for x in lines if len(x.split(',')) == 2]
        folds = [x.split()[2] for x in lines if x.startswith('fold')]

        for fold in folds:
            if fold.startswith('x'):
                xf = int(fold.split('=')[1])
                for point in points:
                    if point[0] >= xf:
                        point[0] = xf - ((point[0] - xf))
            else:
                yf = int(fold.split('=')[1])
                for point in points:
                    if point[1] >= yf:
                        point[1] = yf - ((point[1] - yf))
            if single:
                break

        min_y = min([point[1] for point in points])
        min_x = min([point[0] for point in points])
        max_y = max([point[1] for point in points])
        max_x = max([point[0] for point in points])

        points = set([tuple(x) for x in points])

        total = 0
        for y in range(min_y, max_y + 1):
            row = []
            for x in range(min_x, max_x + 1):
                if (x, y) in points:
                    total += 1
                    row.append('X')
                else:
                    row.append(' ')
            if not single:
                print(''.join(row))
        if single:
            print (f'Part 1: {total}\n')

    folder()
    folder(False)

