import math

with open('16.in') as f:

    line = f.readline().strip()
    versions = []
    bits = []
    
    for char in line:
        bits += list(bin(int(char, 16))[2:].zfill(4))
    i = 0 

    def read_n(ind, n):
        op = int(''.join(bits[ind:ind+n]), 2)
        return op, ind + n

    def read_raw(ind, n):
        data = bits[ind:ind+n]
        return data, ind + n

    def parse_num(ind):
        num = []
        num_bits = 0

        while True:
            raw, ind = read_raw(ind, 5)
            num_bits += 4
            num += raw[1:]
            if raw[0] == '0':
                break

        ind += num_bits % 4

        return int(''.join(num), 2), ind

    def parse_packet(nums, ptype):
        if ptype == 0:
            return sum(nums)
        if ptype == 1:
            return math.prod(nums)
        if ptype == 2:
            return min(nums)
        if ptype == 3:
            return max(nums)
        if ptype == 5:
            return int(nums[0] > nums[1])
        if ptype == 6:
            return int(nums[0] < nums[1])
        if ptype == 7:
            return int(nums[0] == nums[1])

    def read_packet(i):
        packet_version, i = read_n(i, 3)
        packet_type, i = read_n(i, 3)
        versions.append(packet_version)

        if packet_type == 4:
            num, i = parse_num(i)
            return num, i
        else:
            length_type, i = read_n(i, 1)
            nums = []
            if length_type == 0:
                total_length_bits, i = read_n(i, 15)
                start = i
                while i < start + total_length_bits:
                    num, i = read_packet(i)
                    nums.append(num)
            elif length_type == 1:
                packet_count, i = read_n(i, 11)
                for c in range(packet_count):
                    num, i = read_packet(i)
                    nums.append(num)

            return parse_packet(nums, packet_type), i

    print(f'Part2: {read_packet(i)[0]}')
    print(f'Part1: {sum(versions)}')

