class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        left=0
        flag=True
        while left<len(bits):
            if bits[left]==0:
                left+=1
                flag=True
            elif bits[left]==1:
                left+=2
                flag=False
        if left==len(bits) and flag==True:
            return True
        return False
