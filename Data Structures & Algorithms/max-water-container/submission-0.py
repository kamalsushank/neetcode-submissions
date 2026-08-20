class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxval = 0
        l =0
        r = len(heights)-1
        while l<r:
            ht = min(heights[l],heights[r])
            wd = r-l
            maxval = max(ht*wd , maxval)
            if heights[l] <heights[r]:
                l+=1
            else:
                r-=1
        return maxval
            
