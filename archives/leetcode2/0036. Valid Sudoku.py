class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            rep=[]
            for digit in row:
                if digit!='.':
                    rep.append(digit)
            if not self.subisisValidSudoku(rep):
                return False
        for column in range(9):
            rep=[]
            for row in range(9):
                if board[row][column]!='.':
                    rep.append(board[row][column])
            if not self.subisisValidSudoku(rep):
                return False
        for i in range(0,7,3):
            for j in range(0,7,3):
                rep=[]
                for row in range(i,3+i):
                    for column in range(j,3+j):
                        if board[row][column]!='.':
                            rep.append(board[row][column])
                if not self.subisisValidSudoku(rep):
                    return False
        return True
    
    def subisisValidSudoku(self,num):
        if len(num)!=len(list(set(num))):
            return False
        for i in num:
            if i not in '123456789':
                return False
        return True
