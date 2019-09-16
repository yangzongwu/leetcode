class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]=='R':
                    return self.getNumRookCaptures(row,col,board)
        return 0
    
    def getNumRookCaptures(self,row,col,board):
        cnt=0
        r,c=row-1,col
        while r>=0:
            if board[r][c]=='p':
                cnt+=1
                break
            elif board[r][c]=='B':
                break
            r-=1
        r,c=row+1,col
        while r<len(board):
            if board[r][c]=='p':
                cnt+=1
                break
            elif board[r][c]=='B':
                break
            r+=1
        r,c=row,col-1
        while c>=0:
            if board[r][c]=='p':
                cnt+=1
                break
            elif board[r][c]=='B':
                break
            c-=1
        r,c=row,col+1
        while c<len(board[0]):
            if board[r][c]=='p':
                cnt+=1
                break
            elif board[r][c]=='B':
                break
            c+=1
        return cnt
    
