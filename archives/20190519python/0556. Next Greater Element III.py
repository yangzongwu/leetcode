class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_list=[]
        for ss in str(n)[::-1]:
            n_list.append(ss)
            
        for k in range(len(n_list)-1):
            if n_list[k]>n_list[k+1]:
                r,cur_val=k,n_list[k]
                for i in range(0,r):
                    if n_list[k+1]<n_list[i]<cur_val:
                        cur_val=n_list[i]
                        r=i
                n_list[r],n_list[k+1]=n_list[k+1],n_list[r]
                cur=n_list[:k+1]
                cur.sort()
                rep=""
                for num in cur:
                    rep=str(num)+rep
                for num in n_list[k+1:]:
                    rep+=str(num)
                res=int(rep[::-1])
                if res>2**31-1:return -1
                return res
        return -1
