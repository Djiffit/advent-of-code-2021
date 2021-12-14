from collections import Counter, defaultdict

with open('14.in') as f:
    lines = f.readlines()
    start = lines[0].strip()
    rules = {}
    for rule in lines[2:]:
        src, trgt = [x.strip() for x in rule.split(' -> ')]
        rules[src] = trgt

    pairs = {start[i:i+2] : 1 for i in range(len(start) - 1)}
    runcount = Counter(start)
    part = 1

    for i in range(1, 41):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            val = rules[pair]
            new_pairs[pair[0] + val] += count
            new_pairs[val + pair[1]] += count
            runcount[val] += count
        pairs = new_pairs
        if i == 10 or i == 40:
            print(f'Part {part}: {runcount["S"] - runcount["F"]}')
            part += 1

