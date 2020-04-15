class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a,b):
            return int(b+a)-int(a+b)
        if len(nums)==0:
            return ''
        if len(nums)==1:
            return str(nums[0])
        if sum(nums)==0:
            return '0'
        nums=sorted([str(s) for s in nums],cmp=compare)
        return ''.join(nums)
