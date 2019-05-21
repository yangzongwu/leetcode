# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        rep=[]
        self.getBinaryTreePaths(root,str(root.val),rep)
        return rep
    
    def getBinaryTreePaths(self,root,cur,rep):
        if not root.left and not root.right:
            rep.append(cur)
        elif root.left and not root.right:
            self.getBinaryTreePaths(root.left,cur+"->"+str(root.left.val),rep)
        elif not root.left and root.right:
            self.getBinaryTreePaths(root.right,cur+"->"+str(root.right.val),rep)
        else:
            self.getBinaryTreePaths(root.left,cur+"->"+str(root.left.val),rep)
            self.getBinaryTreePaths(root.right,cur+"->"+str(root.right.val),rep)
        
