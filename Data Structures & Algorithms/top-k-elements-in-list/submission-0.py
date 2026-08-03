class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for v in nums:
            counter[v] = counter.get(v, 0) + 1
        
        ordenado = sorted(counter.items(), key=lambda x:x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(ordenado[i][0])

        return res
        



        