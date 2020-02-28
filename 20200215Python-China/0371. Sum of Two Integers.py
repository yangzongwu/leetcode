'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            cur=(a&b)&(2**32-1)
            a=(a^b)&(2**32-1)
            b=(cur<<1)&(2**32-1)
        if a<(2**31-1):
            return a
        else:
            return ~(a^(2**32-1))
            
'''
但是对于 -2 + -2 , 最后结果为 1110 + 1110 = 1100 (12) 会出现问题
结果映射为有符号整数
首先有符号整数的值域应该为 [-8, 7] 对于初步运算的结果,当结果小于8直接返回就可.
对于大于 7 的结果, 可知符号位必为1. 现在的问题转化为, 如何通过位运算把负数转换出来.
假设python用的是 8bit 有符号整数,当前结果为0000 1100, 对应8bit有符号整数为12, 但结果应该为-4对应8bit有符号整数为1111 1100
通过两步转换可以得到:
结果 与 0b1111 异或
对异或结果按位取反
~(a ^ 0xF)
这样就搞定了4bit 有符号加法,同理可以拓展到32bit
'''
