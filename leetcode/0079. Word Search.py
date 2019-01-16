'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells 
are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

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
'''
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column]==word[0]:
                    if self.subexist(board,row,column,word[1:]):
                        return True
        return False
    
    def subexist(self, board, row, column, word):
        if not word:
            return True
        tmp=board[row][column]
        board[row][column] = '#'
        if row - 1 >= 0 and board[row - 1][column] == word[0]:
            if self.subexist(board, row - 1, column, word[1:]):
                return True
        if column - 1 >= 0 and board[row][column - 1] == word[0]:
            if self.subexist(board, row, column - 1, word[1:]):
                return True
        if row + 1 < len(board) and board[row + 1][column] == word[0]:
            if self.subexist(board, row + 1, column, word[1:]):
                return True
        if column + 1 < len(board[0]) and board[row][column + 1] == word[0]:
            if self.subexist(board, row, column + 1, word[1:]):
                return True
        board[row][column]=tmp


