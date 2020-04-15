class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split(" ")
        k=0
        while k<len(s_list):
            s_list[k]=s_list[k][::-1]
            k+=1
        return ' '.join(s_list)
