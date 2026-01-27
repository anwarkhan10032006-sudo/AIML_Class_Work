#N-Queens Problem Implementation

This project demonstrates the N-Queens problem using a simple Python backtracking implementation suitable for beginners.
It finds a valid arrangement of N queens on a chessboard such that no two queens attack each other.

---

#Pseudocode of N-Queens Problem

```text
N-QUEENS(N)

board ← array of size N initialized to -1

CALL SOLVE(board, 0)


FUNCTION SOLVE(board, row)

    IF row = N THEN
        PRINT board as a valid solution
        RETURN TRUE        // stop after first solution

    FOR col ← 0 TO N-1 DO

        IF IS_SAFE(board, row, col) THEN
            board[row] ← col

            IF SOLVE(board, row + 1) = TRUE THEN
                RETURN TRUE

            board[row] ← -1      // backtrack

    END FOR

    RETURN FALSE


FUNCTION IS_SAFE(board, row, col)

    FOR i ← 0 TO row-1 DO

        IF board[i] = col OR
           ABS(board[i] - col) = ABS(i - row) THEN
            RETURN FALSE

    END FOR

    RETURN TRUE


FUNCTION PRINT_SOLUTION(board)

    FOR i ← 0 TO N-1 DO
        FOR j ← 0 TO N-1 DO
            IF board[i] = j THEN
                PRINT "Q"
            ELSE
                PRINT "."
        PRINT new line

RETURN failure
```

