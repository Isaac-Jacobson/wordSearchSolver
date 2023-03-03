#  0 1 2 
#  3 x 4
#  5 6 7       -> Direction key

from xml.etree.ElementTree import tostring

directions = "NW", "N", "NE", "W", "E", "SW", "S", "SE"

def checkWord(grid, word, row, col, direction):
    count = 0
    for i in range(0, len(word)):
        if(row<0 or col<0): return False
        if(row>=len(grid) or col>=len(grid[row])): return False
        if(grid[row][col] != word[count]): return False
        else: 
            count+=1
            if(direction==0): row-=1; col-=1
            elif(direction==1): row-=1
            elif(direction==2): row-=1; col+=1
            elif(direction==3): col-=1
            elif(direction==4): col+=1
            elif(direction==5): row+=1; col-=1
            elif(direction==6): row+=1
            elif(direction==7): row+=1; col+=1
    return True

def checkFromLetter(grid, word, row, col):
    for i in range(0, 7):
        if(checkWord(grid, word, row, col, i)): 
            print("Word Found: " + word)
            print("Strarting at: (" + str(row) + "," + str(col) + ")")
            print("Direction: " + directions[i])
            return True
    return False

def printGrid(grid):
    print("GRID: ")
    line = ""
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            line = line + grid[i][j] + " "
        print(line)
        line = ""

def solve(grid, words):
    for word in words:
        flag = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if(checkFromLetter(grid, word, i, j)): flag+=1
        if(flag==0): print("WORD NOT FOUND: " + word)

grid = [['E', 'A', 'S', 'Y'],['N', 'O', 'E', 'N'],['U', 'U', 'X', 'U'], ['J', 'W', 'S', 'R']]
words = "EASY", "JUNE", "NEON", "SUN", "UEA"
print("Words: EASY, JUNE, NEON, SUN, UEA")
printGrid(grid)
solve(grid, words)
