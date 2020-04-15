class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.insert(0,1)
        flowerbed.append(0)
        flowerbed.append(1)
        
        rep=0
        
        left=0
        while left<len(flowerbed):
            while left<len(flowerbed) and flowerbed[left]!=0:
                left+=1
                
            right=left+1
            while right<len(flowerbed) and flowerbed[right]==0:
                right+=1
            
            rep+=(right-left-1)//2
            
            left=right
            
        return rep>=n
    
