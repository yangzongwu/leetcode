class Solution:
    def reverseWords(self, s: 'str') -> 'str':
        s=s.split(' ')
        rep=''
        for ss in s:
            rep+=ss[::-1]+' '
        return rep[:-1]
