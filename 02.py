with open('02.in') as f:
    lines = f.readlines()

    def parse_moves(aimer=False):
        depth, horiz, aim = 0, 0, 0

        for cmd, change in [x.split() for x in lines]:
            change = int(change)
            if cmd == 'forward':
                horiz += change
                if aimer:
                    depth += change * aim
            elif cmd == 'down':
                if aimer:
                    aim += change
                else:
                    depth = change + depth
            elif cmd == 'up':
                if aimer:
                    aim -= change
                else:
                    depth = depth - change

        return horiz * depth

    print(parse_moves())
    print(parse_moves(True))

