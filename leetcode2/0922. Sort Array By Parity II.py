class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        odd=[]
        even=[]
        for num in A:
            if num%2==0:
                odd.append(num)
            else:
                even.append(num)
        rep=[]
        k=0
        while k<len(odd):
            rep.append(odd[k])
            rep.append(even[k])
            k+=1
        return rep
