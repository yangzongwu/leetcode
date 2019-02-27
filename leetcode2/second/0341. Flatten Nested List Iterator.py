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
        self.cnt=0
        self.stack=[]
        self.getlist(nestedList)
        
    def getlist(self,nestedList):
        for cur in nestedList:
            if cur.isInteger():
                self.stack.append(cur.getInteger())
            else:
                self.getlist(cur.getList())
        return 

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext:
            self.cnt+=1
            return self.stack[self.cnt-1]
        return False

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cnt<len(self.stack)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
