class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        arr=list(bin(N)[2:])
        i=0
        while i<len(arr):
            arr[i]=int(arr[i])^1
            i+=1
        strs='0b'+''.join(str(s) for s in arr)
        return int(strs,2)
