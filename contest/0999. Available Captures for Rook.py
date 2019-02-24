class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column]=='R':
                    return self.subnumRookCaptures(row,column,board)
    
    def subnumRookCaptures(self,row,column,board):
        rep=0
        
        i,j=row,column
        while row-1>=0 and board[row-1][column]=='.':
            row-=1
        if row-1>=0 and board[row-1][column]=='p':
            rep+=1
            
        row,column=i,j
        while column-1>=0 and board[row][column-1]=='.':
            column-=1
        if column-1>=0 and board[row][column-1]=='p':
            rep+=1
        
        row,column=i,j
        while row+1<len(board) and board[row+1][column]=='.':
            row+=1
        if row+1<len(board) and board[row+1][column]=='p':
            rep+=1
        
        row,column=i,j
        while column+1<len(board[0]) and board[row][column+1]=='.':
            column+=1
        if column+1<len(board[0]) and board[row][column+1]=='p':
            rep+=1
        
        return rep
            
