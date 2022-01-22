const N = 8;

function printSolution(board) {
    table = '<table class="table table-bordered table-dark" style="margin: 10px auto; width:500px">';
    for (var x = 0; x < N; x++) {
        table = table + "<tr>"
        for (var y = 0; y < N; y++) {
            let bg = "secondary";
            if (board[x][y] == 2)
                bg = "dark text-dark";
            else if (board[x][y] == 0)
                bg = "white"

            table = table + "<td class='text-center bg-" + bg + "'>";
            table = table + "Q";
            table = table + "</td>"
        }
        table = table + "</tr>"
    }
    table = table + "</table>";
    document.write(table);
}

function isSafe(board, row, col) {
    for (var IE = -1; IE < 2; IE++) {
        for (var JE = -1; JE < 2; JE++) {
            newRow = row + IE;
            newCol = col + JE;

            if (IE == 0 && JE == 0) {
                if (board[newRow][newCol] == 0)
                    continue;
                else   
                    return false;
            }

            while (newRow < N && newRow >= 0 && newCol < N && newCol >= 0) {
                if (board[newRow][newCol] == 1)
                    return false;
                if (board[newRow][newCol] == 2)
                    break;
                newRow += IE;
                newCol += JE;
            }
        }
    }
    return true;
}

function getScore(board, index) {
    if (index >= N*N) 
        return 0;
    let row = Math.floor(index / N);
    let col = index % N;

    if (board[row][col] != 0) 
        return 0;
    
    return index + 1;
}

function calculateMaxScore(board, index, queensToPlace) {
    let placedQ = 0;
    let score = 0;
    let currentIndex = index;

    while (queensToPlace > placedQ && currentIndex < N*N && currentIndex >= 0) {
        let scoreToAdd = getScore(board, currentIndex);
        if (scoreToAdd > 0) {
            score += scoreToAdd;
            placedQ++;
        }
        currentIndex -= 1;
    }

    return score;
}

function solveNQUtil(board, row, col, res, score, minScore) {
    if (res[0] >= N) {
        document.write(score);
        return true
    }

    for (var i = row; i > -1; i--) {
        for (var j = N-1; j > -1; j--) {
            maxPossibleScore = score + calculateMaxScore(board, i*N+j, N-res[0]);
            if (maxPossibleScore < minScore) 
                return false;
            if (i == row && j < col)
                continue;
            if (isSafe(board, i, j)) {
                newScore = score + getScore(board, i*N+j);

                board[i][j] =1;
                res[0] +=1;

                if (solveNQUtil(board, i ,j+1, res, newScore, minScore)) {
                    printSolution(board);
                    document.write("<br />");
                    res[1] += 1;
                }
                board[i][j] = 0;
                res[0] -=1;
            }
        }
    }

    return false;
}

var board = new Array(N);

for (var i = 0; i < N; i++) {
    board[i] = new Array(N);
    for (var j = 0; j < N; j++) {
        board[i][j] = Math.random() > 0.8 ? 2 : 0;
    }
}

res = [0, 0];
printSolution(board);
document.write("<br />");
solveNQUtil(board, N-1, N-1, res, 0, 50);
document.write("count found: " + res[1]);