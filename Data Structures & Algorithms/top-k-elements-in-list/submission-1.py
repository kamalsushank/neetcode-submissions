from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
        for i,j in count.items():
            buckets[j].append(i)
        res = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res