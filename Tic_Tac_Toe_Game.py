def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn")
        
        # Get user input for row and column
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    board[row][col] = players[current_player]
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Check if the current player wins
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins! Congratulations!")
            break

        # Check if the board is full (draw)
        if is_board_full(board):
            print_board(board)
            print("It's a draw! Good game!")
            break

        # Switch to the other player
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
