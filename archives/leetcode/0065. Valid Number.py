'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up 
front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a 
const char * argument, please click the reload button to reset your code definition.
'''
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        while s[0]==' ':
            s=s[1:]
            if not s:
                return False
        while s[-1]==' ':
            s=s[:-1]
            if not s:
                return False
        
        
        isE,isDot,isDigit=False,False,False
        for k in range(len(s)):
            if s[k]=='e':
                if isE or not isDigit:
                    return False
                isE=True
                isDigit=False
            elif s[k] in '+-':
                if k!=0 and s[k-1]!='e':
                    return False
            elif s[k]=='.':
                if isDot or isE:
                    return False
                isDot=True
            elif s[k]  in '1234567890':
                isDigit=True
            else:
                return False
        return isDigit
