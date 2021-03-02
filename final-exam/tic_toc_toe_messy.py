# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random
from typing import List


BOARD_LENGTH = 3
NUM_BOXES = BOARD_LENGTH * BOARD_LENGTH


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo: List[str], le: str) -> bool:
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    def is_winner_by_row(winning_sequence):
        '''Check each row of the board, to see if the player has won.'''
        for board_index in range(1, NUM_BOXES, BOARD_LENGTH):
            board_row = bo[board_index:board_index + BOARD_LENGTH]
            if board_row == winning_sequence:
                return True
        # if no rows win, then return False
        return False

    def is_winner_by_column(winning_sequence):
        '''Check each column of the board, to see if the player has won.'''
        # get the start of each column
        for col_start in range(1, BOARD_LENGTH + 1):
            # form an array of the column
            board_col = list()
            for board_pos in range(col_start, NUM_BOXES, BOARD_LENGTH):
                board_col.append(bo[board_pos])
            # compare to the desired values
            if board_col == winning_sequence:
                return True
        # if no cols win, then return False
        return False
        
    def is_winner_by_diagonal(winning_sequence):
        '''Check both diagonals of the board, to see if the player has won.'''
        # form the diagonals
        up_to_down = [
            bo[index] for index in range(1, NUM_BOXES, BOARD_LENGTH + 1)
        ]
        down_to_up = [
            bo[index] for index in 
            range(BOARD_LENGTH, NUM_BOXES, BOARD_LENGTH - 1)
        ]
        # check the diagonals against the desired sequence
        if winning_sequence == up_to_down or winning_sequence == down_to_up:
            return True
        return False

    # init a list of the letters the board must have, for the player to win
    winning_sequence = [le for _ in range(BOARD_LENGTH)]
    return (
        is_winner_by_row(winning_sequence) or
        is_winner_by_column(winning_sequence) or
        is_winner_by_diagonal(winning_sequence)
    ) 

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    return [board_val for board_val in board]

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move.
    player_move = None
    moves = set(str(move_num) for move_num in range(1, len(board) + 1))
    # find out which space the player wants to move
    while player_move not in moves or \
          not isSpaceFree(board, int(player_move)):
        # prompt the player to choose their move
        print('What is your next move? (1-9)')
        player_move = input()
    return int(player_move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if possibleMoves:
        return random.choice(possibleMoves)
    return None

def getComputerMove(board, computerChar):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerChar == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerChar, i)
            if isWinner(copy, computerChar):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None: # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')

    # TODO: The following mega code block is a huge hairy monster. Break it down 
    # into smaller methods. Use TODO s and the comment above each section as a guide 
    # for refactoring.

    while True:
        # Reset the board
        theBoard = [' '] * 10 # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True # TODO: Study how this variable is used. Does it ring a bell? (which refactoring method?) 
                            #       See whether you can get rid of this 'flag' variable. If so, remove it.

        while gameIsPlaying: # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
                            #       Use a meaningful name for the function you choose.
            if turn == 'player':
                # Player’s turn.
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:  # TODO: is this 'else' necessary?
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:  # TODO: Is this 'else' necessary?
                        turn = 'computer'

            else:
                # Computer’s turn.
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:     # TODO: is this 'else' necessary?
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else: # TODO: Is this 'else' necessary?
                        turn = 'player'

        if not playAgain():
            break
