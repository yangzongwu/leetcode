class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt=0
        left=0
        right=0
        while right<len(chars):
            target=chars[right]
            cnt=1
            right+=1
            while right<len(chars) and chars[right]==target:
                right+=1
                cnt+=1
            if cnt==1:
                chars[left]=chars[right-1]
                left+=1
            else:
                chars[left]=chars[right-1]
                left+=1
                for c in str(cnt):
                    chars[left]=c
                    left+=1
        return left
                
