'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that 
at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''
'''
看到leetcode的提示有two points，这个一直不明白，看到别人的博客，原贴地址，https://segmentfault.com/a/1190000003817671 
这里讲到了相应的原理，如果我们的序列是没有重复的，例如，[1,2,3]。那么可以由每一个下标对应一个数字，0->1 1->2 2->3，我们把这
种映射关系应用出来，从下标0开始，找到0对应的数字，然后将这个数字作为新的下标找到新的数字，直到超出下界。
比如这个例子中我们的路径就是0->1->2->3。 
那么如果序列是重复的，[1,3,3,2]，那么就会有下标对应数字时会有重复，0->1 {1,2}->3 3->2，那么我们的路径就会出现环！ 
0->1->3->2->3->2…，会出现3 2 这个环，那么环开始的地方就是重复的数字啦。
这时我们利用的是leetcode中Linked List Cycle || 的方法，具体可以参见那篇博客。
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=nums[0]
        fast=nums[nums[0]]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[nums[fast]]
        fast=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
