class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)+1
        arr = [0]*(n+1)
        for i in nums :
            if arr[i] == 0 :
                arr[i] +=1
            else:
                return i 
        