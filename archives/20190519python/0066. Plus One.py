class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse();
        flag=1;
        for i in range(len(digits)):
            if digits[i]+flag>=10:
                digits[i]=digits[i]+flag-10
                flag=1
            else:
                digits[i]=digits[i]+flag
                flag=0
                break
        if flag==1:
            digits.append(1)
        digits.reverse()
        return digits
#=====================================================================
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag=1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+flag>=10:
                digits[i]=digits[i]+flag-10
                flag=1
            else:
                digits[i]=digits[i]+flag
                flag=0
                break
        if flag==1:
            digits=[1]+digits
        return digits
