from ships import *

board = []

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    print "  A B C D E F G H I J"
    for i, row in enumerate(board):
        print str(i) + " " + " ".join(row)

def soloGame():
    print_board(board)
    compShips = Ships()

    turn = 1
    print "Guess ship location in column/row format (ex. A6)"
    while turn < 50:
        print "Turn", turn
        guess = str(raw_input("Guess location: "))
        guessClean = str(guess[0].upper() + guess[1:])

        if ord(guessClean[0]) < 65 or \
           ord(guessClean[0]) > 74 or \
           ord(guessClean[1]) < 48 or \
           ord(guessClean[1]) > 57 or \
           len(guessClean) > 2:
            print "Invalid guess, try again."
            turn = turn - 1
        else:
            if(board[ord(guessClean[1]) - 48][ord(guessClean[0]) - 65] == "*") or \
                (board[ord(guessClean[1]) - 48][ord(guessClean[0]) - 65] == "X"):
                print "You guessed that one already."
                turn = turn - 1
            elif compShips.checkHit(guessClean):
                board[ord(guessClean[1]) - 48][ord(guessClean[0]) - 65] = "*"
                print "Hit!"
                hitShip = compShips.returnHit(guessClean)
                hitShip.hit()
                if hitShip.destroyed:
                    print "You sunk my " + str(hitShip.name) + "!"
                    if compShips.destroyedCheck():
                        print "You win!"
                        break
            else:
                print "You missed!"
                board[ord(guessClean[1]) - 48][ord(guessClean[0]) - 65] = "X"
        turn = turn + 1
        print_board(board)

    print "Game Over"

"""
print "Let's play Battleship!"
choice = raw_input("Would you like the computer to shoot back at you? (Y/N)")
if choice == "Y" or choice == "y":
"""
soloGame();
