class Solution:
    def canPlaceFlowers(self, flowerbed: 'List[int]', n: 'int') -> 'bool':
        rep=0
        left=0
        while left<len(flowerbed) and flowerbed[left]==0:
            left+=1
        
        if left==len(flowerbed):
            return self.allcanflowerbed(left)>=n
        else:
            rep+=self.sidecanflowerbed(left)
            
        right=len(flowerbed)-1
        while right>=left and flowerbed[right]==0:
            right-=1
        rep+=self.sidecanflowerbed(len(flowerbed)-1-right)
        
        
        while left<right:
            k=1
            while left+k<right and flowerbed[left+k]==0:
                k+=1
            rep+=self.midcanflowerbed(k-1)
            left+=k
        
        return rep>=n
    
    def allcanflowerbed(self,k):
        if k%2==0:
            return k//2
        else:
            return k//2+1
    #1-0,2-1,3-1,4-2,5-2,6-3
    def sidecanflowerbed(self,k):
        if k%2==0:
            return k//2
        else:
            return (k-1)//2
    #1-0,2-0,3-1,4-1,5-2,6-2
    def midcanflowerbed(self,k):
        if k%2==0:
            return k//2-1
        else:
            return (k-1)//2
