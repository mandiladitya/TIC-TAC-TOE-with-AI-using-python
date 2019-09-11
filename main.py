board = [ ' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos]=letter;

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] +' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] +' | ' + board[5] +' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] +' | ' + board[8] +' | ' + board[9])
    print('   |   |')

def isWinner(board ,letter):
     return (board[7] == letter and board[8]== letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter and board[3] == letter) or (board[1] == letter and board[4]== letter and board[7] == letter ) or (board[2] == letter and board[5] == letter and board[8] == letter) or  (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)
def playerMove():
     run = True
     while run:
         move = input('Please select the position to plac an \'X\' (1-9)\n ')
         try:
             move = int(move)
             if move>0 and move<10:
                 if spaceIsFree(move):
                     run=False
                     insertLetter('X',move)
                 else:
                     print('space is already occupied \n ')
             else:
                 print('please type a number within the range!  \n ')
         except:
             print('please type a valid number  \n')


def compMove():
     posibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
     move = 0
     for let in  ['O', 'X']:
         for i in posibleMoves:
             boardCopy = board[:] #making a copy of board not reference
             boardCopy[i] = let
             if isWinner(boardCopy,let):
                 move = i
                 return move
     cornerOpen = []
     for i in posibleMoves:
         if i in(1,3,7,9):
             cornerOpen.append(i)
     if len(cornerOpen) > 0:
         move = selectRandom(cornerOpen)
         return move
     if 5 in posibleMoves:
         move = 5
         return move
     edgesOpen = []
     for i in posibleMoves:
         if i in (1, 3, 7, 9):
             edgesOpen.append(i)
     if len(edgesOpen) > 0:
         move = selectRandom(edgesOpen)
     return move


def selectRandom(list):
    import random
    ln = len(list)
    r = random.randrange(0,ln)
    return list[r]
def isBoardFull(board):
    if board.count(' ') > 1:
          return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe game !')
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry I won this game! you need to think strategically')
            break
        if not (isWinner(board,'X')):
            move= compMove()
            if move == 0:
                print('TIE Game')
            else:
                insertLetter('O',move)
                print('Computer  placed an \'O\' in position ',move,';')
            printBoard(board)
        else:
            print('YOU won this game! Good Job')

            break
    if isBoardFull(board):
        print('GAME TIE')

main()