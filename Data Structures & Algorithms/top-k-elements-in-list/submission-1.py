class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums) + 1)]

        for v in nums:
            counter[v] = counter.get(v, 0) + 1
        
        for n, c in counter.items():
            freq[c].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return res
        



        