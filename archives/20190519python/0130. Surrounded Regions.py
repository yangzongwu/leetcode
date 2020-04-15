class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board:
            for row in range(len(board)):
                if board[row][0]=='O':
                    self.reFillBoard(board,row,0)
                if board[row][len(board[0])-1]=='O':
                    self.reFillBoard(board,row,len(board[0])-1)
        
            for col in range(len(board[0])):
                if board[0][col]=='O':
                    self.reFillBoard(board,0,col)
                if board[len(board)-1][col]=='O':
                    self.reFillBoard(board,len(board)-1,col)
                
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col]=='O':
                        board[row][col]='X'
                        
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col]=='Y':
                        board[row][col]='O'
                    
    def reFillBoard(self,board,row,col):
        board[row][col]='Y'
        if row-1>=0 and board[row-1][col]=='O':
            self.reFillBoard(board,row-1,col)
        if col-1>=0 and board[row][col-1]=='O':
            self.reFillBoard(board,row,col-1)
        if row+1<len(board) and board[row+1][col]=='O':
            self.reFillBoard(board,row+1,col)
        if col+1<len(board[0]) and board[row][col+1]=='O':
            self.reFillBoard(board,row,col+1)
            
