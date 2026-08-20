class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxlen = 0
        for i in s:
            if i-1 not in s:
                l=1
                while i+1 in s:
                    i +=1
                    l+=1
                maxlen = max(maxlen,l)
        return maxlen
            
