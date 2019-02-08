class Solution:
    def solve(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        for row in range(len(board)):
            if board[row][0]=='O':
                self.subFill(board,row,0)
            if board[row][len(board[0])-1]=='O':
                self.subFill(board,row,len(board[0])-1)
                
        for column in range(0,len(board[0])-1):
            if board[0][column]=='O':
                self.subFill(board,0,column)
            if board[len(board)-1][column]=='O':
                self.subFill(board,len(board)-1,column)
                
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column]=='O':
                    board[row][column]='X'
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column]=='Y':
                    board[row][column]='O'
                
        
        
    def subFill(self,board,row,column):
        board[row][column]='Y'
        if row-1>=0 and board[row-1][column]=='O':
            self.subFill(board,row-1,column)
        if column-1>=0 and board[row][column-1]=='O':
            self.subFill(board,row,column-1)
        if row+1<len(board) and board[row+1][column]=='O':
            self.subFill(board,row+1,column)
        if column+1<len(board[0]) and board[row][column+1]=='O':
            self.subFill(board,row,column+1)
        
        
            
