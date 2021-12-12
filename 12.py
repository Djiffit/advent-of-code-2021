from collections import defaultdict

with open('12.in') as f:
    lines = [x.strip().split('-') for x in f.readlines()]
    conns = defaultdict(list)

    for a, b in lines:
        conns[a].append(b)
        conns[b].append(a)

    def travel(node, history, visited_twice=False):
        total = 0
        if node == 'end':
            return 1

        for c in conns[node]:
            if c == 'start':
                continue
            if c.isupper() or (c.islower() and c not in history or not visited_twice):
                repeat = c.islower() and c in history
                history.append(c)
                total += travel(c, history, visited_twice if not repeat else repeat)
                history.pop()

        return total

    print(f'Part 1: {travel("start", ["start"], True)}')
    print(f'Part 2: {travel("start", ["start"], False)}')

