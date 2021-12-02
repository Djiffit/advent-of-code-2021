with open('01.in') as f:
    lines = [int(x) for x in f.readlines()]

    def comp_window(size):
        total = 0
        for i in range(max(1, size), len(lines)):
            if sum(lines[i - size:i]) < sum(lines[i-size + 1:i+1]):
                total += 1
        return total

    print(comp_window(1), comp_window(3))

