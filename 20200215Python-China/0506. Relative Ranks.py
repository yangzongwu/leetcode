'''
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums_copy=nums[:]
        nums_copy.sort(reverse=True)
        dict_num={}
        cnt=4
        for k in range(len(nums)):
            if k==0:
                dict_num[nums_copy[k]]="Gold Medal"
            elif k==1:
                dict_num[nums_copy[k]]="Silver Medal"
            elif k==2:
                dict_num[nums_copy[k]]="Bronze Medal"
            else:
                dict_num[nums_copy[k]]=str(cnt)
                cnt+=1
        rep=[]
        for num in nums:
            rep.append(dict_num[num])
        return rep
