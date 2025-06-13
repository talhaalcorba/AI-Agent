# Simple Tic-Tac-Toe game

def print_board(board):
    print("\n")
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" | ".join(cell if cell else str(i*3+j+1) for j, cell in enumerate(row)))
        if i < 2:
            print("-" * 9)
    print("\n")


def check_winner(board):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for pos in win_positions:
        a, b, c = pos
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def tic_tac_toe():
    board = ["" for _ in range(9)]
    current = "X"
    moves = 0

    while moves < 9:
        print_board(board)
        choice = input(f"Player {current}, choose a position (1-9): ")
        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Invalid input. Choose a number between 1 and 9.")
            continue
        pos = int(choice) - 1
        if board[pos]:
            print("Position already taken. Choose another.")
            continue
        board[pos] = current
        moves += 1

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return

        current = "O" if current == "X" else "X"

    print_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    tic_tac_toe()
