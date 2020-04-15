class Solution:
    def canPlaceFlowers(self, flowerbed: 'List[int]', n: 'int') -> 'bool':
        left=0
        while left<len(flowerbed) and flowerbed[left]==0:
            left+=1
        if left==len(flowerbed):
            if left%2==0:
                return left//2>=n
            else:
                return left//2+1>=n
        
        right=len(flowerbed)-1
        while right>=0 and flowerbed[right]==0:
            right-=1
        
        rep=0
        rep+=self.sidePlaceFlowers(left)        
        rep+=self.sidePlaceFlowers(len(flowerbed)-1-right)
        
        k=left
        while k<right:
            j=1
            while k+j<=right and flowerbed[k+j]==0:
                j+=1
            rep+=self.midPlaceFlowers(j-1)
            k+=j
        return rep>=n
    
    def sidePlaceFlowers(self,n):
        return n//2
    
    def midPlaceFlowers(self,n):
        if n<=2:return 0
        return (n-1)//2
