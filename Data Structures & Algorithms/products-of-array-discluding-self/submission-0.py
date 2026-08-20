class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i in nums:
            prod *= i
        res = []
        for i in range(len(nums)):
            if nums[i]!=0 :
                res.append(prod//nums[i])
            else:
                p =1
                for j in range(i):
                    p*=nums[j]
                for j in range(i+1,len(nums)):
                    p*=nums[j]
                res.append(p)
        return res