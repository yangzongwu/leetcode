"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        nodelist=[node]
        clonenode=Node(node.val,[])
        dictnode={node:clonenode}
        
        while nodelist:
            curnode=nodelist.pop(0)
            for node in curnode.neighbors:
                if node not in dictnode:
                    nodelist.append(node)
                    newclonenode=Node(node.val,[])
                    dictnode[node]=newclonenode
                    dictnode[curnode].neighbors.append(newclonenode)
                else:
                    dictnode[curnode].neighbors.append(dictnode[node])
        return clonenode
