'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lista=[]
        listb=[]
        for ss in a[::-1]:
            lista.append(ss)
        for ss in b[::-1]:
            listb.append(ss)
        if len(lista)>len(listb):
            lista,listb=lista,listb
        else:
            lista,listb=listb,lista
        i=0
        flag='0'
        while i<len(listb):
            if lista[i]=='1' and listb[i]=='1' and flag=='0':
                lista[i]='0'
                flag='1'
            elif lista[i]=='1' and listb[i]=='1' and flag=='1':
                lista[i]='1'
                flag='1'
            elif lista[i]=='0' and listb[i]=='1' and flag=='1':
                lista[i]='0'
                flag='1'
            elif lista[i]=='1' and listb[i]=='0' and flag=='1':
                lista[i]='0'
                flag='1'
            elif lista[i]=='0' and listb[i]=='1' and flag=='0':
                lista[i]='1'
                flag='0'
            elif lista[i]=='1' and listb[i]=='0' and flag=='0':
                lista[i]='1'
                flag='0'
            elif lista[i]=='0' and listb[i]=='0' and flag=='1':
                lista[i]='1'
                flag='0'
            elif lista[i]=='0' and listb[i]=='0' and flag=='0':
                lista[i]='0'
                flag='0'
            i+=1
        
        while i<len(lista):
            if lista[i]=='1' and flag=='1':
                lista[i]='0'
                flag='1'
            elif lista[i]=='0' and flag=='1':
                lista[i]='1'
                flag='0'
            elif lista[i]=='0' and flag=='0':
                lista[i]='0'
                flag='0'
            i+=1
        
        if flag=='1':
            lista.append('1')
        rep=''
        for s in lista[::-1]:
            rep=rep+s
        return rep
        
###################################################################
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
