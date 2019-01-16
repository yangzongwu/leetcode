'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units
of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmaxlsit=[]
        rightmaxlist=[]
        tmpmax=0
        for h in height:
            leftmaxlsit.append(tmpmax)
            if h>tmpmax:
                tmpmax=h
        tmpmax = 0
        for h in height[::-1]:
            rightmaxlist.append(tmpmax)
            if h > tmpmax:
                tmpmax = h
        rightmaxlist=rightmaxlist[::-1]

        totaltrap=0
        for k in range(len(height)):
            curtrap=min(leftmaxlsit[k],rightmaxlist[k])-height[k]
            if curtrap>0:
                totaltrap+=curtrap
        return totaltrap




    def trap01(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rep=0
        for k in range(len(height)):
            rep+=self.detailtrap(k,height)
        return rep
    def detailtrap(self,k,height):
        if k==0:
            return 0
        if k==len(height)-1:
            return 0
        tmp=min(max(height[:k]),max(height[k+1:]))-height[k]
        if tmp>0:
            return tmp
        else:
            return 0

if __name__=='__main__':
    Test=Solution()
    print(Test.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
