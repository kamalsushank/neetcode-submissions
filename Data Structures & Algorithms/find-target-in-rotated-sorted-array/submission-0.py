class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(left, right):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        # Find pivot (smallest element)
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        pivot = l

        # Search left half
        ans = bs(0, pivot - 1)
        if ans != -1:
            return ans

        # Search right half
        return bs(pivot, len(nums) - 1)