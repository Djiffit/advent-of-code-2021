from collections import Counter

segments = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c', 'f'],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'e', 'f', 'g'],
        7: ['a', 'c', 'f'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g']
}

with open('08.in') as f:
    lines = f.readlines()
    total, part1 = 0, 0

    for line in lines:
        mappings = {}
        patterns, out_val = line.split(' | ')
        counts = Counter(''.join(patterns.split()))

        sevens, eights = [], []
        seven_c, eight_c = [0, 0], [0, 0]

        for key, val in counts.items():
            if val == 4:
                mappings['e'] = key
            elif val == 6:
                mappings['b'] = key
            elif val == 9:
                mappings['f'] = key
            elif val == 7:
                sevens.append(key)
            else:
                eights.append(key)

        for vals in patterns.split():
            for ind, sev in enumerate(sevens):
                if sevens[ind] in vals and mappings['e'] in vals:
                    seven_c[ind] += 1
            for ind, eigh in enumerate(eights):
                if eights[ind] in vals and mappings['b'] in vals:
                    eight_c[ind] += 1

        if seven_c[0] < seven_c[1]:
            mappings['d'] = sevens[0]
            mappings['g'] = sevens[1]
        else:
            mappings['d'] = sevens[1]
            mappings['g'] = sevens[0]

        if eight_c[0] < eight_c[1]:
            mappings['c'] = eights[0]
            mappings['a'] = eights[1]
        else:
            mappings['c'] = eights[1]
            mappings['a'] = eights[0]

        new_nums = {''.join(list(sorted(mappings[x] for x in v))) : k for k, v in segments.items()}

        num = 0
        for digit in out_val.split():
            if len(digit) in (len(segments[x]) for x in (4,1,7,8)):
                part1 += 1
            num = num * 10 + new_nums[''.join(sorted(digit))]

        total += num

    print(f'Part 1: {part1}')
    print(f'Part 2: {total}')

