class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        cnt_0=0
        cnt_1=0
        for chip in chips:
            if chip%2==0:
                cnt_0+=1
            else:
                cnt_1+=1
        return min(cnt_0,cnt_1)
