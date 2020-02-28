'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hour=[1,2,4,8]
        minus=[1,2,4,8,16,32]
        rep=[]
        for h in range(min(0,num-6),max(num,5)):
            m=num-h
            h_list=self.convertToString(h,hour,"h")
            m_list=self.convertToString(m,minus,"m")
            for h1 in h_list:
                for m1 in m_list:
                    if m1<10:
                        rep.append(str(h1)+":0"+str(m1))
                    else:
                        rep.append(str(h1)+':'+str(m1))
        return rep

    def convertToString(self,k,nums,flag):
        if k==0:
            return [0]
        rep=[]
        def dfs(k,nums,rep,res,flag):
            if k==0:
                rep.append(res)
                return
            if not nums:
                return
            for  i in range(len(nums)):
                if flag=='h' and res+nums[i]<12:
                    dfs(k-1,nums[i+1:],rep,res+nums[i],flag)
                if flag=='m' and res+nums[i]<60:
                    dfs(k-1,nums[i+1:],rep,res+nums[i],flag)
        dfs(k,nums,rep,0,flag)
        return rep
