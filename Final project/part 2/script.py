N = 8

def printSolution(board):
	for i in range(N):
		for j in range(N):
			print (board[i][j],end=' ')
		print()

def isSafe(board, row, col):
    for IE in range(-1 , 2):
        for JE in range(-1 , 2):
            newRow = row+IE
            newCol = col+JE
            if IE == 0 and JE == 0:
                if board[newRow][newCol] == 0:
                    continue
                else:
                    return False

            while newRow < N and newRow >= 0 and newCol < N and newCol >= 0:
                if board[newRow][newCol] == 1:
                    return False
                if board[newRow][newCol] == 2:
                    break;
                newRow += IE
                newCol += JE
    return True

# res[0] means initQuens and res[1] means resCount
def solveNQUtil(board, row , col , res):
    if res[0] >= N:
        return True

    for i in range(row,N):
        for j in range(N):
            if i == row and j < col:
                continue
            if isSafe(board, i, j):
                board[i][j] =1

                res[0] +=1
                if solveNQUtil(board, i ,j+1, res) == True:
                    printSolution(board)
                    print()
                    res[1] += 1
                board[i][j] = 0
                res[0] -=1
    return False

board = [ [ 0 for _ in range(N)] for _ in range(N)]
res = [0,0]
board[0][N//2] = 2
board[N//2][N//2] = 2
printSolution(board)
input()
solveNQUtil(board, 0,0,res)
print("countFound :" + str(res[1]))

