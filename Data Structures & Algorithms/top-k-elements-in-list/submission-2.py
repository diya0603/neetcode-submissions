from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=defaultdict(int)
        for n in nums:
            m[n]+=1
        heap = []
        for key,val in m.items():
            heapq.heappush(heap,(-val,key))

        out=[]
        for i in range(k):
            val,key=heapq.heappop(heap)
            out.append(key)
        return out   