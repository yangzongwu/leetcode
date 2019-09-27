class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        r=len(arr)
        cur=0
        l=0
        while cur<r:
            if arr[l]!=0:
                cur+=1
            elif arr[l]==0:
                cur+=2
            if cur>=r:
                break
            l+=1
        if cur>r:
            arr[r-1]=0
            r-=1
            l-=1
        r-=1
        while l>=0:
            if arr[l]!=0:
                arr[r]=arr[l]
                r-=1
                l-=1
            else:
                arr[r]=0
                arr[r-1]=0
                r-=2
                l-=1
        
