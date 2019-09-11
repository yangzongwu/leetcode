"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf or quadTree2.isLeaf:
            if quadTree1.isLeaf and quadTree2.isLeaf:
                return Node(quadTree1.val|quadTree2.val,True)
            elif quadTree1.val==True or quadTree2.val==True:
                return Node(True,True)
            elif quadTree1.isLeaf:
                return quadTree2
            elif quadTree2.isLeaf:
                return quadTree1
        else:
            t1=self.intersect(quadTree1.topLeft,quadTree2.topLeft)
            t2=self.intersect(quadTree1.topRight,quadTree2.topRight)
            t3=self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
            t4=self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
            if t1.val==t2.val==t3.val==t4.val and t1.isLeaf and t2.isLeaf and t3.isLeaf and t4.isLeaf:
                return Node(t1.val,True)
            return Node(None,False,t1,t2,t3,t4)
        
        
        
