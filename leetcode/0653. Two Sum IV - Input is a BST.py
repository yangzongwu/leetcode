'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the 
BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        dictroot=set([])
        listroot=[root]
        while listroot:
            lenlistroot=len(listroot)
            for i in range(lenlistroot):
                curroot=listroot.pop(0)
                if k-curroot.val not in dictroot:
                    dictroot.add(curroot.val)
                else:
                    return True
                if curroot.left:
                    listroot.append(curroot.left)
                if curroot.right:
                    listroot.append(curroot.right)
        return False
                
