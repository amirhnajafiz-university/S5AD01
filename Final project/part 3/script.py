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

def getScore(board,index):
    if index >= N*N:
        return 0
    row = index//N
    col = index%N

    if board[row][col] != 0 :
        return 0
    return index + 1
    
def calculateMaxScore(board , index, queensToPlace):
    placedQ = 0
    score = 0
    currentIndex = index
    while queensToPlace > placedQ and currentIndex < N*N and currentIndex>=0:
        #print(">" + str(currentIndex) + " : " + str(placedQ) )
        scoreToAdd = getScore(board,currentIndex)
        if scoreToAdd > 0 :
            score += scoreToAdd
            placedQ += 1
        currentIndex -= 1
    return score


# res[0] means initQuens and res[1] means resCount
def solveNQUtil(board, row , col , res, score , minScore):
    if res[0] >= N:
        print(score)
        return True

    for i in range(row,-1,-1):
        for j in range(N-1,-1,-1):
            maxPosibleScore = score + calculateMaxScore(board,i*N + j,N - res[0])
            #print("max postibble: "+ str(maxPosibleScore))
            if maxPosibleScore < minScore:
               # print("failed by " + str(maxPosibleScore))
                #printSolution(board)
                #print()
                return False
            if i == row and j >= col:
                continue
            if isSafe(board, i, j):
                newScore = score + getScore(board,i*N + j)
                #print("new score: "+ str(getScore(board,i*N + j)) + " in " , str(i*N + j))
                board[i][j] =1
                res[0] +=1
                if solveNQUtil(board, i ,j-1, res,newScore,minScore) == True:
                    printSolution(board)
                    print()
                    res[1] += 1
                board[i][j] = 0
                res[0] -=1
    return False

board = [[ 0 for _ in range(N)] for _ in range(N)]
res = [0,0]
board[0][N//2] = 2
board[N//2][N//2] = 2
printSolution(board)
input()
solveNQUtil(board, N-1,N-1,res,0,50)
print("countFound :" + str(res[1]))

