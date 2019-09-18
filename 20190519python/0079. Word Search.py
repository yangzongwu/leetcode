class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used_list=[]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                    if self.isExist(row,col,board,word[1:],used_list+[[row,col]]):
                        return True
        return False
    
    def isExist(self,row,col,board,word,used_list):
        if not word:
            return True
        
        if row-1>=0 and board[row-1][col]==word[0] and [row-1,col] not in used_list:
            if self. isExist(row-1,col,board,word[1:],used_list+[[row-1,col]]):
                return True
        if col-1>=0 and board[row][col-1]==word[0] and [row,col-1] not in used_list:
            if self. isExist(row,col-1,board,word[1:],used_list+[[row,col-1]]):
                return True
        if row+1<len(board) and board[row+1][col]==word[0] and [row+1,col] not in used_list:
            if self. isExist(row+1,col,board,word[1:],used_list+[[row+1,col]]):
                return True
        if col+1<len(board[0]) and board[row][col+1]==word[0] and [row,col+1] not in used_list:
            if self. isExist(row,col+1,board,word[1:],used_list+[[row,col+1]]):
                return True
        return False
        
    
