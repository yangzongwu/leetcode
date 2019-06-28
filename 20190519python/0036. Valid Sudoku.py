class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            if not self.validList(board[row]):
                return False
        
        for col in range(len(board[0])):
            nums=[]
            for row in range(len(board)):
                nums.append(board[row][col])
            if not self.validList(nums):
                return False
            
        for i in range(0,9,3):
            for j in range(0,9,3):
                nums=[]
                for m in range(i,i+3):
                    for n in range(j,j+3):
                        nums.append(board[m][n])
                if not self.validList(nums):
                    return False
        
        return True
        
    def validList(self,nums):
        s="0123456789"
        rep=[]
        for num in nums:
            if len(num)!=1:
                return False
            if num in s:
                rep.append(num)
        return len(rep)==len(set(rep))
