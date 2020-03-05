'''
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

 

Example 1:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.
Example 2:



Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.
Example 3:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.
 

Note:

board.length == board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
'''
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]=='R':
                    return self.countCap(board,row,col)

    def countCap(self,board,row,col):
        cnt=0
        r=row-1
        while r>=0:
            if board[r][col]=='p':
                cnt+=1
                break
            elif board[r][col]=='B':
                break
            r-=1
        r=row+1
        while r<len(board):
            if board[r][col]=='p':
                cnt+=1
                break
            elif board[r][col]=='B':
                break
            r+=1
        c=col-1
        while c>=0:
            if board[row][c]=='p':
                cnt+=1
                break
            elif board[row][c]=='B':
                break
            c-=1
        c=col+1
        while c<len(board[0]):
            if board[row][c]=='p':
                cnt+=1
                break
            elif board[row][c]=='B':
                break
            c+=1
        return cnt
