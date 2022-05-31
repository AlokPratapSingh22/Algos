def check(board, row, col, N):

    drow = row
    dcol = col

    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    row, col = drow, dcol

    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    col = dcol

    while col >= 0 and row < N:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1
    return True


def solve(col, board, N):
    if col == N:
        print("**************")
        print(*(' '.join(row) for row in board), sep='\n')
        print("**************")
        return

    for row in range(0, N):
        if check(board, row, col, N):
            board[row][col] = 'Q'
            solve(col+1, board, N)
            board[row][col] = '.'


def nqueens(N: int) -> list[list[chr]]:
    board = [['.' for _ in range(N)] for __ in range(N)]
    solve(0, board, N)


nqueens(8)
