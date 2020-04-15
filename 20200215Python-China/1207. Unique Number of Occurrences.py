'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

'''


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_arr = {}
        for num in arr:
            if num not in dict_arr:
                dict_arr[num] = 1
            else:
                dict_arr[num] += 1

        rep = set()
        for k in dict_arr:
            if dict_arr[k] in rep:
                return False
            rep.add(dict_arr[k])

        return True