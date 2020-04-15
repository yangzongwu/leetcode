class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        rep=[[1],[1,1]]
        while numRows>2:
            cur_list=[1]
            last_list=rep[-1]
            for k in range(len(last_list)-1):
                cur_list.append(last_list[k]+last_list[k+1])
            cur_list.append(1)
            rep.append(cur_list)
            numRows-=1
        return rep
