'''
658. Find K Closest Elements
Given a sorted array, two integers k and x, find the k closest elements to x in the array. 
The result should also be sorted in ascending order. 
If there is a tie, the smaller elements are always preferred.
Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        rep=[]
        for num in arr:
            rep.append([abs(num-x),num])
        rep.sort(key=lambda x:x[1])
        rep.sort(key=lambda x:x[0])
        res=[]
        for i in range(k):
            res.append(rep[i][1])
        res.sort()
        return res
 
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        while len(arr)>k:
            if abs(arr[0]-x)<=abs(arr[-1]-x):
                arr.pop()
            else:
                arr.pop(0)
        return arr
#二分查找 转
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        while left < right:
            mid = (right + left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]
