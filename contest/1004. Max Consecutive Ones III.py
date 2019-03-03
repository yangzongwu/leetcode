class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        tmp=[]
        cur=0
        for i in A:
            if i==1:
                cur+=1
            else:
                if cur>0:
                    tmp.append(cur)
                    cur=0
                tmp.append(0)
        if cur>0:
            tmp.append(cur)
        
        left=0
        cnt0=0
        maxrep=0
        cur=left
        if K==0:
            return max(tmp)
        else:
            for cur in range(len(tmp)):
                maxrep+=tmp[cur]
                if tmp[cur]==0:
                    cnt0+=1
                    if cnt0==K:
                        break
                    
        right=cur+1
        cursum=maxrep
        print(tmp)
        while right<len(tmp):
            print(maxrep,cursum,left,right)
            if tmp[right]==0:
                if tmp[left]!=0:
                    cursum=cursum-tmp[left]
                    left+=1
                left+=1
                right+=1
                if right<len(tmp) and tmp[right]!=0:
                    cursum+=tmp[right]
                    maxrep=max(maxrep,cursum)
                    right+=1
            else:
                cursum+=tmp[right]
                maxrep=max(maxrep,cursum)
                right+=1
        return maxrep+K
        
                    
