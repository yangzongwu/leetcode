'''
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

 

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
 

Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6

'''
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        r_x=self.rightSide(x,bound)
        r_y=self.rightSide(y,bound)
        
        if x==1 and y==1:
            if bound<2:
                return []
            return [2]
        if x==1:
            return self.singlePowerfulIntegers(y,r_y,bound)
        if y==1:
            return self.singlePowerfulIntegers(x,r_x,bound)
        
        rep=set()
        for i in range(r_x):
            for j in range(r_y):
                if x**i+y**j<=bound:
                    rep.add(x**i+y**j)
                else:
                    break
        return list(rep)

    def singlePowerfulIntegers(self,x,nums,bound):
        rep=[]
        for i in range(nums):
            if x**i+1<=bound:
                rep.append(x**i+1)
        return rep

    def rightSide(self,x,bound):
        l,r=x,bound
        while r>=l:
            mid=(r+l)//2
            if x**mid==bound:
                return mid
            elif x**mid>bound:
                r=mid-1
            else:
                l=mid+1
        return l
