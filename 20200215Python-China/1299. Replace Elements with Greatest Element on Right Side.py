'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5

'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rep=[0]*len(arr)
        rep[-1]=-1
        for k in range(len(arr)-2,-1,-1):
            rep[k]=arr[k+1]
            arr[k]=max(arr[k],arr[k+1])
        return rep
