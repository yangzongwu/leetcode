class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split(' ')
        rep=""
        for ss in s_list[::-1]:
            if ss:
                rep+=' '+ss
        return rep[1:]
