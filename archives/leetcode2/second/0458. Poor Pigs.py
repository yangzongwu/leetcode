class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        k=minutesToTest//minutesToDie+1
        for i in range(0,buckets):
            if k**i>=buckets:
                return i
        
