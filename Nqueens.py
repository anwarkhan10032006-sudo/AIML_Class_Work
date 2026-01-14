N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row):
    if row == N:
        print_solution(board)
        return True   # prints only one solution

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
            board[row] = -1   # backtrack

    return False


def print_solution(board):
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Driver code
board = [-1] * N
solve(board, 0)
