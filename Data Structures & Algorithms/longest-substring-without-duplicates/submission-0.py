class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0 
        res = 0
        settu = set()
        for r in range(len(s)):
            while s[r] in settu :
                settu.remove(s[l])
                l+=1
            settu.add(s[r])
            res = max(res , r-l+1)
        return res