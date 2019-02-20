class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        if len(nums)==0:
            return []
        if len(nums)==1:
            return nums
        if len(nums)==2:
            return list(set(nums))
        
        
        first=nums[0]
        cnt_f=1
        k=1
        while k<len(nums) and nums[k]==first:
            k+=1
            cnt_f+=1
        if k==len(nums):
            return [first]
        second=nums[k]
        cnt_s=1
        
        for num in nums[k+1:]:
            if num==first:
                cnt_f+=1
            elif num==second:
                cnt_s+=1
            else:
                if cnt_f>=cnt_s:
                    if cnt_s==0:
                        second=num
                        cnt_s=1
                    else:
                        cnt_s-=1
                        cnt_f-=1
                else:
                    if cnt_f==0:
                        first=num
                        cnt_f=1
                    else:
                        cnt_f-=1
                        cnt_s-=1
                        
        cnt_f,cnt_s,cnt=0,0,0
        for num in nums:
            if num==first:
                cnt_f+=1
            if num==second:
                cnt_s+=1
            cnt+=1
            
        #print(first,second,cnt_f,cnt_s,cnt)
        rep=[]
        if (cnt_f)>(cnt/3):
            rep.append(first)
        if (cnt_s)>(cnt/3):
            rep.append(second)
        return rep
