# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.findTilt(root.left)+self.findTilt(root.right)+abs(self.sumOfTree(root.left)-self.sumOfTree(root.right))
    
    def sumOfTree(self,root):
        if not root:
            return 0
        return root.val+self.sumOfTree(root.left)+self.sumOfTree(root.right)
 #======================================================================================
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.rep=0
        
        def sum_of_tree(root):
            if not root:
                return 0
            
            left_sum=sum_of_tree(root.left)
            right_sum=sum_of_tree(root.right)
            self.rep+=abs(left_sum-right_sum)
            return root.val+left_sum+right_sum
        
        sum_of_tree(root)
        
        return self.rep
