class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        if letters[right]<=target:
            return letters[0]
        
        while left<=right:
            mid=(left+right)//2
            if letters[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return letters[left]
