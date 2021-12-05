
with open('04.in') as f:
    lines = f.readlines()
    numbers = [int(x) for x in lines[0].split(',')]
    boards = []

    for i in range(2, len(lines), 6):
        rows = lines[i:i+5]
        rows = [[int(x) for x in row.split()] for row in rows]
        boards.append(rows)

    def check_board(board, row, col):
        bingorow = sum([x == 'X' for x in board[row]]) == len(board)
        bingocol = sum([board[y][col] == 'X' for y in range(len(board))]) == len(board[0])

        return bingorow or bingocol

    def count_board(board, mult):
        total = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] != 'X':
                    total += board[y][x]
        return total * mult

    def do_bingo(boards, first=True):
        winners = set()
        last = 0
        for number in numbers:
            for ind, board in enumerate(boards):
                if ind in winners:
                    continue
                for row in range(len(board)):
                    for col in range(len(board[0])):
                        if board[row][col] == number:
                            board[row][col] = 'X'
                            if check_board(board, row, col):
                                winners.add(ind)
                                if first:
                                    return count_board(board, number)
                                else:
                                    last = count_board(board, number)
        return last

    print(do_bingo([row[:] for row in boards]))
    print(do_bingo([row[:] for row in boards], False))

