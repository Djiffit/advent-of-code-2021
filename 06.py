from collections import Counter, defaultdict

with open('06.in') as f:
    vals = Counter([int(x) for x in f.readlines()[0].split(',')])

    def simulate(vals, days):
        for i in range(days):
            new_vals = defaultdict(int)
            for k, v in vals.items():
                if k == 0:
                    new_vals[6] += v
                    new_vals[8] += v
                else:
                    new_vals[k - 1] += v
            vals = new_vals
        return sum(vals.values())

    print(simulate({k : v for k, v in vals.items()}, 80))
    print(simulate({k : v for k, v in vals.items()}, 256))


