class Solution:
    def diffWaysToCompute(self, input: 'str') -> 'List[int]':
        nums=self.strToList(input)
        def dfs(nums):
            rep=[]
            if len(nums)==1:
                return [int(nums[0])]
            else:
                for k in range(1,len(nums),2):
                    tmp1=dfs(nums[:k])
                    tmp2=dfs(nums[k + 1:])
                    for l in tmp1:
                        for r in tmp2:
                            if nums[k]=='+':
                                rep.append(l+r)
                            elif nums[k]=='-':
                                rep.append(l-r)
                            else:
                                rep.append(l*r)
            return rep
        return dfs(nums)
        
    
    def strToList(self,input):
        nums=[]
        left=0
        while left<len(input):
            k=1
            while left+k<len(input) and input[left+k] not in '+-*':
                k+=1
            if left+k!=len(input):
                nums.append(input[left:left+k])
                nums.append(input[left+k])
                left=left+k+1
            else:
                nums.append(input[left:left+k])
                left=left+k+1
        return nums
