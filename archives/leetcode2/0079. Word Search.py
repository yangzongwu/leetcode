class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column]==word[0]:
                    if self.subexist(board,row,column,word[1:],[[row,column]]):
                        return True
        return False
    
    def subexist(self,board,row,column,word,res):
        if not word:
            return True
        flag1,flag2,flag3,flag4=False,False,False,False
        if row-1>=0 and ([row-1,column] not in res) and board[row-1][column]==word[0]:
            flag1=self.subexist(board,row-1,column,word[1:],res+[[row-1,column]])
        if flag1:return True
        if column-1>=0 and ([row,column-1] not in res) and board[row][column-1]==word[0]:
            flag2=self.subexist(board,row,column-1,word[1:],res+[[row,column-1]])
        if flag2:return True
        if row+1<len(board) and ([row+1,column] not in res) and board[row+1][column]==word[0]:
            flag3=self.subexist(board,row+1,column,word[1:],res+[[row+1,column]])
        if flag3:return True
        if column+1<len(board[0]) and ([row,column+1] not in res) and board[row][column+1]==word[0]:
            flag4=self.subexist(board,row,column+1,word[1:],res+[[row,column+1]])
        if flag4:return True
        return False
          
