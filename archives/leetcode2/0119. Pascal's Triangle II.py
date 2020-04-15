class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        rep=[[1],[1,1]]
        while rowIndex>1:
            cur_list=[1]
            last_list=rep[-1]
            for k in range(len(last_list)-1):
                cur_list.append(last_list[k]+last_list[k+1])
            cur_list.append(1)
            rep.append(cur_list)
            rowIndex-=1
        return rep[-1]
