'''
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def dfs(name,typed,cur):
            if not typed:
                if not name:
                    return True
                return False
            else:
                if not name:
                    if typed[0]==cur:
                        return dfs(name,typed[1:],cur)
                    else:
                        return False
                if typed[0]==name[0]:
                    return dfs(name[1:],typed[1:],name[0])
                else:
                    if typed[0]==cur:
                        return dfs(name,typed[1:],cur)
                    else:
                        return False 
        return dfs(name,typed,name[0])
