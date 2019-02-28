"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clonenode=Node(node.val,[])
        stack=[node]
        visitstack={node:clonenode}
        
        while stack:
            curnode=stack.pop(0)
            for node in curnode.neighbors:
                if node not in visitstack:
                    cur_clonenode=Node(node.val,[])
                    stack.append(node)
                    visitstack[node]=cur_clonenode
                    visitstack[curnode].neighbors.append(cur_clonenode)
                else:
                    visitstack[curnode].neighbors.append(visitstack[node])
        return clonenode
