'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not 
flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be 
flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board:
            for row in range(len(board)):
                if board[row][0]=='O':
                    self.fillboard(board,row,0)
                if board[row][len(board[0])-1]=='O':
                    self.fillboard(board,row,len(board[0])-1)
            for column in range(1,len(board[0])):
                if board[0][column]=='O':
                    self.fillboard(board,0,column)
                if  board[len(board)-1][column]=='O':
                    self.fillboard(board,len(board)-1,column)
            for row in range(len(board)):
                for column in range(len(board[0])):
                    if board[row][column]=='O':
                        board[row][column]='X'
            for row in range(len(board)):
                for column in range(len(board[0])):
                    if board[row][column]=='Y':
                        board[row][column]='O'
                    
    def fillboard(self,board,row,column):
        board[row][column]='Y'
        if row-1>=0 and board[row-1][column]=='O':
            self.fillboard(board,row-1,column)
        if column-1>=0 and board[row][column-1]=='O':
            self.fillboard(board,row,column-1)
        if row+1<len(board) and board[row+1][column]=='O':
            self.fillboard(board,row+1,column)
        if column+1<len(board[0]) and board[row][column+1]=='O':
            self.fillboard(board,row,column+1)
