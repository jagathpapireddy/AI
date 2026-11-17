import random

N = 8

def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def display(board):
    for row in range(N):
        for col in range(N):
            print("Q" if board[col] == row else ".", end=" ")
        print()


def hill_climbing(max_steps):
    board = [random.randint(0, N - 1) for _ in range(N)]

    for step in range(1, max_steps + 1):
        current_h = heuristic(board)

        print("\nStep:", step)
        print("State:", board)
        print("Conflicts:", current_h)

        if step <= 6:
            display(board)

        if current_h == 0:
            print("\nFINAL SOLUTION FOUND")
            print("State:", board)
            print("Conflicts:", current_h)
            display(board)
            return

        best_board = None
        best_h = current_h

        for col in range(N):
            old_row = board[col]

            for row in range(N):
                if row == old_row:
                    continue

                board[col] = row
                h = heuristic(board)

                if h < best_h:
                    best_h = h
                    best_board = board.copy()

            board[col] = old_row

        if best_board is None:
            board = [random.randint(0, N - 1) for _ in range(N)]
        else:
            board = best_board

    print("\nMaximum steps reached.")
    print("FINAL STATE:", board)
    print("Final conflicts:", heuristic(board))

    if heuristic(board) == 0:
        print("Solution found!")
    else:
        print("No solution found within the step limit.")


max_steps = int(input("Enter maximum steps: "))
hill_climbing(max_steps)
