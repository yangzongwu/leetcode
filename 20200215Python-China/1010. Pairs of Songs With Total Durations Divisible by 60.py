'''
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500

'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt=0
        dict_time={}
        for n in time:
            n=n%60
            if n not in dict_time:
                dict_time[n]=1
            else:
                dict_time[n]+=1

        cnt=0
        for k in range(1,30):
            if 60-k in dict_time and k in dict_time:
                cnt+=dict_time[k]*dict_time[60-k]

        if 30 in dict_time:
            cnt+=(1+dict_time[30]-1)*(dict_time[30]-1)//2
        if 0 in dict_time:
            cnt+=(1+dict_time[0]-1)*(dict_time[0]-1)//2
        
        return cnt
