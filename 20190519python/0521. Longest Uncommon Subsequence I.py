class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a)==len(b):
            if a!=b:
                return len(a)
            else:
                return -1
        return max(len(a),len(b))
