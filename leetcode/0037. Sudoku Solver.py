class Solution:
    class Solution:
        def solveSudoku(self, board):
            def isvalid(board, x, y, k):
                tmp = board[x][y]
                board[x][y] = 'D'
                for i in range(9):
                    if board[i][y] == tmp: return False
                for i in range(9):
                    if board[x][i] == tmp: return False
                for i in range(3):
                    for j in range(3):
                        if board[(x // 3) * 3 + i][(y // 3) * 3 + j] == tmp: return False
                board[x][y] = tmp
                return True

            def subsolveSudoku(board):
                for row in range(0, 9):
                    for column in range(0, 9):
                        if board[row][column] == '.':
                            for k in '123456789':
                                board[row][column] = k
                                if isvalid(board, row, column, k) and subsolveSudoku(board):
                                    return board
                                else:
                                    board[row][column] = '.'
                            return False
                return True

            subsolveSudoku(board)


    ########################################################################
    def solveSudoku01(self, board):
        board = self.subsolveSudoku(board)
        return board

    def subsolveSudoku(self, board):
        for row in range(0, 9):
            for column in range(0, 9):
                if board[row][column] == '.':
                    for k in '123456789':
                        board[row][column] = k
                        if self.isvalid(board, row, column, k) and self.solveSudoku(board):
                            return board
                        else:
                            board[row][column] = '.'
                    return False
        return True

    def isvalid(self, board, x, y, k):
        tmp = board[x][y]
        board[x][y] = 'D'
        for i in range(9):
            if board[i][y] == tmp: return False
        for i in range(9):
            if board[x][i] == tmp: return False
        for i in range(3):
            for j in range(3):
                if board[(x // 3) * 3 + i][(y // 3) * 3 + j] == tmp: return False
        board[x][y] = tmp
        return True



        '''
        for i in range(0, 9):
            if board[i][column] == k and i != row:
                return False
            if board[row][i] == k and i != column:
                return False

        for i in range((row // 3) * 3, (row // 3) * 3 + 3):
            for j in range((column // 3) * 3, (column // 3) + 3):
                if board[i][j] == k and  not (i== row or j == column):
                    return False
        return True
        '''


if __name__=='__main__':
    A=[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    Test=Solution()
    print(Test.solveSudoku(A))
