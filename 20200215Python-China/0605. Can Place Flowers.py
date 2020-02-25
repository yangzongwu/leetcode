'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if sum(flowerbed)==0:
            return (len(flowerbed)+1)//2>=n

        rep=0
        left,right=0,len(flowerbed)-1
        cnt_left,cnt_right=0,0
        
        while left<=right and flowerbed[left]==0:
            left+=1
            cnt_left+=1
        rep+=self.sideFlowerbed(cnt_left)

        while right>=left and flowerbed[right]==0:
            right-=1
            cnt_right+=1
        rep+=self.sideFlowerbed(cnt_right)

        while left<=right:
            while left<=right and flowerbed[left]==1:
                left+=1
            cnt=0
            while left<=right and flowerbed[left]==0:
                left+=1
                cnt+=1
            rep+=self.midFlowered(cnt)
        return rep>=n

    def sideFlowerbed(self,n):
        return n//2
    
    def midFlowered(self,n):
        if n<=1:
            return 0
        return (n-1)//2 

        
