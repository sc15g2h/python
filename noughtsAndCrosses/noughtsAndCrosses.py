import sys
import random 

def printBanner(): 
    space = "O                                                                                                 X"
    print("X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O\n"+space)
    print("X                                      Noughts & Crosses Game                                     O\n"+space)
    print("X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O\n\n")


def displayInstructions():
    space = "|                                                                                                 |"
    print("X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O")
    print("X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O\n"+space)
    print("|                                      I N S T R C T I O N S                                      |\n"+space)
    print("|   When its your turn enter the position you want to play. Use the grid below as a reference.    |")
    print("|   + - - - + - - - + - - - +                                                                     |")
    print("|   |  0,0  |  0,1  |  0,2  |                                                                     |")
    print("|   + - - - + - - - + - - - +                                                                     |")
    print("|   |  1,0  |  1,1  |  1,2  |                                                                     |")
    print("|   + - - - + - - - + - - - +                                                                     |")
    print("|   |  2,0  |  2,1  |  2,2  |                                                                     |")
    print("|   + - - - + - - - + - - - +                                                                     |")
    print("|   Enter your poisition using `[row][comma][colum]` for example: 1,1                             |\n"+space)
    print("X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O")
    print("O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X\n\n")


# tidy this up
def displayGrid(grid):
    print("+ - - - + - - - + - - - +")
    print("|   " + grid[0][0] + "   |   " + grid[0][1] + "   |   " + grid[0][2] + "   |")
    print("+ - - - + - - - + - - - +")
    print("|   " + grid[1][0] + "   |   " + grid[1][1] + "   |   " + grid[1][2] + "   |")
    print("+ - - - + - - - + - - - +")
    print("|   " + grid[2][0] + "   |   " + grid[2][1] + "   |   " + grid[2][2] + "   |")
    print("+ - - - + - - - + - - - +\n")

def playerTurn(player,grid,comp):
    checkForWinner(grid)
    if(comp == 'Y'):
        p1 = random.randint(0,2)
        p2 = random.randint(0,2)
        position = str(p1) + "," + str(p2) 
        print("Player " + player + " its your turn: " + position)
    else:
        position = input("Player " + player + " its your turn: ") 
    while(checkGridPosition(position,grid) != True ):
        print("Invalid Input - please enter a valid position in the grid")
        position = input("Player " + player + " its your turn: ")
    position = position.split(',')
    grid[int(position[0])][int(position[1])] = player
    displayGrid(grid)

def checkGridPosition(position,grid):
    position=position.split(',')
    if(grid[int(position[0])][int(position[1])] != " "):
        return False
    else:
        return True
            

# check if you have 3 in a row / Announce winner / Identify when grid is full and no winner 
def checkForWinner(grid):
    winninggroups = [   # horizontal
                        ["0,0","0,1","0,2"],
                        ["1,0","1,1","1,2"],
                        ["2,0","2,1","2,2"],
                        # vertical
                        ["0,0","1,0","2,0"],
                        ["0,1","1,1","2,1"],
                        ["0,2","1,2","2,2"],
                        # diagonal
                        ["0,0","1,1","2,2"],
                        ["2,0","1,1","0,2"],
                      ]

    #check X
    for winningLine in winninggroups:
        counterX = 0
        counterO = 0
        for position in winningLine:
            position.split(',')
            if(grid[int(position[0])][int(position[2])] == 'X'):
                counterX += 1
            if(grid[int(position[0])][int(position[2])] == 'O'):
                counterO += 1
        if(counterO == 3):
            print("\nPLAYER O WINS!\n")
            exit()
        if(counterX == 3):
            print("\nPLAYER X WINS!\n")
            exit()


# Alternative size grid / x in a row

# validity of input ie. check if coordinates are correct


def main():
    printBanner()

    if(len(sys.argv) >=2):
        if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            displayInstructions()

    comp = input("Do you want to play the computer? (Y/N) : ")



    print("                                       L E T S   P L A Y !                                           ")
    print("X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O\n")


    print("\n\nYou're player X.")

    # Define grid for game
    grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
    displayGrid(grid)

    # game
    turn =0
    while True:
        if(turn % 2 == 0):
            player = "X"
            playerTurn(player,grid,'N')
            turn +=1
        else:
            player = "O"
            playerTurn(player,grid,comp)
            turn +=1


main()