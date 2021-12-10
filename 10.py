opens = ['(', '<', '{', '[']
mapping = { '(': ')', '<': '>', '{': '}', '[': ']' }
corrupt_cost = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
fix_cost = { '(': 1, '[': 2, '{': 3, '<': 4 }

with open('10.in') as f:
    lines = f.readlines()
    stack, invalids, corruption = [], [], 0

    for line in lines:
        for char in line.strip():
            if char in opens:
                stack.append(char)
            else:
                if len(stack) and char == mapping[stack[-1]]:
                    stack.pop()
                else:
                    corruption += corrupt_cost[char]
                    stack = []
                    break

        invalid = 0
        while len(stack):
            invalid = invalid * 5 + fix_cost[stack.pop()]

        if invalid:
            invalids.append(invalid)

    print(f'Part 1: {corruption}')
    print(f'Part 2: {sorted(invalids)[len(invalids) // 2]}')

