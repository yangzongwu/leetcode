'''
Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

 

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1
 

Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
'''
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs)%5!=0:
            return -1
        
        dict_crock={}
        for k in range(len(croakOfFrogs)):
            if croakOfFrogs[k] not in dict_crock:
                dict_crock[croakOfFrogs[k]]=[k]
            else:
                dict_crock[croakOfFrogs[k]].append(k)
                
        if 'c' not in dict_crock:
            return -1
        
        
        target=len(dict_crock['c'])
        for k in dict_crock:
            if len(dict_crock[k])%target!=0:
                return -1
        

        for k in range(len(dict_crock['c'])):
            cur='c'
            if dict_crock['r'][k]-dict_crock['c'][k]<0:
                return -1
            
            if dict_crock['o'][k]-dict_crock['r'][k]<0:
                return -1
              
            if dict_crock['a'][k]-dict_crock['o'][k]<0:
                return -1
                
            if dict_crock['k'][k]-dict_crock['a'][k]<0:
                return -1   
        
        res=len(dict_crock['c'])
        l_k=0
        l_c=0
        while l_c<len(dict_crock['c']) and l_k<len(dict_crock['k']):
            if dict_crock['c'][l_c]<dict_crock['k'][l_k]:
                l_c+=1
            else:
                res-=1
                l_c+=1
                l_k+=1
        return res
