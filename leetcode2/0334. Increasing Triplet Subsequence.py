class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=2**31-1
        second=2**31-1
        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            else:
                return True
        return False
