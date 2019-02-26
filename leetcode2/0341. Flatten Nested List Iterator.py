# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        
        self.stack=[]
        self.get_list(nestedList)
        self.index=0
        
        
    def get_list(self,nestedList):
        for tmp in nestedList:
            if tmp.isInteger():
                self.stack.append(tmp.getInteger())
            else:
                self.get_list(tmp.getList())
                
    
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext:  
            self.index+=1
            return self.stack[self.index-1]
        else:
            return False
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index<len(self.stack)

    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
