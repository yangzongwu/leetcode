class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        rep=0
        while left<right:
            rep=max(rep,(right-left)*min(height[left],height[right]))
            if height[left]>=height[right]:
                cur_height=height[right]
                while right>left and height[right]<=cur_height:
                    right-=1
            else:
                cur_height=height[left]
                while left<right and height[left]<=cur_height:
                    left+=1
        return rep
        
