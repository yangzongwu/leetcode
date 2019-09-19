class Solution:
    def checkValidString(self, s: str) -> bool:
        s_set=set()
        s_set.add(0)
        
        for ss in s:
            cur_set=set()
            if ss=='(':
                for num in s_set:
                    if num>=0:
                        cur_set.add(num+1)
            elif ss==')':
                for num in s_set:
                    cur_set.add(num-1)
            else:
                for num in s_set:
                    cur_set.add(num-1)
                    if num>=0:
                        cur_set.add(num+1)
                        cur_set.add(num)
            s_set=cur_set
        
        return 0 in s_set
