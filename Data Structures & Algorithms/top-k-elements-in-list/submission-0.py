from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        store = [[i, count[i]] for i in count]
        store.sort(key = lambda x : x[1])
        res = []
        for _ in range(k):
            res.append(store.pop()[0])
        return res
