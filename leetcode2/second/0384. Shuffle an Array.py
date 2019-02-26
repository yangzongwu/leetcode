class Solution:

    def __init__(self, nums: 'List[int]'):
        self.nums=nums
        
    def reset(self) -> 'List[int]':
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> 'List[int]':
        """
        Returns a random shuffling of the array.
        """
        nums=self.nums
        num=[i for i in range(0,len(nums))]
        rep=[]
        while num:
            x=random.choice(num)
            num.remove(x)
            rep.append(nums[x])
        return rep

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
