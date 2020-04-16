'''
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

 

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.

'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rep=[['1','1','1'] for _ in range(3)]
        cnt=0
        for move in moves:
            if cnt%2==0:
                rep[move[0]][move[1]]='X'
            else:
                rep[move[0]][move[1]]='O'
            if cnt>2 and self.isWin(rep,move[0],move[1]):
                return 'A' if cnt%2==0 else 'B'
            cnt+=1
        print(rep)
        return 'Draw' if cnt==9 else 'Pending'

    def isWin(self,rep,row,col):
        target=rep[row][col]

        r,c,cnt=row,col,1
        while r-1>=0 and rep[r-1][c]==target:
            cnt+=1
            r-=1
        r,c=row,col
        while r+1<3 and rep[r+1][c]==target:
            cnt+=1
            r+=1
        if cnt==3:
            return True

        r,c,cnt=row,col,1
        while c-1>=0 and r-1>=0 and rep[r-1][c-1]==target:
            cnt+=1
            r-=1
            c-=1
        r,c=row,col
        while c+1<3 and r+1<3 and rep[r+1][c+1]==target:
            cnt+=1
            c+=1
            r+=1
        if cnt==3:
            return True
        
        r,c,cnt=row,col,1
        while c-1>=0 and rep[r][c-1]==target:
            cnt+=1
            c-=1
        r,c=row,col
        while c+1<3 and rep[r][c+1]==target:
            cnt+=1
            c+=1
        if cnt==3:
            return True
        
        r,c,cnt=row,col,1
        while c-1>=0 and r+1<3 and rep[r+1][c-1]==target:
            cnt+=1
            r+=1
            c-=1
        r,c=row,col
        while c+1<3 and r-1>=0 and rep[r-1][c+1]==target:
            cnt+=1
            c+=1
            r-=1
        if cnt==3:
            return True

        return False
