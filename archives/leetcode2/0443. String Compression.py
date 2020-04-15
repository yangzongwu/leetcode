class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = -1
        cur = 0
        while cur < len(chars):
            if cur + 1 < len(chars) and chars[cur + 1] != chars[cur]:
                cur_chars = chars[cur]
                chars[left + 1] = cur_chars
                left += 1
                cur += 1
            else:
                k = 0
                while cur + k < len(chars) and chars[cur + k] == chars[cur]:
                    k += 1
                cur_chars = chars[cur]
                chars[left + 1] = cur_chars
                if k>1:
                    tmp = k
                    while tmp > 0:
                        chars[left + 1 + len(str(tmp))] = str(tmp % 10)
                        tmp = tmp // 10
                    left = left + len(str(k))+1
                    cur = cur + k
                else:
                    left = left  + 1
                    cur = cur + 1
                    
        return left + 1
