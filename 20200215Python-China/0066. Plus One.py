class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag=1
        for k in range(len(digits)-1,-1,-1):
            if flag==0:
                break
            if digits[k]==9:
                digits[k]=0
            else:
                digits[k]+=1
                flag=0
        if flag==1:
            return [1]+digits
        return digits
