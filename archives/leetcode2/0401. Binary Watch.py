class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ['0:00']
        A = [8, 4, 2, 1]
        B = [32, 16, 8, 4, 2, 1]
        rep = []

        # 0<=i<=4
        # 0<=num-i<=6     i>=num-6  i<=num
        for i in range(max(0, num - 6), min(4, num) + 1):
            s1 = self.subreadBinaryWatch(A, i,0)
            s2 = self.subreadBinaryWatch(B, num - i,1)
            for ss1 in s1:
                for ss2 in s2:
                    str1=str(ss1)
                    if ss2>=10:
                        str2=str(ss2)
                    else:
                        str2='0'+str(ss2)
                    rep.append(str1+ ':' +str2)
        return rep

    def subreadBinaryWatch(self, num, k,flag):
        if k==0:
            return [0]
        rep = []
        res = 0

        def dfs(num, k, rep, res,flag):
            if k == 0:
                if flag==0:
                    if res<12:
                        rep.append(res)
                else:
                    if res<60:
                        rep.append(res)
            if not num:
                return
            else:
                for i in range(len(num)):
                    dfs(num[i + 1:], k - 1, rep, res + num[i],flag)

        dfs(num, k, rep, res,flag)
        return rep
