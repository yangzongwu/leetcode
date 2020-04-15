class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A=sum(A)
        sum_B=sum(B)
        gap=(sum_A-sum_B)//2
        
        set_B=set(B)
        for num in A:
            if num-gap in set_B:
                return [num,num-gap]
