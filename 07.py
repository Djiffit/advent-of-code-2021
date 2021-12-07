with open('07.in') as f:
    numbers = [int(x) for x in f.readlines()[0].split(',')]
    numbers.sort()
    median = numbers[len(numbers) // 2]
    avg = round(sum(numbers) // len(numbers))
    print(sum([abs(x - median) for x in numbers]))
    print(sum([abs(x - avg) * (abs(x - avg) + 1) // 2 for x in numbers]))

