class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        <2--0
        2,3--keep
        >3--0
        
        0,
        3---->1
        '''
        for row in range(len(board)):
            for col in range(len(board[0])):
                rep=self.countNeighbor(board,row,col)
                if board[row][col]==0:
                    if rep==3:
                        board[row][col]='01'
                elif board[row][col]==1:
                    if rep<2 or rep>3:
                        board[row][col]='1d'
                        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]=='01':
                    board[row][col]=1
                if board[row][col]=='1d':
                    board[row][col]=0
        
    def countNeighbor(self,board,row,col):
        rep=0
        if row-1>=0:
            if col-1>=0 and (board[row-1][col-1]==1 or board[row-1][col-1]=='1d'):
                rep+=1
            if board[row-1][col]==1 or board[row-1][col]=='1d':
                rep+=1
            if col+1<len(board[0]) and (board[row-1][col+1]==1 or board[row-1][col+1]=='1d'):
                rep+=1
        if col-1>=0 and (board[row][col-1]==1 or board[row][col-1]=='1d'):
            rep+=1
        if col+1<len(board[0]) and (board[row][col+1]==1 or board[row][col+1]=='1d'):
            rep+=1
        if row+1<len(board):
            if col-1>=0 and (board[row+1][col-1]==1 or board[row+1][col-1]=='1d'):
                rep+=1
            if board[row+1][col]==1 or board[row+1][col]=='1d':
                rep+=1
            if col+1<len(board[0]) and (board[row+1][col+1]==1 or board[row+1][col+1]=='1d'):
                rep+=1
        return rep
