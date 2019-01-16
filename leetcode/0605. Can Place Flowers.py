'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), 
and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

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
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        rep=0
        left=0
        cntleft=0
        while left<len(flowerbed) and flowerbed[left]!=1:
            cntleft+=1
            left+=1
        if left==len(flowerbed):
            return (len(flowerbed)+1)//2>=n
        else:
            rep+=cntleft//2
        #1001
        right=len(flowerbed)-1
        cntright=0
        while flowerbed[right]!=1 and right>left:
            cntright+=1
            right-=1
        rep+=cntright//2
        rep+=self.subcanPlaceFlowers(flowerbed[left:right+1])
        return rep>=n
    def subcanPlaceFlowers(self,num):
        left=0
        right=1
        rep=0
        while right<len(num):
            tmp=0
            while num[right]==0:
                right+=1
                tmp+=1
            rep+=(tmp-1)//2
            left=right
            right+=1
        return rep
                
  #############################################
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed=[1,0]+flowerbed+[0,1]
        left=0
        rep=0
        while left<len(flowerbed):
            if flowerbed[left]!=0:
                left+=1
            else:
                right=left+1
                while right<len(flowerbed) and flowerbed[right]==0:
                    right+=1
                rep+=(right-1-left)//2
                left=right
        return rep>=n
        
            
            
