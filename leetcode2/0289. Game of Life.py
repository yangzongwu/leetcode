class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for column in range(len(board[0])):
                rep=self.countBoard(board,row,column)
                
                if board[row][column]==0:
                    if rep==3:
                        board[row][column]='0l'
                else:#board[row][column]==1:
                    if rep!=2 and rep!=3:
                        board[row][column]='1D'
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column]=='0l':
                    board[row][column]=1
                elif board[row][column]=='1D':
                    board[row][column]=0
        
    def countBoard(self,board,row,column):
        rep=0
        
        if row-1>=0:
            if column-1>=0:
                if board[row-1][column-1]==1 or board[row-1][column-1]=='1D':
                    rep+=1
            if board[row-1][column]==1 or board[row-1][column]=='1D':
                    rep+=1
            if column+1<len(board[0]):
                if board[row-1][column+1]==1 or board[row-1][column+1]=='1D':
                    rep+=1
        
        if column-1>=0:
            if board[row][column-1]==1 or board[row][column-1]=='1D':
                rep+=1
        if column+1<len(board[0]):
            if board[row][column+1]==1 or board[row][column+1]=='1D':
                rep+=1
                
        if row+1<len(board):
            if column-1>=0:
                if board[row+1][column-1]==1 or board[row+1][column-1]=='1D':
                    rep+=1
            if board[row+1][column]==1 or board[row+1][column]=='1D':
                    rep+=1
            if column+1<len(board[0]):
                if board[row+1][column+1]==1 or board[row+1][column+1]=='1D':
                    rep+=1
        return rep
