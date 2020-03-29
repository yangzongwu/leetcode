'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                    if self.isExist(board,row,col,word[1:]):
                        return True
        return False

    def isExist(self,board,row,col,word):
        if not word:
            return True
        cur=board[row][col]
        board[row][col]='1'
        if row-1>=0 and board[row-1][col]==word[0]:
            if self.isExist(board,row-1,col,word[1:]):
                return True
        if col-1>=0 and board[row][col-1]==word[0]:
             if self.isExist(board,row,col-1,word[1:]):
                return True
        if row+1<len(board) and board[row+1][col]==word[0]:
            if self.isExist(board,row+1,col,word[1:]):
                return True
        if col+1<len(board[0]) and board[row][col+1]==word[0]:
             if self.isExist(board,row,col+1,word[1:]):
                return True
        board[row][col]=cur
        return False
