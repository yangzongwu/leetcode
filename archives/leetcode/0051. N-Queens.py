class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        rep = []
        chessboard = [['.' for i in range(n)] for i in range(n)]
        self.subsolveNQueens(chessboard, n, rep, 0)
        return rep

    def subsolveNQueens(self, chessboard, n, rep, row):
        if row == n:
            rep.append(chessboard)
            return
        for column in range(n):
            if self.checkQueens(chessboard, row, column, n):
                chessboard[row][column] = 'Q'
                self.subsolveNQueens(chessboard, n, rep, row + 1)
                chessboard[row][column] = '.'

    def checkQueens(self, chessboard, row, column, n):
        for i in range(n):
            if chessboard[i][column] != '.' or chessboard[row][i] != '.':
                return False
        i = 1
        while row - i >= 0 and column - i >= 0:
            if chessboard[row - i][column - i] != '.':
                return False
            i += 1
        i = 1
        while row + i < n and column + i < n:
            if chessboard[row + i][column + i] != '.':
                return False
            i += 1
        i = 1
        while row - i >= 0 and column + i < n:
            if chessboard[row - i][column + i] != '.':
                return False
            i += 1
        i = 1
        while row + i < n and column - i >= 0:
            if chessboard[row + i][column - i] != '.':
                return False
            i += 1
        return True
if __name__=='__main__':
    Test=Solution()
    print(Test.solveNQueens(1))
