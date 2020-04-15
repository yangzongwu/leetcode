class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        return (sum(nums)-sum(list(set(nums))))//(len(nums)-len(list(set(nums))))
