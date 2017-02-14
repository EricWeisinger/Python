theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print("Welcome to my wonderful game of Tic-Tac-Toe: The Fun Side of Python!")


print("Here are your options: top-L, top-M, top-R, mid-L, mid-M, mid-R,low-L, low-M, or low-R.")
 
def checkWin(board):
    flag = False
    possibleWins = [['top-L', 'top-M', 'top-R'],
                    ['mid-L', 'mid-M', 'mid-R'],
                    ['low-L', 'low-M', 'low-R'],
                    ['top-L', 'mid-L', 'low-L'],
                    ['top-M', 'mid-M', 'low-M'],
                    ['top-R', 'mid-R', 'low-R'],
                    ['top-L', 'mid-M', 'low-R'],
                    ['top-R', 'mid-M', 'low-L']]

    for row in range(len(possibleWins)):
        temp = board[possibleWins[row][0]]
        if temp != ' ':
            for position in possibleWins[row]:
                if board[position] != temp:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                return True

    return False           

def winn(player1, player2, new):
    ways = [['top-L', 'top-M', 'top-R'],
                    ['mid-L', 'mid-M', 'mid-R'],
                    ['low-L', 'low-M', 'low-R'],
                    ['top-L', 'mid-L', 'low-L'],
                    ['top-M', 'mid-M', 'low-M'],
                    ['top-R', 'mid-R', 'low-R'],
                    ['top-L', 'mid-M', 'low-R'],
                    ['top-R', 'mid-M', 'low-L']]
    for i in ways:
        if new[i[0]] == new[i[1]] == new[i[2]] != null:
            winner = new[i[0]]
            if winner == player1:
                return 1
            elif winner == player2:
                return 0
            if null not in new: 
                return 'TIE'
    if null not in new: 
        return 'TIE'    
    return None


def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

player1 = 'X'
for i in range(9):
    printBoard(theBoard) 
    print('Turn for ' + player1 + '. Move on which space?')
    while True:
        move = input()
        if move in theBoard:
            if theBoard[move] != ' ':
                print('Invalid move. Try again.')
            else:
                break
        else:
            print('Invalid move. Try again.')
    theBoard[move] = player1
    if checkWin(theBoard):
        printBoard(theBoard) 
        print('Player ' + player1 + ' wins!' +  playAgain())



player2 = 'O'
for i in range(9):
    printBoard(theBoard) 
    print('Turn for ' + player2 + '. Move on which space?')
    while True:
        move = input()
        if move in theBoard:
            if theBoard[move] != ' ':
                print('Invalid move. Try again.')
            else:
                break
        else:
            print('Invalid move. Try again.')
    theBoard[move] = turn
    if checkWin(theBoard):
        printBoard(theBoard) 
        print('Player ' + player2 + ' wins!')
        break
    
