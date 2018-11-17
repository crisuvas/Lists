from random import randint

board = []
for x in range(5):
    board.append(["0"] * 5)


def print_board(brd):
    for row in brd:
        print(" ".join(row))


def random_row(brd):
    return randint(0, len(brd) - 1)


def random_col(brd):
    return randint(0, len(brd) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: \n"))
    guess_col = int(input("Guess Col: \n"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if(guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, tha\'s not even in the ocean.")
            turn -= 1
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
            turn -= 1
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

        print_board(board)

        if turn == 3:
            print("Game Over")
