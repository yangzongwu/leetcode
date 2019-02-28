class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]
        dictedges={}
        degreen=[0]*n
        for edge in edges:
            degreen[edge[0]]+=1
            degreen[edge[1]]+=1
            if edge[0] not in dictedges:
                dictedges[edge[0]]=[edge[1]]
            else:
                dictedges[edge[0]].append(edge[1])
            if edge[1] not in dictedges:
                dictedges[edge[1]]=[edge[0]]
            else:
                dictedges[edge[0]].append(edge[1])
        
        stack=[]
        for k in range(len(degreen)):
            if degreen[k]==1:
                stack.append(k)
                
        while len(stack)>2 or max(degreen)>1:
            tmp=[]
            for i in stack:
                for edge in dictedges[i]:
                    degreen[edge]-=1
                    if degreen[edge]==1:
                        tmp.append(edge)
            stack=tmp
            
        return stack
            
