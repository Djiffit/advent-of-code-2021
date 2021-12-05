with open('03.in') as f:
    lines = [x.strip() for x in f.readlines()]
    counts = {i: {} for i in range(len(lines[0]))}

    for line in lines:
        for i in range(len(line)):
            counts[i][line[i]] = counts[i].get(line[i], 0) + 1

    gamma = []
    epsilon = []
    
    valid_ox = [int(x, 2) for x in lines]
    valid_co = [int(x, 2) for x in lines]

    for ind, (k, val) in enumerate(counts.items()):
        ones = val.get('1', 0)
        zeros = val.get('0', 0)

        if ones >= zeros:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')

    def get_pop(nums, bit, popular):
        ones = 0
        zeros = 0
        
        for num in nums:
            if num & (1 << (len(lines[0]) - bit - 1)):
                ones += 1
            else:
                zeros += 1

        new_nums = []

        for num in nums:
            if popular:
                if (ones >= zeros and (num & (1 << (len(lines[0]) - bit - 1))) > 0) or (ones < zeros and (num & (1 << (len(lines[0]) - bit - 1))) == 0):
                    new_nums.append(num)
            else:
                if (ones >= zeros and (num & (1 << (len(lines[0]) - bit - 1))) == 0) or (ones < zeros and (num & (1 << (len(lines[0]) - bit - 1))) > 0):
                    new_nums.append(num)

        return new_nums

    def get_ox(nums):
        bit = 0
        while len(nums) > 1:
            nums = get_pop(nums, bit, True)
            bit += 1

        return nums[0]

    def get_co(nums):
        bit = 0
        while len(nums) > 1:
            nums = get_pop(nums, bit, False)
            bit += 1

        return nums[0]
        
    print(int(''.join(epsilon), 2) * int(''.join(gamma), 2))
    print(get_ox(valid_ox) * get_co(valid_co))

    


   
