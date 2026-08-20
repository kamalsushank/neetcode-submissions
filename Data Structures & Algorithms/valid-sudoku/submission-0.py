class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s1 = set()
            for ele in row:
                if (ele !='.'):
                    if (ele in s1):
                        return False
                    else:
                        s1.add(ele)
        for j in range(9):
            s2 = set()
            for i in range(9):
                if (board[i][j] != '.'):
                    if (board[i][j] in s2):
                        return False
                    else :
                        s2.add(board[i][j])
        for rows in range(0,9,3):
            for cols in range(0,9,3):
                s3 = set ()
                for i in range(rows, rows+3):
                    for j in range(cols ,cols+3):
                        if board[i][j] != ".":
                            if board[i][j] in  s3:
                                return False
                            else:
                                s3.add(board[i][j])
        return True
